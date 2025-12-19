from PIL import Image
import numpy as np

def ft_load(path: str) -> list:
    image = Image.open(path)
    image_array = np.array(image)

    print("The shape of image is:", image_array.shape)

    return image_array.tolist()