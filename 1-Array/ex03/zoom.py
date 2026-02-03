from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(image: list) -> list:
    """Zoom into the center of an image by cropping.

    Args:
        image: Image data as a nested list.

    Returns:
        list: Cropped/zoomed grayscale image data.
    """
    assert len(image) > 0, "Input image must have a positive length."

    image_array = np.array(image)

    sliced_array = image_array[100: 500, 450: 850, :1]

    return sliced_array


def main():
    """Load an image, zoom into it, and display the result."""
    # np.set_printoptions(threshold = False)
    image = ft_load("animal.jpeg")
    # print(image)

    zoomed_image = ft_zoom(image)
    print(f"New shape after slicing: {zoomed_image.shape} or {zoomed_image[:, :, 0].shape}")
    # print(zoomed_image)
    plt.imshow(zoomed_image, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
