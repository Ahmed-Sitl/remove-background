from rembg import remove
from PIL import Image

# Input path
input_path = 'ahmed.jpg'

# Output path
output_path = 'ahmed1.jpg'

# Open input image
input = Image.open(input_path)

# Remove background
output = remove(input)

# Convert image to RGB if it's in RGBA mode
if output.mode == 'RGBA':
    output = output.convert('RGB')

# Save the output image
output.save(output_path)
