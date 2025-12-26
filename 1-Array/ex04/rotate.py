from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom_and_rotate(image: list, zoom_scale: int) -> list:
    """Zoom into an image and rotate it 90 degrees.

    Args:
        image: Image data as a nested list.
        zoom_scale: Factor determining the crop size.

    Returns:
        list: Cropped and rotated grayscale image data.
    """
    assert len(image) > 0, "Input image must have a positive length."

    image_array = np.array(image)
    h = image_array.shape[0]
    w = image_array.shape[1]

    sliced_array = image_array[h//zoom_scale: -h//zoom_scale, w//zoom_scale: -w//zoom_scale, 0]

    # rotate_array = np.rot90(sliced_array, k=1, axes=(0, 1))
    # Handmade 90-degree rotation
    rotate_array = np.array([[sliced_array[j, i] for j in range(sliced_array.shape[0]-1, -1, -1)] for i in range(sliced_array.shape[1])])

    return rotate_array[()].tolist()


def main():
    """Load an image, zoom, rotate it, and display the result."""
    image = ft_load("animal.jpeg")

    rotated_image = ft_zoom_and_rotate(image, 4)

    plt.imshow(np.array(rotated_image), cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
