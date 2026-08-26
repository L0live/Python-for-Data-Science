from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom_and_rotate(image_array: np.array) -> np.array:
    """Zoom into an image and rotate it 90 degrees.

    Args:
        image_array: Image data as np.array.

    Returns:
        np.array: Cropped and rotated grayscale image data.
    """
    assert len(image_array) > 0, "Input image must have a positive length."

    sliced_array = image_array[100: 500, 450: 850, :1]

    print(f"New shape after slicing: {sliced_array.shape} or {sliced_array[:, :, 0].shape}")

    # rotate_array = np.rot90(sliced_array, k=1, axes=(0, 1))
    # Handmade 90-degree rotation
    rotate_array = np.array([[sliced_array[-j, i] for j in range(sliced_array.shape[0]-1, -1, -1)] for i in range(sliced_array.shape[1])])[:, :, 0]

    print(f"New shape after Transpose: {rotate_array.shape}")

    return rotate_array


def main():
    """Load an image, zoom, rotate it, and display the result."""
    image_array = ft_load("animal.jpeg")

    rotated_image = ft_zoom_and_rotate(image_array)

    plt.imshow(np.array(rotated_image), cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
