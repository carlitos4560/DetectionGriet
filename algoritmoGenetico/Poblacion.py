from random import shuffle
import cv2
import random
class Poblacion:

    def __init__(self):
        self.__poblacion = []
        self.__totalFitness = self.__totalFitnes()

    def addIndividuo(self, individuo):
        self.__poblacion.append(individuo)

    def __str__(self):
        return str("poblacion") + str(len(self.__poblacion))

    def mutar(self):
        longitud = len(self.__poblacion) - 1
        aleatorio = random.randint(0, longitud)
        self.__poblacion[aleatorio].mutar()

    def __totalFitnes(self):
        totalFitness = 0
        for i in range(len(self.__poblacion)):
            totalFitness += self.__poblacion[i].getFitness()
        return totalFitness

    def probabilidadSeleccion(self, posicion):
        return self.__poblacion[posicion].getFitness() / self.__totalFitness

    def seleccion(self, posicion):
        return self.__poblacion[posicion]

    def longitudPoblacion(self):
        return len(self.__poblacion) - 1

    def mostrarPoblacion(self):
        for i in range(len(self.__poblacion)):
            nombre = "individuo " + str(i)
            # cv2.imshow(nombre, self.__poblacion[i].getIndividuo())
            print("Individuo \t fitness")
            print("\t"+str(i) + "\t" + "\t" + str(self.__poblacion[i].getFitness()))
        print("cantidad de poblacion", len(self.__poblacion))

    def mostarElitista(self, posicion):
        cv2.imshow("elitista", self.__poblacion[posicion].getIndividuo())

    def elitista(self):
        longitud = len(self.__poblacion)
        elitista = 0
        for i in range(1, longitud):
            if self.__poblacion[elitista].getFitness() < self.__poblacion[i].getFitness():
                elitista = i
        return elitista

    # def elitista(self):
    #     longitud = len(self.__poblacion)
    #     totalFitness = self.__totalFitnes()
    #     media = int(totalFitness / 2)
    #     elitista = 0
    #     posicionElitista = 0;
    #     for i in range(longitud):
    #         mejorIndividuo = self.__poblacion[i].mejor(media)
    #     elitista = self.__poblacion[i].mejor(media)
    #
    #     for j in range(1, longitud):
    #         if elitista < mejorIndividuo:
    #             elitista = mejorIndividuo
    #             posicionElitista = i
    #     return posicionElitista
