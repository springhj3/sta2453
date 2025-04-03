import pandas as pd
from PIL import Image
import os

# Crop Images

# Reload the CSV file
csv_file_path = r'C:\Users\sprin\Downloads\SIMC_OverlapTiffsWithPP\SIMC_OverlapTiffsWithPP\SIMC.Overlap.csv\20180529_SIMC_200_2mm_rep2_redo_KG_data.csv'
data = pd.read_csv(csv_file_path)#.sort_values(by='Class')

# Dictionary to store loaded .tif images
tif_images = {}

# Extract the first 10 rows for testing
data = data[data['Class'] == 'CountGT500']
test_particles = data[['Class', 'Image.File', 'Image.X', 'Image.Y', 'Image.Width', 'Image.Height']].head(5)

# Ensure the output directory exists
output_dir = r"crop_images\big_particles\20180529_SIMC_200_2mm_rep2_redo_KG_data"
os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

# Loop through each row, load the corresponding tif file, and crop the image
for idx, particle in test_particles.iterrows():
    tif_filename = particle['Image.File']
    tif_path = fr"C:\Users\sprin\Downloads\SIMC_OverlapTiffsWithPP\SIMC_OverlapTiffsWithPP\{tif_filename}"  # Assuming .tif files are in the same directory

    # Load the .tif image if not already loaded
    if tif_filename not in tif_images:
        try:
            tif_images[tif_filename] = Image.open(tif_path)
        except FileNotFoundError:
            print(f"Warning: {tif_filename} not found, skipping this row.")
            continue

    # Define the crop box (left, upper, right, lower)
    crop_box = (
        int(particle['Image.X']),  # Starting X (left)
        int(particle['Image.Y']),  # Starting Y (upper)
        int(particle['Image.X'] + particle['Image.Width']),  # Ending X (right)
        int(particle['Image.Y'] + particle['Image.Height'])  # Ending Y (lower)
    )

    # Crop the image
    cropped_image = tif_images[tif_filename].crop(crop_box)

    # Save the cropped image
    output_path = fr"{output_dir}_{idx + 1}.png"
    cropped_image.save(output_path)
    print(f"Cropped particle {idx + 1} from {tif_filename} saved as {output_path}")