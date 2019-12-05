import matplotlib.pyplot as plt
import numpy as np
import imageio
import math


def halftoning(i, bs):
    i = 255 - i
    floyd = np.zeros(i.shape)
    size = i.size

    error = np.zeros(size(i))

    all_blocks = np.zeros(i.shape)

    for p in range(0, math.floor(i.shape[0] / bs)):
        for q in range(0, math.floor(i.shape[1] / bs)):
            block = i[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs]  # Skapar blocken

            greytone_average = np.average(block)
            pixel_amount = int(greytone_average * (block.size / 255))  # får inte vara fler pixlar än 64 per ruta

            quant_error = i - floyd

            for x in range(0, bs):
                for y in range(0, bs):
                    if x < bs:
                        error[x+1, y] = error[x, y+1] + (quant_error*5/16)

                    elif y < bs:
                        error[x, y+1] = error[x, y+1] + quant_error*3/16

                    elif x>1:
                        error[x-1, y+1] = error[x-1, y+1] + quant_error*3/16
                    elif x < bs:
                        error[x+1, y+1] = error[x+1, y+1] + quant_error*1/16







    return all_blocks

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
