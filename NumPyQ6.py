import numpy as np
import matplotlib.pyplot as plt
rgb_image = np.random.rand(100, 100, 3)
swapped_rgb = rgb_image[..., [2, 1, 0]]
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(rgb_image)

plt.subplot(1, 2, 2)
plt.title("Swapped")
plt.imshow(swapped_rgb)
plt.show()