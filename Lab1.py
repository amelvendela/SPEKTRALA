import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.signal
import imageio
import math




def block(i):
    bs = 8
    c = np.zeros(i.shape)
    for p in range(0, math.floor(i.shape[0] / bs)):
        for q in range(0, math.floor(i.shape[1] / bs)):
            isub = i[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs]  # Man skapar 8x8 block


            # Skapa prick

            c[p * bs: (p + 1) * bs, q * bs: (q + 1) * bs] = average  # Sätter ihop alla block
    return c


stockholm = imageio.imread("sthlm.jpg")
bw_stockholm = np.mean(stockholm, axis=2)
plt.imshow(bw_stockholm, cmap="gray")
plt.title("Stockholm original")
plt.show()

mean_image = block(stockholm)
plt.imshow(mean_image.astype('uint8'), cmap="gray")
plt.title("Stockholm block")
plt.show()
