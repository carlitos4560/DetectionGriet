import random
import numpy as np
import cv2

class Individuo:

    def __init__(self, cromosoma):
        self.__cromosoma = cromosoma
        self.__peso = 0
        # self.__fitness = self.__fitness()
        self.__fitness = self.suma()
        self.__mejor  = 0
        # cv2.imshow("maskara", cromosoma)
        # print("fitness", self.__fitness)
        # print("binario FxC", cromosoma.shape)

    def getIndividuo(self):
        return self.__cromosoma

    def mejor(self, media):
        self.__mejor = abs(self.__fitness - media)
        return self.__mejor

    def getBinariLon(self):
        return self.__cromosoma.shape

    def getFitness(self):
        return self.__fitness

    def suma(self):
        fila, columna = self.__cromosoma.shape
        suma = 0
        for i in range(0, fila):
            for j in range(0, columna):
                if self.__cromosoma[i][j] == 255:
                    suma+= (256 - self.__cromosoma[i][j])
            #     print(self.__cromosoma[i][j], " ", end="")
            # print(" ")
        return suma

    def mostarIndividuo(self):
        fila, columna = self.__cromosoma.shape
        for i in range(0, fila):
            for j in range(0, columna):
                if self.__cromosoma[i][j] == 255:
                    print(self.__cromosoma[i][j], " ", end="")
                print(" ")

    def getElemento(self, fila, columna):
        return self.__cromosoma[fila, columna]

    def mutar(self):
        tamanioX, tamanioY = self.__cromosoma.shape
        fila = random.randint(0, tamanioX - 1)
        columna = random.randint(0, tamanioY - 1)
        self.__cromosoma[fila][columna] = 255 - self.__cromosoma[fila][columna]

    # def costeMaximo(self, widht, heihgt):
    #     # print(len(self.__cromosoma[0]))
    #     tamanioX = widht
    #     tamanioY = heihgt
    #     maximoPeso = tamanioX + tamanioY
    #     if self.__peso < maximoPeso:
    #         self.__fitness = self.__fitness - self.__peso
    #     else:
    #         self.__peso = self.__peso - maximoPeso
    #         self.__fitness = self.__fitness - maximoPeso
    #         self.__fitness = self.__fitness - self.__peso * 3
    #     print(str(self.__fitness))
