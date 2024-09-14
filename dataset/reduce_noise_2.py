import pandas as pd
import requests
import os
from PIL import Image
from io import BytesIO
import cv2
import numpy as np

# Step 1: Load CSV file
csv_file = 'sample_test.csv'  # Change this to the path of your CSV file
df = pd.read_csv(csv_file)

# Step 2: Create a directory to save the images
save_dir = 'downloaded_images4'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Step 3: Set the target size for normalization (resizing)
target_size = (256, 256)  # Change to the size you want

# Step 4: Loop through the URLs, download images, resize them, and apply noise reduction
for index, row in df.iterrows():
    url = row['image_link']  # Replace with the actual column name that contains the URLs
    img_name = f'image_{index}.jpg'  # Customize the naming convention
    img_path = os.path.join(save_dir, img_name)

    try:
        # Step 5: Download the image
        response = requests.get(url)
        if response.status_code == 200:
            # Step 6: Open the image with Pillow
            img = Image.open(BytesIO(response.content))

            # Step 7: Resize the image
            img = img.resize(target_size)

            # Convert the image to a NumPy array for OpenCV
            img_np = np.array(img)

            # Step 8: Apply noise reduction using Non-Local Means Denoising
            # h = strength of denoising, 10 is a good starting point
            img_denoised = cv2.fastNlMeansDenoisingColored(img_np, None, 10, 10)

            # Convert back to PIL Image
            img_clean = Image.fromarray(img_denoised)

            # Step 9: Save the noise-reduced and resized image
            img_clean.save(img_path)
            print(f"Downloaded, resized, and denoised {img_name}")
        else:
            print(f"Failed to download {img_name}")
    except Exception as e:
        print(f"Error processing {img_name}: {e}")
