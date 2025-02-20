import os
from PIL import Image

INPUT_FOLDER = "input_photos"
OUTPUT_FOLDER = "output_photos"
IMAGE_FORMAT = "JPEG"
IMAGE_QUALITY = 40

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

files_to_compress = os.listdir(INPUT_FOLDER)

for file in files_to_compress:
    input_path = os.path.join(INPUT_FOLDER, file)
    output_path = os.path.join(OUTPUT_FOLDER, file)

    photo = Image.open(input_path)

    photo.save(output_path, IMAGE_FORMAT, quality=IMAGE_QUALITY)
