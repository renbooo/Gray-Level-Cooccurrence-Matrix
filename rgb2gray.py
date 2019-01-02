from skimage import io, color, img_as_ubyte

img = io.imread('')

gray = color.rgb2gray(img)
image = img_as_ubyte(gray)
