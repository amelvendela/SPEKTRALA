import matplotlib.pyplot as plt
import numpy as np
import imageio
import math


def greys(i, bs):
    i = 255 - i
    full_i = np.zeros(i.shape)
    for p in range(0, math.floor(i.shape[0] / bs)):
        for q in range(0, math.floor(i.shape[1] / bs)):
            block = i[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs]  # Skapar blocken

            greytone_average = np.average(block)
            pixel_amount = int(greytone_average * (block.size / 255))  # får inte vara fler pixlar än 64 per ruta

            m = np.zeros(bs*bs)
            for h in range(pixel_amount):  # Går igenom varje pixel och sätter värden till vår matris
                m[h] = 255

            m = m.reshape((bs, bs))
            full_i[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs] = m  # Sätter ihop alla block

    return full_i


def floyd_steinberg(i):
    floyd = np.zeros(i.shape)
    height, width = i.shape
    pixel = greys(i, 8)
    factor = 1
    for x in range(1, width-1):
        for y in range(0, height-1):
            old_pixel = pixel[x][y]
            new_pixel = np.round(factor * old_pixel / 255) * (255 / factor)
            pixel[x][y] = new_pixel
            quant_error = old_pixel - new_pixel

            floyd[x + 1][y] = floyd[x+1][y] + quant_error * 7 / 16
            floyd[x-1][y+1] = floyd[x-1][y+1] + quant_error * 3 / 16
            floyd[x][y+1] = floyd[x][y+1] + quant_error * 5 / 16
            floyd[x+1][y+1] = floyd[x+1][y+1] + quant_error * 1 / 16


    return floyd


'''quant_error = i - all_blocks

            for p in range(0, math.floor(i.shape[0] / bs)):
                for q in range(0, math.floor(i.shape[1] / bs)):
                    # Extract an 8x8 sub matrix 'Isub' from the original image
                    Isub = i[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs]

                    # Put matrix operation under this line
                    new_isub = Isub / all_blocks
                    new_isub = np.trunc(new_isub)
                    P[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs] = new_isub
                    P[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs] *= w_matrix

    return all_blocks'''


image = imageio.imread("sthlm.jpg")
image_bw = np.mean(image, axis=2)
plt.imshow(image_bw, cmap="gray")
plt.title("Original image")
plt.show()

mean_image = floyd_steinberg(image_bw)
plt.imshow(mean_image.astype('uint8'), cmap="gray")
plt.title("Halftoned image")
plt.show()
