import matplotlib.pyplot as plt
import numpy as np
import imageio
import math


def grey_averages(i):
    #i = 255 - i
    bs = 8
    all_blocks = np.zeros(i.shape)

    # dela upp bilden i block

    for p in range(0, math.floor(i.shape[0] / bs)):
        for q in range(0, math.floor(i.shape[1] / bs)):
            block = i[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs]  # skapar 8x8 block

            # mäter blockets gråtonsmedelvärde
            average = np.average(block)
            pixel_amount = int(average * (block.size / 255))  # får inte vara fler pixlar än 64 per ruta

            radius = np.sqrt(pixel_amount / np.pi)

            m = np.zeros((bs, bs))  # skapar en array + gör om till matris

            # går igenom alla pixlar
            for x in range(bs):
                for y in range(bs):
                    if radius <= np.sqrt((x-(bs / 2)) ** 2 + (y - (bs / 2))**2):  # cirkelns ekvation
                        m[x, y] = 255
                    else:
                        m[x,y] = 0

            all_blocks[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs] = m # Sätter ihop alla block

    return all_blocks




sthlm = imageio.imread("katter.jpg")
sthlm_bw = np.mean(sthlm, axis=2)
plt.imshow(sthlm_bw, cmap="gray")
plt.title("Stockholm original")
plt.show()

mean_image = grey_averages(sthlm_bw)
plt.imshow(mean_image.astype('uint8'), cmap="gray")
plt.title("Stockholm block")
plt.show()
