import cv2 
import numpy as np

class ReadImage:

    def __init__(self, routeImage):
        self.__routeImage = routeImage
    
    def read(self):
        img = cv2.imread(self.__routeImage, 0)
        fila, columna = img.shape
        # print(str(img.shape))
        # print('fila', fila, 'columna', columna)
        fila = int(fila / 2)
        columna = int(columna / 2)
        img = cv2.resize(img, (fila, columna))
        img = cv2.resize(img, (200, 200))
        print("tamanio FxC", fila, columna)
        tupla = (img, fila, columna)
        return tupla
    
    def getRoute(self):
        return str(self.__routeImage)