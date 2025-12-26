from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(image: list, zoom_scale: int) -> list:
    """Zoom into the center of an image by cropping.

    Args:
        image: Image data as a nested list.
        zoom_scale: Factor determining the crop size (higher = more zoom).

    Returns:
        list: Cropped/zoomed grayscale image data.
    """
    assert len(image) > 0, "Input image must have a positive length."

    image_array = np.array(image)
    h = image_array.shape[0]
    w = image_array.shape[1]

    sliced_array = image_array[h//zoom_scale: -h//zoom_scale, w//zoom_scale: -w//zoom_scale, 0]

    return sliced_array[()].tolist()


def main():
    """Load an image, zoom into it, and display the result."""
    image = ft_load("animal.jpeg")

    zoomed_image = ft_zoom(image, 4)

    plt.imshow(np.array(zoomed_image), cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
