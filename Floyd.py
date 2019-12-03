import matplotlib.pyplot as plt
import numpy as np
import imageio
import math


def grey_averages(i):
    bs = 8
    all_blocks = np.zeros(i.shape)
    for p in range(0, math.floor(i.shape[0] / bs)):
        for q in range(0, math.floor(i.shape[1] / bs)):
            block = i[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs]  # Man skapar 8x8 block
            greyscale_average = np.average(block)
            pixel_amount = int(greyscale_average * (block.size / 255))

            m = np.zeros(bs*bs)
            for h in range(pixel_amount):
                m[h] = 255
            m = m.reshape((bs, bs))
            all_blocks[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs] = m  # Sätter ihop alla block
    return all_blocks


size_circle = 4


sthlm = imageio.imread("sthlm.jpg")
sthlm_bw = np.mean(sthlm, axis=2)
plt.imshow(sthlm_bw, cmap="gray")
plt.title("Stockholm original")
plt.show()

mean_image = grey_averages(sthlm_bw)
plt.imshow(mean_image.astype('uint8'), cmap="gray")
plt.title("Stockholm block")
plt.show()
