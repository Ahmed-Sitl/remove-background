# Background Removal Script

This project demonstrates how to use the `rembg` library in combination with `Pillow` to remove the background from an image. It reads an input image, removes its background, and saves the result.

## Prerequisites

Make sure you have Python installed on your system. You'll also need to install the following Python library:

- [rembg](https://pypi.org/project/rembg/)

You can install these libraries using `pip`:

```bash
pip install rembg
```

## Usage

1. Clone the repository or download the script.

   ```bash
   git clone https://github.com/ahmed-sitl/remove-background.git
   cd remove-background
   ```

2. Place the image you want to process in the same directory as the script and update the `input_path` variable in `main.py` to the image file name.

3. Run the script:

   ```bash
   python main.py
   ```

4. The output image with the background removed will be saved in the same directory as `ahmed.jpg`.

## Code

```python
from rembg import remove
from PIL import Image

# Input path
input_path = 'ahmed.jpeg'

# Output path
output_path = 'ahmed.jpg'

# Open input image
input = Image.open(input_path)

# Remove background
output = remove(input)

# Convert image to RGB if it's in RGBA mode
if output.mode == 'RGBA':
    output = output.convert('RGB')

# Save the output image
output.save(output_path)
```

## Example

Here is an example of the input image and the output image after background removal:

### Input Image

![Input Image](ahmed.jpeg)

### Output Image

![Output Image](ahmed.jpg)

### Input Image

![Input Image](elon.jpg)

### Output Image

![Output Image](elon1.jpg)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
