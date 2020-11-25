import random
import cv2
import numpy as np

from algoritmoGenetico.Individuo import Individuo


class CruzaIndividuo:

    def __init__(self, seleccion1, seleccion2, poblacion):
        self.__seleccion1 = seleccion1
        self.__seleccion2 = seleccion2
        self.__poblacion = poblacion

    def cruza1puno(self):
        longitud = len(self.__seleccion1)
        mejores = []
        for i in range(0, longitud):
            mejores.append(self.__cruza1punto(i))
        return mejores

    def __cruza1punto(self, posicion):
        fila, columna = self.__seleccion1[posicion].getBinariLon()
        corteAleatorioFila = int(random.randint(0, fila))
        corteAleatoriocolumna = int(random.randint(0, columna))
        hijo1 = np.zeros((fila, columna), dtype=np.uint8)
        hijo2 = np.zeros((fila, columna), dtype=np.uint8)
        padre = self.__seleccion1[posicion]
        madre = self.__seleccion2[posicion]
        # cv2.imshow('padre', padre.getIndividuo())
        # cv2.imshow('madre', madre.getIndividuo())
        for i in range(0, fila):
            for j in range(0, columna):
                if i >= corteAleatorioFila and j >= corteAleatoriocolumna:
                    hijo1[i][j] = int(madre.getElemento(i, j))
                    hijo2[i][j] = int(padre.getElemento(i, j))
                else:
                    hijo1[i][j] = int(padre.getElemento(i, j))
                    hijo2[i][j] = int(madre.getElemento(i, j))
        individuoHijo1 = Individuo(hijo1)
        individuoHijo2 = Individuo(hijo2)
        # cv2.imshow("Hijo 1", individuoHijo1.getIndividuo())
        # cv2.imshow("Hijo 2", individuoHijo2.getIndividuo())
        fitnessHijo1 = individuoHijo1.getFitness()
        fitnessHijo2 = individuoHijo2.getFitness()
        resultado = individuoHijo2
        if fitnessHijo1 > fitnessHijo2:
            resultado = individuoHijo1
        return resultado

            #     print(self.__cromosoma[i][j], " ", end="")
            # print(" ")
        # limite = len(self.__seleccion1[0])

        # aleatorio = random.randint(0, limite - 1)
        # widht, heidht = self.__seleccion1[0].shape
        # print(widht, "\t", heidht)

    def elitista(self):
        pass