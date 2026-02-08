import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

f1 = 5
f2 = 20
f3 = 50

signal = (
    np.sin(2 * np.pi * f1 * t) +
    0.5 * np.sin(2 * np.pi * f2 * t) +
    0.2 * np.sin(2 * np.pi * f3 * t)
)

plt.plot(t, signal)
plt.title("Complex Signal (Time Domain)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

#apply fourier transformation
fft_vals = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(fft_vals), 1 / fs)

positive_freqs = freqs[:len(freqs)//2]
magnitude = np.abs(fft_vals[:len(fft_vals)//2])

#frequency spectrum
plt.stem(positive_freqs, magnitude, basefmt=" ")
plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, 100)
plt.show()

#isolate single frequency components
frequencies = [5, 20, 50]
bandwidth = 1  # Hz

plt.figure(figsize=(10, 6))

for f in frequencies:
    filtered_fft = fft_vals.copy()
    mask = (np.abs(freqs - f) > bandwidth) & (np.abs(freqs + f) > bandwidth)
    filtered_fft[mask] = 0
    filtered_signal = np.fft.ifft(filtered_fft).real
    plt.plot(t, filtered_signal, label=f"{f} Hz")

plt.title("Separated Frequency Components")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()

plt.figure(figsize=(10, 8))
for i, f in enumerate(frequencies, 1):
    filtered_fft = fft_vals.copy()
    mask = (np.abs(freqs - f) > bandwidth) & (np.abs(freqs + f) > bandwidth)
    filtered_fft[mask] = 0
    filtered_signal = np.fft.ifft(filtered_fft).real

    plt.subplot(3, 1, i)
    plt.plot(t, filtered_signal)
    plt.title(f"{f} Hz component")
    plt.ylabel("Amplitude")

plt.xlabel("Time (s)")
plt.tight_layout()
plt.show()
