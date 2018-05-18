import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg', cv.IMREAD_COLOR)
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('image', imgGray)
cv.waitKey(0)
cv.destroyAllWindows()

#Para abrir a VM - OpenCVVM
#work on opencvvm

#deactivate