#
# Authors: Flavio Omar Losada e Leonardo Fiedler
#

import cv2 as cv
import numpy as np
import os as os

FOLDER = "./Trabalho003/Amostras"

idxToFilter = [1, 4, 7, 8, 11, 12, 18, 22, 24, 27, 29, 31, 32, 38, 39, 43, 46, 47, 49, 51, 52, 57, 58, 59, 60, 67, 72, 73, 74, 75, 78, 86, 88, 89, 95, 97, 99]

# Itera os arquivos acima mencionados, conforme indice.
x = 1
for file in sorted(os.listdir(FOLDER)):
    if file.endswith('.JPG'):
        if x in idxToFilter:
            print("Current position %i" % x)
            print("Processando o arquivo %s" % file)
            img = cv.imread(FOLDER + "/" + file)
            gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            # Obtem a ROI da imagem
            roi = gray_image[700:1300, 1000:1600]

            # Aplica um Treshold para otimizar o processamento
            _, threshold = cv.threshold(roi, 100, 255, cv.THRESH_BINARY)

            # Aplica o algoritmo, param1 = valor do parametro.
            circles = cv.HoughCircles(threshold,cv.HOUGH_GRADIENT,1,500, param1=30,param2=10,minRadius=120,maxRadius=200)
            circles = np.uint16(np.around(circles))

            # itera os circulos obtidos e desenha na imagem
            for i in circles[0,:]:
                cv.circle(roi,(i[0],i[1]),i[2],(0,255,0),2)
                cv.circle(roi,(i[0],i[1]),2,(0,0,255),3)

            filename = "%s %i" % (file, x)
            cv.imshow(filename, roi)
            cv.waitKey(0)
            cv.destroyAllWindows()
        x+=1