from PIL import Image
import numpy as np
import os


image_path = os.getcwd()+'\\sample.png'
image = Image.open(image_path)

image_array = np.array(image)


red_color = (255, 0, 0)
green_color = (0, 255, 0)
blue_color = (0, 0, 255)


red_pixels = np.sum(np.all(image_array == red_color, axis=-1))
green_pixels = np.sum(np.all(image_array == green_color, axis=-1))
blue_pixels = np.sum(np.all(image_array == blue_color, axis=-1))

print(f"red : {red_pixels} pixels")
print(f"green : {green_pixels} pixels")
print(f"blue : {blue_pixels} pixels")
