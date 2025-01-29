from PIL import Image
import os
import math

# Path to the folder containing PNG images
folder_path = r"C:\Users\sprin\STA2453\sta2453\test"

# Get all PNG files from the folder
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png')]
image_files.sort()  # Sort for consistent ordering

# Open images
images = [Image.open(img) for img in image_files]

# Define grid size (e.g., automatic square grid)
grid_size = math.ceil(math.sqrt(len(images)))  # Try to make it as square as possible

# Get the maximum width and height from all images
max_width = max(img.width for img in images)
max_height = max(img.height for img in images)

# Create a new blank image with grid dimensions
combined_width = grid_size * max_width
combined_height = grid_size * max_height
grid_image = Image.new('RGBA', (combined_width, combined_height))

# Place images in the grid
x_offset, y_offset = 0, 0

for i, img in enumerate(images):
    # Paste the image into the grid
    grid_image.paste(img, (x_offset, y_offset))

    # Move to the next column
    x_offset += max_width
    
    # If we reach the end of a row, move to the next row
    if (i + 1) % grid_size == 0:
        x_offset = 0
        y_offset += max_height

# Save the final grid image
output_path = os.path.join(folder_path, "image_grid.png")
grid_image.save(output_path)

print(f"Grid image saved to: {output_path}")
