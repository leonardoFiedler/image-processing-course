import cv2 as cv
import numpy as np

#Circularidade
#Quantidade
#Área do Núcleo

# Algoritmo, passo a passo:
# Grayscale
# Dilatacao
# TOP HAT
# Threshold
# Contornos
# Contar quantos contornos
# Verificar quantidade de contornos
# Se contornos == 1
# Verificar tamanho do contorno interno em relacao ao contorno externo
# Se contorno > 1
# Neutrofilo 

IMAGE = "./dataset_neutrofilos/neutrofilo01.png"
# IMAGE = "./linfocito00.png"
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))

originalImage = cv.imread(IMAGE, cv.IMREAD_COLOR)
grayscaleImage = cv.cvtColor(originalImage, cv.COLOR_RGB2GRAY)

im2, contours, hierarchy = cv.findContours(grayscaleImage, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
ret, thresh = cv.threshold(originalImage, 125, 255, cv.THRESH_BINARY)

#Dilatação imagem original
dilatedImage = cv.dilate(grayscaleImage,kernel, iterations = 1)

#Erosão imagem original 
erodedImage = cv.erode(dilatedImage, kernel, iterations = 1)

#Thresholding
ret, threshold = cv.threshold(erodedImage, 125, 255, cv.THRESH_BINARY)

cv.drawContours(threshold, contours, 0, (255,255,255), 1)

contornoCelula = contours[0]

im2, contours, hierarchy = cv.findContours(threshold, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(originalImage, contours, 0, (0,255,0))

contornosNucleo = contours

neutrofilo: bool = len(contornosNucleo) > 2
areaCelula = cv.contourArea(contornoCelula)

if neutrofilo:
    print("Tipo célula: Neutrófilo\n")
    for contorno in contornosNucleo:
        if contorno == contornoCelula:
            continue
        areaNucleo = cv.contourArea(contorno)
        percent = areaNucleo * 100 / areaCelula
        print("Área do núcleo em relação à celula: %s", percent)
        
else:
    areaNucleo = cv.contourArea(contornosNucleo[1])    

    percent = areaNucleo * 100 / areaCelula        
    neutrofilo = percent < 85
    print("Tipo célula: %s \nÁrea do núcleo em relação à celula: %s" % ("Neutrófilo" if neutrofilo else "Linfócito", percent))