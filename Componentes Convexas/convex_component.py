import cv2 as cv
import numpy as np

img = cv.imread('mama.png', cv.IMREAD_COLOR)

grayImg = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
ret, thresh = cv.threshold(grayImg, 10, 255, cv.THRESH_BINARY)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#cv.drawContours(img,contours,-1,(0,255,0),2)

count = 0
contoursDraw = []
i = 0
greater = 0
for x in contours:
    if len(x) > greater:
        greater = i
    i += 1


cv.drawContours(img, contours,greater,(0,255,0),2)
cv.imshow('Final Image', img)
cv.waitKey(0)
cv.destroyAllWindows()