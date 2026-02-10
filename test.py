import os
import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt

input_folder = "audio"
output_folder = "output"
audio_file = os.path.join(input_folder, "sound.wav")

os.makedirs(output_folder, exist_ok=True)

#extract audio
signal, fs = librosa.load(audio_file, sr=None, mono=True)
t = np.linspace(0, len(signal) / fs, len(signal), endpoint=False)

#ploting the original sound signal
plt.figure(figsize=(10, 4))
plt.plot(t, signal)
plt.title("Audio Signal (Time Domain)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()

#apply fourier transformation
fft_vals = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(fft_vals), d=1/fs)

positive_freqs = freqs[:len(freqs)//2]
magnitude = np.abs(fft_vals[:len(fft_vals)//2])

#frequency spectrum
plt.figure(figsize=(10, 4))
plt.plot(positive_freqs, magnitude)
plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, fs / 2)
plt.tight_layout()
plt.show()

#isolate single frequency components
bands = [
    (0, 300),      #low frequencies
    (300, 2000),   #mid frequencies
    (2000, 8000)   #high frequencies
]

for low, high in bands:
    filtered_fft = fft_vals.copy()

    mask = (np.abs(freqs) < low) | (np.abs(freqs) > high)
    filtered_fft[mask] = 0

    filtered_signal = np.fft.ifft(filtered_fft).real

    #save separated audio
    output_path = os.path.join(output_folder, f"{low}_{high}_Hz.wav")
    sf.write(output_path, filtered_signal, fs)

    #plot separated waveform
    plt.figure(figsize=(10, 3))
    plt.plot(t, filtered_signal)
    plt.title(f"{low}–{high} Hz Component")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()