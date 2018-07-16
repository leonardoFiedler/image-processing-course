
# coding: utf-8

# In[3]:


#Trabalho final
#Grupo: Flávio Losada, Leonardo Fidler, Pâmela Vieira
import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt


# In[4]:


def print_image(img, title = "", size = 8):
    (h,w) = img.shape[:2]
    aspect_ratio = w/h
    plt.figure(figsize = (size * aspect_ratio,size))
    plt.axis("off")
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.show()


# In[5]:


def get_flat_kernel(size):
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(size,size))


# In[8]:


imagem = cv2.imread('C:/Furb/satelite1.png', cv2.IMREAD_COLOR)
imagem_escala_cinza = cv2.imread('C:/Furb/satelite1.png', cv2.IMREAD_COLOR)

#imagem_escala_cinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)

kernel = get_flat_kernel(11)

opening = cv2.morphologyEx(imagem_escala_cinza, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(imagem_escala_cinza, cv2.MORPH_CLOSE, kernel)

top_hat_opening = cv2.subtract(imagem_escala_cinza, opening)
top_hat_closing = cv2.subtract(closing, imagem_escala_cinza)

aprimorada = cv2.add(imagem_escala_cinza,top_hat_opening)
aprimorada = cv2.subtract(aprimorada, top_hat_closing)

#sem_fundo = cv2.subtract(aprimorada, imagem_escala_cinza)
#_, threshold = cv2.threshold(sem_fundo, 50, 255, cv2.THRESH_BINARY)

print_image(imagem)
print_image(aprimorada)

