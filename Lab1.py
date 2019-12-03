import matplotlib.pyplot as plt
import numpy as np
import imageio
import math


def halftoning(i, bs):
    i = 255 - i
    all_blocks = np.zeros(i.shape)

    for p in range(0, math.floor(i.shape[0] / bs)):
        for q in range(0, math.floor(i.shape[1] / bs)):
            block = i[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs]  # Skapar blocken

            greytone_average = np.average(block)
            pixel_amount = int(greytone_average * (block.size / 255))  # får inte vara fler pixlar än 64 per ruta

            radius = np.sqrt(pixel_amount / np.pi)
            m = np.zeros((bs, bs))  # Skapar en matris

            for x in range(bs):  # Går igenom varje pixel och sätter värden till vår matris
                for y in range(bs):
                    if radius <= np.sqrt((x-(bs / 2)) ** 2 + (y - (bs / 2))**2):  # cirkelns ekvation
                        m[x, y] = 255
                    else:
                        m[x, y] = 0

            all_blocks[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs] = m  # Sätter ihop alla block

    return all_blocks


image = imageio.imread("sthlm.jpg")
image_bw = np.mean(image, axis=2)
plt.imshow(image_bw, cmap="gray")
plt.title("Stockholm original")
plt.show()

mean_image = halftoning(image_bw, 4)
plt.imshow(mean_image.astype('uint8'), cmap="gray")
plt.title("Stockholm block")
plt.show()
