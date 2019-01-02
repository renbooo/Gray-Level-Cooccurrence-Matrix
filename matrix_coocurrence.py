from skimage.feature import greycomatrix

matrix_coocurrence = greycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=max_value+1, normed=False, symmetric=False)

