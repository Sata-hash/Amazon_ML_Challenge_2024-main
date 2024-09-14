import os
import cv2
import pandas as pd

# Directories
input_dir = 'denoised_images'
output_file = 'edges_data.csv'

# List to store flattened edge data
edges_data = []

# Process each image
for img_name in os.listdir(input_dir):
    img_path = os.path.join(input_dir, img_name)
    if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        edges = cv2.Canny(img, 100, 200)

        # Flatten and append to list
        edges_data.append(edges.flatten())

# Create DataFrame and save to CSV
df = pd.DataFrame(edges_data)
df.to_csv(output_file, index=False)
print(f"Edge data saved to {output_file}")
