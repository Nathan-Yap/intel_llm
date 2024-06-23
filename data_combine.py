import os
import json
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def compress_image(image_path, max_size=(128, 128)):
    """Compress image to the specified maximum size."""
    with Image.open(image_path) as img:
        img.thumbnail(max_size)
        return img

def image_to_array(img):
    """Convert compressed image to numpy array."""
    return np.array(img).tolist()

def display_image(img):
    """Display the image using matplotlib."""
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def process_images(directory, max_size=(128, 128)):
    """Process all images in the directory, compress them, and save their data in a JSON file."""
    images_data = []
    
    for filename in os.listdir(directory):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(directory, filename)
            compressed_img = compress_image(image_path, max_size)
            display_image(compressed_img)
            description = input(f"Enter a description for {filename}: ")
            image_array = image_to_array(compressed_img)
            images_data.append({"image": image_array, "description": description})
    
    with open('images_data.json', 'w') as json_file:
        json.dump(images_data, json_file)

if __name__ == "__main__":
    image_directory = 'images'
    process_images(image_directory, max_size=(128, 128))