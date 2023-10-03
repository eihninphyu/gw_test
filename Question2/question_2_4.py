from utils import get_modified_mask_image,crop_1024x1024_pixels,rotate_30degree_clockwise
import numpy as np
from PIL import Image

modified_mask = np.array(get_modified_mask_image())

cropped_image = crop_1024x1024_pixels(modified_mask)

rotate_image = rotate_30degree_clockwise(cropped_image)

rotate_image.save('result4.jpg', format='JPEG')
