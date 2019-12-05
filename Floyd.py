import matplotlib.pyplot as plt
import numpy as np
import imageio
import math




def floyd_steinberg(i):





image = imageio.imread("sthlm.jpg")
image_bw = np.mean(image, axis=2)
plt.imshow(image_bw, cmap="gray")
plt.title("Original image")
plt.show()

mean_image = floyd_steinberg(image_bw)
plt.imshow(mean_image.astype('uint8'), cmap="gray")
plt.title("Halftoned image")
plt.show()
