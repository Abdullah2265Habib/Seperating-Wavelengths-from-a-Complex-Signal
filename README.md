# Seperating-Wavelengths-from-a-Complex-Signal-Using-Fourier-Transformation

## Overview

This project demonstrates how to **generate**, **analyze**, and **separate** a complex signal composed of multiple sine waves using the **Fast Fourier Transform (FFT)** in Python.

The workflow includes:
- Time-domain signal synthesis
- Frequency-domain analysis via FFT
- Isolation of individual frequency components
- Reconstruction of separated signals using inverse FFT

This is a foundational example in **Digital Signal Processing (DSP)**.

---

## Technologies Used

- **Python 3**
- **NumPy** – numerical computation
- **Matplotlib** – visualization

---

## Mathematical Background

### 1. Continuous-Time Sinusoidal Signal

Each sinusoidal component is defined as:

$$
x(t) = A \sin(2\pi f t)
$$

Where:
- \( A \) = amplitude  
- \( f \) = frequency (Hz)  
- \( t \) = time (seconds)

---

### 2. Composite Signal

The generated signal is a sum of three sine waves:

$$
x(t) = \sin(2\pi \cdot 5 t) + 0.5 \sin(2\pi \cdot 20 t) + 0.2 \sin(2\pi \cdot 50 t)
$$

| Frequency (Hz) | Amplitude |
|----------------|-----------|
| 5              | 1.0       |
| 20             | 0.5       |
| 50             | 0.2       |

---

### 3. Discrete Fourier Transform (DFT)

The DFT converts a discrete time-domain signal into the frequency domain:

$$
X(k) = \sum_{n=0}^{N-1} x(n) e^{-j 2\pi k n / N}
$$

Where:
- \( x(n) \) is the time-domain signal  
- \( X(k) \) is the frequency-domain representation  
- \( N \) is the number of samples  

In practice, the **Fast Fourier Transform (FFT)** is used for computational efficiency.

---

### 4. Frequency Resolution

The frequency resolution is:

$$
\Delta f = \frac{f_s}{N}
$$

Where:
- \( f_s \) = sampling frequency  
- \( N \) = number of samples  

In this project:
- \( f_s = 1000 \text{ Hz} \)  
- \( N = 1000 \)  
- \( \Delta f = 1 \text{ Hz} \)

---

## Code Walkthrough

### 1. Signal Generation (Time Domain)

- Sampling frequency: **1000 Hz**  
- Duration: **1 second**  
- Three sinusoidal components are summed to create a composite waveform.

📈 **Output:** Time-domain plot of the composite signal.

---

### 2. Frequency Spectrum (FFT)

- FFT converts the signal from the **time domain → frequency domain**.  
- Only **positive frequencies** are plotted.  
- The magnitude spectrum reveals peaks at:
  - **5 Hz**
  - **20 Hz**
  - **50 Hz**

The FFT magnitude is computed as:

$$
|X(f)| = \sqrt{\Re\{X(f)\}^2 + \Im\{X(f)\}^2}
$$

Because the input signal is real-valued, its Fourier Transform is symmetric:

$$
X(-f) = X^*(f)
$$

Hence, only **positive frequencies** are visualized.

📊 **Output:** Frequency spectrum using a stem plot.

---

### 3. Frequency Isolation (Band-Pass Filtering)

Each frequency component is isolated using a narrow frequency mask:

$$
|f - f_0| \leq \text{bandwidth}
$$

Where:
- \( f_0 \) = target frequency  
- Bandwidth = **1 Hz**  

Steps:
1. Copy the FFT data  
2. Zero out all frequencies outside the target band  
3. Apply inverse FFT

---

### 4. Signal Reconstruction (Inverse FFT)

The inverse FFT is defined as:

$$
x(n) = \frac{1}{N} \sum_{k=0}^{N-1} X(k) e^{j 2 \pi k n / N}
$$

This reconstructs the isolated sinusoidal components in the time domain.

📉 **Output:**
- Overlaid plot of all separated components  
- Individual subplots for each frequency

---

## Visual Outputs

1. **Composite Time-Domain Signal**  
2. **Frequency Spectrum (Magnitude vs Frequency)**  
3. **Overlaid Separated Frequency Components**  
4. **Individual Frequency Component Subplots**

---

## Key Concepts Demonstrated

- Signal superposition  
- FFT and inverse FFT  
- Frequency-domain filtering  
- Time–frequency duality  
- Spectral analysis

---

## Applications

- Audio signal processing  
- Vibration analysis  
- Communications systems  
- Biomedical signal analysis (EEG, ECG)  
- Feature extraction in machine learning

---

## How to Run

```bash
pip install numpy matplotlib
python app.py
