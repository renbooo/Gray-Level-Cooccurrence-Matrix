import numpy as np

bins4 = np.array([0, 64, 128, 192, 255]) #4-bit
bins8 = np.array([0, 32, 64, 96, 128, 160, 192, 224, 255]) #8-bit
bins16 = np.array([0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 255]) #16-bit

inds = np.digitize(image, bins)