import pandas as pd
from PIL import Image

# # Specify the file path
# file_path = r"C:\Users\sprin\OneDrive - University of Toronto\HURON_OverlapTiffsWithPP\HURONOvlerap_csv\20170411_FISHI_003_2mm_rep3_KG_data.csv"

# # Read the CSV file into a pandas DataFrame
# data = pd.read_csv(file_path)

# # Display the first few rows of the data
# print(data.head())

# Load the .tif mosaic image
tif_image_path = r'C:\Users\sprin\Downloads\SIMC_OverlapTiffsWithPP\SIMC_OverlapTiffsWithPP\20170510_Simcoe_95_2mm_rep1_000001.tif'
tif_image = Image.open(tif_image_path)

# Sample data: coordinates and dimensions of particles
# This data should come from your CSV file (e.g., Image.X, Image.Y, Image.Width, Image.Height)
particles_info = [
    {'id': 1, 'x': 78, 'y': 0, 'width': 127, 'height': 94},  # Example particle
]

# Crop and save each particle
for particle in particles_info:
    # Define the crop box (left, upper, right, lower)
    crop_box = (
        particle['x'],  # Starting X (left)
        particle['y'],  # Starting Y (upper)
        particle['x'] + particle['width'],  # Ending X (right)
        particle['y'] + particle['height']  # Ending Y (lower)
    )
    
    # Crop the image
    cropped_image = tif_image.crop(crop_box)
    
    # Save the cropped image
    output_path = f"particle_{particle['id']}.png"
    cropped_image.save(output_path)
    print(f"Cropped particle {particle['id']} saved as {output_path}")