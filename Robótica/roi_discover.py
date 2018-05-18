import cv2 as cv
import imageio
import numpy as np
import math
import os as os


IMAGE = "roi_48.png"

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
img = cv.imread(IMAGE, cv.IMREAD_COLOR)
grayscaleImage = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

_, cnts, _ = cv.findContours(grayscaleImage, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
areaTotal = cv.contourArea(cnts[0])
# print("Area Total: ", areaTotal)

erodedImage = cv.erode(grayscaleImage, kernel, iterations = 1)

ret, threshold = cv.threshold(erodedImage, 240, 255, cv.THRESH_BINARY_INV)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (11,11))
morphed = cv.morphologyEx(threshold, cv.MORPH_CLOSE, kernel)
_, cnts, _ = cv.findContours(morphed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnt = 0
areaContorno = 0
area = 0

if len(cnts) > 0:
    cnt = cnts[0]
    areaContorno = cv.contourArea(cnt)
    # print("Area Contorno: ", areaContorno)
    area = (100 * areaContorno) / areaTotal
    # print("Area ", area)

if (area > 15):
    print("Obstaculo")
else:
    print("Nao eh obstaculo")

# cv.imshow('Result', erodedImage)
# cv.waitKey(0)
# cv.destroyAllWindows()