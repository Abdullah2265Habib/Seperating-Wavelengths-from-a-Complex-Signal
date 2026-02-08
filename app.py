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

