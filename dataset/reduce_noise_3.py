import os
from PIL import Image
import cv2
import numpy as np

# Step 1: Set the directory where the images are stored
image_dir = 'downloaded_images4'  # Change to your actual directory where images are saved
save_dir = 'denoised_images'      # Directory to save denoised images

# Create directory to save denoised images if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Step 2: Loop through the images in the directory
for img_name in os.listdir(image_dir):
    img_path = os.path.join(image_dir, img_name)

    try:
        # Step 3: Open the image using Pillow
        img = Image.open(img_path)

        # Convert the image to a NumPy array for OpenCV
        img_np = np.array(img)

        # Step 4: Apply noise reduction using Non-Local Means Denoising
        img_denoised = cv2.fastNlMeansDenoisingColored(img_np, None, 10, 10)

        # Convert back to PIL Image
        img_clean = Image.fromarray(img_denoised)

        # Step 5: Save the denoised image
        denoised_img_path = os.path.join(save_dir, img_name)
        img_clean.save(denoised_img_path)
        print(f"Denoised and saved {img_name}")

    except Exception as e:
        print(f"Error processing {img_name}: {e}")
