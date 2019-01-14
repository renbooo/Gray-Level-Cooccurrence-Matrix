from skimage import io, color, img_as_ubyte

image = io.imread('your_image_file')

gray = color.rgb2gray(image)
convert_pixel = img_as_ubyte(gray)
