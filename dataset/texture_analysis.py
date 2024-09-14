import os
import cv2
import numpy as np
from skimage.feature import local_binary_pattern

# Directories
input_dir = 'denoised_images'
output_dir = 'lbp_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parameters for LBP
radius = 1
n_points = 8 * radius

# Process each image
for img_name in os.listdir(input_dir):
    img_path = os.path.join(input_dir, img_name)
    if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Read the image in grayscale
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        # Compute LBP
        lbp = local_binary_pattern(img, n_points, radius, method='uniform')

        # Convert LBP result to uint8 by normalizing to [0, 255] range
        lbp_uint8 = np.uint8(lbp * (255 / np.max(lbp)))

        # Save the result
        output_path = os.path.join(output_dir, img_name)
        cv2.imwrite(output_path, lbp_uint8)
        print(f"Processed and saved LBP image for {img_name}")
