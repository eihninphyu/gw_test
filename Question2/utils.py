import os
from PIL import Image
import numpy as np

def get_modified_mask_image():
    background_path = os.getcwd()+'\\background.jpg'
    mask_path = os.getcwd()+'\\mask.png'
    foreground_path = os.getcwd()+'\\foreground.jpg'
    foreground = Image.open(foreground_path)
    background = Image.open(background_path)
    mask = Image.open(mask_path)

    background = background.resize(foreground.size)
    mask = mask.resize(foreground.size)

    foreground = np.array(foreground)
    background = np.array(background)
    mask = np.array(mask)

    # Ensure all images have the same dimensions
    if (foreground.shape[:2] != mask.shape[:2]) or (background.shape[:2] != mask.shape[:2]):
        raise ValueError("All images must have the same dimensions.")

    # Define conditions to identify red and green pixels in the mask (adjust as needed)
    red_condition = (mask[..., 0] > 200) & (mask[..., 1] < 100) & (mask[..., 2] < 100)
    green_condition = (mask[..., 0] < 100) & (mask[..., 1] > 200) & (mask[..., 2] < 100)

    # Create a modified mask by replacing red pixels with foreground and green pixels with background
    modified_mask = np.where(red_condition[..., np.newaxis], foreground, mask)
    modified_mask = np.where(green_condition[..., np.newaxis], background, modified_mask)

    # Save the modified result3 image
    modified_mask_image = Image.fromarray(modified_mask)
    return modified_mask_image

def crop_1024x1024_pixels(modified_mask):
    # Calculate the center of gravity (COG) of the person in the mask
    y, x = np.where(modified_mask[..., 2] > 0)  # Find non-transparent pixels
    cog_y, cog_x = int(np.mean(y)), int(np.mean(x))

    # Define the cropping dimensions (1024x1024)
    crop_size = 1024
    half_crop = crop_size // 2

    # Calculate the cropping box with COG at the center
    crop_box = (
        max(cog_x - half_crop, 0),
        max(cog_y - half_crop, 0),
        min(cog_x + half_crop, modified_mask.shape[1]),
        min(cog_y + half_crop, modified_mask.shape[0]),
    )

    cropped_image = modified_mask[crop_box[1]:crop_box[3], crop_box[0]:crop_box[2]]

    cropped_image = Image.fromarray(cropped_image)

    cropped_image = cropped_image.resize((crop_size, crop_size))
    return cropped_image

def rotate_30degree_clockwise(cropped_image):
    center_x, center_y = cropped_image.width / 2, cropped_image.height / 2

    # Rotate the cropped image by 30 degrees clockwise around the center
    rotated_image = cropped_image.rotate(-30, center=(center_x, center_y), resample=Image.BICUBIC, expand=True)

    return rotated_image