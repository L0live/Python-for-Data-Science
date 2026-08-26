from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt

image_array = ft_load("landscape.jpg")

plt.imshow(ft_invert(image_array))
plt.show()
plt.imshow(ft_red(image_array))
plt.show()
plt.imshow(ft_green(image_array))
plt.show()
plt.imshow(ft_blue(image_array))
plt.show()
plt.imshow(ft_grey(image_array), cmap='gray')
plt.show()

print(ft_invert.__doc__)