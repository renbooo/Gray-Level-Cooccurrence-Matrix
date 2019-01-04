import os, pickle
from matplotlib import pyplot as plt

# img = io.imread('196.jpg')

def extract_glcm(filename_read, filename_save):
	# open file pickle
	with open(filename_read, 'rb') as file_read:
		execute = pickle.load(file_read)

	# convert rgb matrix ke coocurrence
	coocurrence_temp = []
	for idx, img in enumerate(execute):
		print('idx ke-> ',idx)
		coocurrence_temp.append(ccm(img))

	# save file pickle
	with open(filename_save, 'wb') as file_save:
		execute = pickle.dump(coocurrence_temp, file_save)	
	
	# return execute

# def save_image(path):
# 	dataset = []

# 	files = os.listdir(path)
# 	for name in files:
# 		dataset.append(io.imread(path+name))

# 	with open('dataimage.pickle', 'wb') as handle:
# 		pickle.dump(dataset, handle)

extract_glcm('dataimage.pickle', 'coocurrence_matrix')
io.imshow(data[0])
print(data)
# plt.show()
# save_image('/media/kopidingin/3d275aee-c29f-4cdb-bc36-682cf4304465/Tutorial-Python/get-twitter-data/scrape-twitter/Data Batik Madura/citra batik madura/')