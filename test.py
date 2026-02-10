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