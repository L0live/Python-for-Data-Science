from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom_and_rotate(image: list) -> list:
    """Zoom into an image and rotate it 90 degrees.

    Args:
        image: Image data as a nested list.

    Returns:
        list: Cropped and rotated grayscale image data.
    """
    assert len(image) > 0, "Input image must have a positive length."

    image_array = np.array(image)

    sliced_array = image_array[100: 500, 450: 850, :1]

    print(f"New shape after slicing: {sliced_array.shape} or {sliced_array[:, :, 0].shape}")

    # rotate_array = np.rot90(sliced_array, k=1, axes=(0, 1))
    # Handmade 90-degree rotation
    rotate_array = np.array([[sliced_array[-j, i] for j in range(sliced_array.shape[0]-1, -1, -1)] for i in range(sliced_array.shape[1])])[:, :, 0]

    print(f"New shape after Transpose: {rotate_array.shape}")

    return rotate_array[()].tolist()


def main():
    """Load an image, zoom, rotate it, and display the result."""
    image = ft_load("animal.jpeg")

    rotated_image = ft_zoom_and_rotate(image)

    plt.imshow(np.array(rotated_image), cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
