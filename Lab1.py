import matplotlib.pyplot as plt
import numpy as np
import imageio
import math




sthlm = imageio.imread("katter.jpg")
sthlm_bw = np.mean(sthlm, axis=2)
plt.imshow(sthlm_bw, cmap="gray")
plt.title("Stockholm original")

image = imageio.imread("sthlm.jpg")
image_bw = np.mean(image, axis=2)
plt.imshow(image_bw, cmap="gray")
plt.title("Original image")
plt.show()

mean_image = halftoning(image_bw, 4)
plt.imshow(mean_image.astype('uint8'), cmap="gray")
plt.title("Halftoned image")
plt.show()
