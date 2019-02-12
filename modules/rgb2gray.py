from skimage import io, color, img_as_ubyte

image = io.imread('image_sample.jpg')

gray = color.rgb2gray(image)

# Convert an image to 8-bit unsigned integer format.
ubyte = img_as_ubyte(gray)

print(ubyte)
