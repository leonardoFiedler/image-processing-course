#
# Author: Leonardo Fiedler, Matheus Eduardo Hoeltgebaum
#
#
import cv2 as cv
import imageio
import numpy as np
import math
import os as os
import codecs, json

# Configs

# Folder to save the json file
FOLDER_SAVE_JSON = "file.json"

# Root folder
FOLDER = "./"

# The name of rect we want to divide our image
COUNT_RECT = 7

#DEBUG
IMAGE = FOLDER + "Cenario.gif"

#RUN
# IMAGE = "./Cenario.gif"

# End Configs

# Begin Function to Verify if image is obstacle
def isObstacle(imgName) -> bool:
    img = cv.imread(imgName, cv.IMREAD_COLOR)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    grayscaleImage = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    _, cnts, _ = cv.findContours(grayscaleImage, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    areaTotal = cv.contourArea(cnts[0])
    erodedImage = cv.erode(grayscaleImage, kernel, iterations = 1)
    _, threshold = cv.threshold(erodedImage, 240, 255, cv.THRESH_BINARY_INV)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (11,11))
    morphed = cv.morphologyEx(threshold, cv.MORPH_CLOSE, kernel)
    _, cnts, _ = cv.findContours(morphed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnt = 0
    areaContorno = 0
    area = 0

    if len(cnts) > 0:
        cnt = cnts[0]
        areaContorno = cv.contourArea(cnt)
        area = (100 * areaContorno) / areaTotal

    if (area > 15):
        return True
    else:
        return False

# End Function

# Begin Function to save data in file
def save_file(content):
    # b = content.tolist() # nested lists with same data, indices
    # json.dump(b, codecs.open(FOLDER_SAVE_JSON, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
    np.savetxt(FOLDER_SAVE_JSON, [content], fmt='%s')

#End Function

# Begin PROGRAM

# Remove ROI Images
for file in os.listdir(FOLDER):
    if file.endswith('.png'):
        os.remove(FOLDER + file)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
gif = imageio.mimread(IMAGE)
imgs = [cv.cvtColor(img, cv.COLOR_RGB2BGR) for img in gif]

img = imgs[0]
# Apply dilation
dilatedImage = cv.dilate(img, kernel, iterations = 1)

#Apply Threshold
ret, thresh = cv.threshold(dilatedImage, 125, 255, cv.THRESH_BINARY)

# Erode image
erodedImage = cv.erode(thresh, kernel, iterations = 1)

# Shape of image
width, height = erodedImage.shape[:2]

# Div by the quantity of rects
widthSizeBlock = width / COUNT_RECT
heightSizeBlock = height / COUNT_RECT

# Start - get's the initial position
widthVal = int(math.ceil(widthSizeBlock))
heightVal = int(math.ceil(heightSizeBlock))

# Origin position
originWidth = 0
originHeight = 0

# Matrix result
matRes = np.zeros((7,7), int)
# print(matRes)

# iterate over X and Y
i = 0
x = 0
y = 0
while (heightVal <= height):
    while(widthVal <= width):
        if originWidth == widthVal:
            widthVal += int(widthSizeBlock)
            continue
        # Use this only for debug. This will make the matrix result crash 
        # This enable to show the matrix directly in image
        cv.rectangle(erodedImage,(originWidth, originHeight),(widthVal, heightVal),(0,255,0), 2)
        fname = FOLDER + 'roi_{0}.png'.format(i)
        imROI = cv.imwrite(fname, erodedImage[originHeight:heightVal, originWidth:widthVal])
        
        if isObstacle(fname):
            # Add Obstacles
            matRes[x][y] = 1
        else:
            # Not Obstacle
            matRes[x][y] = 0
        
        originWidth = widthVal
        widthVal += int(widthSizeBlock)
        i += 1
        y += 1

    y = 0
    x += 1
    widthVal = 0
    originWidth = widthVal
    originHeight = heightVal
    heightVal += int(heightSizeBlock)

# Generate JSON file with the matrix
value = ""
for j in range(len(matRes)):
    for i in range(len(matRes[j])):
        value += str(matRes[j][i])
    value += '\n'
print(value)

save_file(value)

cv.imshow('Result', erodedImage)
cv.waitKey(0)
cv.destroyAllWindows()