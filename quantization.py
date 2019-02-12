import numpy as np
from skimage import io

image = io.imread('your_image_file')

bins4 = np.array([0, 64, 128, 192, 255]) #4-bit
bins8 = np.array([0, 32, 64, 96, 128, 160, 192, 224, 255]) #8-bit
bins16 = np.array([0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 255]) #16-bit
bins32 = np.array([0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160,
		168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 255]) #32-bit

inds = np.digitize(image, bins)
print(inds)