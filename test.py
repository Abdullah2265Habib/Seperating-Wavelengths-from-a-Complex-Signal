import os

input_folder = "audio"
output_folder = "output"
audio_file = os.path.join(input_folder, "sound.mp4")

os.makedirs(output_folder, exist_ok=True)


