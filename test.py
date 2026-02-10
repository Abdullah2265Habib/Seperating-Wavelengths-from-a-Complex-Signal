import os
import numpy as np
import librosa
import soundfile as sf

input_folder = "audio"
output_folder = "output"
audio_file = os.path.join(input_folder, "sound.mp4")

os.makedirs(output_folder, exist_ok=True)

#extract audio
signal, fs = librosa.load(audio_file, sr=None, mono=True)
t = np.linspace(0, len(signal) / fs, len(signal), endpoint=False)