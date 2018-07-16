#Authors: Flavio e Leonardo
import cv2 as cv
import numpy as np
import os as os
import statistics


class Ponto:
    inicio = 0
    fim = 0
    quantidade = 0


BASE_FOLDER = "./Plate Recognizing"
FOLDER = BASE_FOLDER + "/Placas"
FOLDER_LETTERS = BASE_FOLDER + "/Letras/"

kernel = (5,5)
# kernel_int = np.ones((5,5),np.float32)/25
for file in sorted(os.listdir(FOLDER)):
    if file.endswith('.jpg') or file.endswith('.jpeg'):
        img = cv.imread(FOLDER + "/" + file)
        #img = cv.imread(FOLDER + "/indice.jpg")
        gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray_image, kernel, 0)
        edges = cv.Canny(blur,150,180)
        iCountWhite = 0
        linhas = []
        height, width = edges.shape
        image = np.zeros(edges.shape, dtype="uint8")
        ponto = Ponto()
        ponto.inicio = 0
        for i in range(0, height):
            for j in range(0, width):
                if (edges[i][j] > 0):
                    iCountWhite += 1
            
            if iCountWhite > 5 and iCountWhite < 130:
                for j in range(0, height):
                    image[i][j] = 255
                
                if i == ponto.fim or (i - 1) == ponto.fim:
                    ponto.fim = i
                    ponto.quantidade += 1
                else:
                    if ponto.quantidade > 5:
                        linhas.append(ponto)
                    ponto = Ponto()
                    ponto.inicio = i
                    ponto.fim = i

            iCountWhite = 0

        linhaMax = Ponto()
        for linha in linhas:
            if (linha.quantidade > linhaMax.quantidade):
                linhaMax = linha

        print("Linha inicio = %i, Fim = %i, Quantidade = %i" %(linhaMax.inicio, linhaMax.fim, linha.quantidade))
        #Adicionado um ajustado por conta de algumas imagens cortarem em uma pequena regiao
        if (linhaMax.inicio >= 20):
            linhaMax.inicio -= 20
        else:
            linhaMax.inicio = 0
        
        if (linhaMax.fim + 20 < height):
            linhaMax.fim += 20
        else:
            linhaMax.fim = height
        
        roi = edges[linhaMax.inicio:linhaMax.fim, 0:width]
        im2, contours, hierarchy = cv.findContours(roi,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        # cv.drawContours(roi, contours, -1, (255,0,0), 3)
        letters = []
        print("width %i, height = %i" % (width, height))

        arrMediaW = []
        arrMediaH = []
        for contour in contours:
            x,y,w,h = cv.boundingRect(contour)
            arrMediaW.append(w)
            arrMediaH.append(h)

        mediaW = statistics.mean(arrMediaW)
        mediaH = statistics.mean(arrMediaH)
        #print("Media w %i, Media h %i" %(mediaW, mediaH))
        
        count = 0
        arrCount = []
        for contour in contours:
            x,y,w,h = cv.boundingRect(contour)
            height, width = roi.shape
            min_x, min_y = width, height
            max_x = max_y = 0
            min_x, max_x = min(x, min_x), max(x+w, max_x)
            min_y, max_y = min(y, min_y), max(y+h, max_y)
            print("x = %i, y = %i, w = %i, h = %i" %(min_x, min_y, w, h))
            if (w >= mediaW and w < (5 * mediaW)) and (h >= mediaH and h < (5 * mediaH)):
                cv.rectangle(roi, (x,y), (x+w,y+h), (255, 0, 0), 0)
                letters.append(roi[min_y:max_y, min_x:max_x])
                count += 1
                arrCount.append({'w': w, 'h': h})
        
        print("Count %i" % (count))
        
        i = 0
        for letter in letters:
            folder_path = FOLDER_LETTERS + str(i) + "_" + file
            cv.imwrite(folder_path, letter )
            i += 1
            # cv.imshow("Imagem", letter)
            # cv.waitKey(0)
            # cv.destroyAllWindows()