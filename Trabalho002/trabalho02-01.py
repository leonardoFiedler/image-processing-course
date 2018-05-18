import cv2 as cv
import numpy as np
# from matplotlib import pyplot as plt

# HELP
#https://en.wikipedia.org/wiki/Histogram_equalization
#http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html

# Plot Histogram
# def plot_histogram(img):
#     # PLOT Histogram
#     hist,bins = np.histogram(img.flatten(),256,[0,256])

#     cdf = hist.cumsum()
#     cdf_normalized = cdf * hist.max()/ cdf.max()

#     plt.plot(cdf_normalized, color = 'b')
#     plt.hist(img.flatten(),256,[0,256], color = 'r')
#     plt.xlim([0,256])
#     plt.legend(('cdf','histogram'), loc = 'upper left')
#     plt.show()
    #End Plot Histogram

# Begin Program

# IMAGE LOADED
IMAGE = "./imgHist.png"

# Passa o parametro 0 por conta do equalizeHist.
img = cv.imread(IMAGE, 0)

# Aplica a convolution na imagem
kernel = (1.0/25.0)*np.ones((5,5))
erosion = cv.erode(img,kernel,iterations = 1)
dst = cv.filter2D(erosion,-1,kernel) # Esta com problemas nao sei porque

# Aplica a equalizacao de histograma
img2 = cv.equalizeHist(dst)
blur = cv.blur(img2,(5,5))
median = cv.medianBlur(blur,5)
cv.imshow('Result', median)
cv.waitKey(0)
cv.destroyAllWindows()