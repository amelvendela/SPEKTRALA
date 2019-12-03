import matplotlib.pyplot as plt
import numpy as np
import imageio
import math


def block(i):
    bs = 8
    c = np.zeros(i.shape)
    for p in range(0, math.floor(i.shape[0] / bs)):
        for q in range(0, math.floor(i.shape[1] / bs)):
            isub = i[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs]  # Man skapar 8x8 block
            average = np.average(isub)
            pixel_amount = int(average * (isub.size / 255))
            circle = 
            m = np.zeros(bs*bs)
            for h in range(pixel_amount):
                m[h] = 255
            m = m.reshape((bs, bs))
            c[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs] = m  # Sätter ihop alla block

    return c


uggla = imageio.imread("uggla2.tif")
plt.imshow(uggla, cmap="gray")
plt.title("Ugglis original")
plt.show()

mean_image = block(uggla)
plt.imshow(mean_image.astype('uint8'), cmap="gray")
plt.title("Ugglis block")
plt.show()
