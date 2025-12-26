from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
    """Load an image from file and convert to array.
    
    Args:
        path: Path to the image file.
    
    Returns:
        list: Image data as a nested list (array representation).
    """
    image = Image.open(path)
    image_array = np.array(image)

    print("The shape of image is:", image_array.shape)

    return image_array.tolist()
