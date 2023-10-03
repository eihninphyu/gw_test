from PIL import Image
import numpy as np
import os

image_path = os.getcwd()+'\\sample.png' 
image = Image.open(image_path)

image_array = np.array(image)

white_color = (255, 255, 255)
black_color = (0, 0, 0)

red_color = (255, 0, 0)
red_mask = np.all(image_array == red_color, axis=-1)


image_array[red_mask] = white_color
image_array[~red_mask] = black_color

result_image = Image.fromarray(image_array)

result_image.save('result.png')

