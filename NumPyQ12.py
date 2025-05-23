import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("Flower.png")
img_np = np.array(img)
height, width, _ = img_np.shape  # height = 500, width = 600
center_y = height // 2  # 250
center_x = width // 2   # 300

half_crop = 100 // 2  # 50
cropped = img_np[
    center_y - half_crop : center_y + half_crop,
    center_x - half_crop : center_x + half_crop
]
plt.imshow(cropped)
plt.title("Center 100x100 Crop")
plt.axis('off')
plt.show()
