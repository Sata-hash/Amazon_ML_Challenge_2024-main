import pandas as pd
import requests
import os

# Step 1: Load CSV file
csv_file = 'sample_test.csv'  # Change this to the path of your CSV file
df = pd.read_csv(csv_file)

# Step 2: Create a directory to save the images
save_dir = 'downloaded_images'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Step 3: Loop through the URLs and download images
for index, row in df.iterrows():
    url = row['image_link']  # Replace with the actual column name that contains the URLs
    img_name = f'image_{index}.jpg'  # You can customize the naming convention
    img_path = os.path.join(save_dir, img_name)

    # Step 4: Download the image
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(img_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {img_name}")
        else:
            print(f"Failed to download {img_name}")
    except Exception as e:
        print(f"Error downloading {img_name}: {e}")

