import random
import cv2
import numpy as np
class SeleccionIndividuo:

    def __init__(self, poblacion):
        self.__poblacion = poblacion
        self.__seleccionados1 = []
        self.__seleccionados2 = []

    def ruleta(self):
        posicion = 0
        probabilidadSeleccion = self.__poblacion.probabilidadSeleccion(posicion)
        print(probabilidadSeleccion)

    def torneo(self):
        longitudPoblacion = self.__poblacion.longitudPoblacion()
        limite = int(longitudPoblacion / 2)
        for i in range(0, limite):
            aleatorio = random.randint(0, longitudPoblacion - 1)
            self.__seleccionados1.append(self.__poblacion.seleccion(aleatorio))
            aleatorio = random.randint(0, longitudPoblacion - 1)
            self.__seleccionados2.append(self.__poblacion.seleccion(aleatorio))
        return self.__seleccionados1, self.__seleccionados2

    def mostrarSeleccion1(self):
        for i in range(len(self.__seleccionados1)):
            nombre = "Seleccion 1 " + str(i)
            img = self.__seleccionados1[i].getIndividuo()
            cv2.imshow(nombre, img)

    def mostrarSeleccion2(self):
        for i in range(len(self.__seleccionados2)):
            nombre = "Seleccion 2 " + str(i)
            img = self.__seleccionados2[i].getIndividuo()
            cv2.imshow(nombre, img)

    def __str__(self):
        return str(len(self.__seleccionados1)) + "\t" + str(len(self.__seleccionados2))
