import matplotlib.pyplot as plt
import numpy as np
import imageio


def floyd_steinberg(i):
    floyd = np.zeros(i.shape)
    height, width = i.shape

    for x in range(1, height-1):
        for y in range(0, width-1):

            if i[x, y] < 127.5:
                floyd[x, y] = 0
            else:
                floyd[x, y] = 255

            quant_error = i[x, y] - floyd[x, y]
            i[x + 1][y] = i[x+1][y] + quant_error * 7 / 16
            i[x][y + 1] = i[x][y + 1] + quant_error * 5 / 16
            i[x-1][y+1] = i[x-1][y+1] + quant_error * 3 / 16
            i[x+1][y+1] = i[x+1][y+1] + quant_error * 1 / 16

    return floyd


image = imageio.imread("sthlm.jpg")
image_bw = np.mean(image, axis=2)
plt.imshow(image_bw, cmap="gray")
plt.title("Original image")
plt.show()

mean_image = floyd_steinberg(image_bw)
plt.imshow(mean_image.astype('uint8'), cmap="gray")
plt.title("Floyd-Steinberg image")
plt.show()
