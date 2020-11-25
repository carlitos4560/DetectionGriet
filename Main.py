import cv2
import numpy as np
from readImage import ReadImage
from imageProces import ImageProces
from algoritmoGenetico.Poblacion import Poblacion
from algoritmoGenetico.AlgoritmoGenetico import AlgoritmoGenetico
from algoritmoGenetico.Individuo import Individuo
class Main:
    def __init__(self):
        pass

    def initial(self):
        return str("comenzando")

    def read(self):
        return "grieta1.jpg"
        # return "grietafalsa.jpg"

if __name__ == "__main__":
    main = Main()
    #Ruta de la imagen
    print(main.initial())
    route = main.read()
    readImage = ReadImage(route)
    # Lectura de la imagen
    print("Ruta de la imagen", readImage.getRoute())
    imgs = readImage.read()
    widht = imgs[1]
    heihgt = imgs[2]
    cv2.imshow('leer Imagen', imgs[0])
    imageProces = ImageProces(imgs[0])
    # print("nuevo tamanio", widht, heihgt)
    """
    ||||||||||||||||||||||||
    |   POBLACION INICIAL  |
    ||||||||||||||||||||||||
    """

    #  | CREACION DEL ALGORITMO GENETICO

    poblacionInicial = Poblacion()
    print(str(poblacionInicial))
    """
    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    | IMAGENES BINARIAS TOMANDO EN CUENTA TECNICAS DE VISION POR COMPUTADORA  |
    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    """

    # FUNCION LA PLACE
    laplace = imageProces.laplace()
    individuo = Individuo(laplace)
    # print("laplace tamanio", individuo.shape)
    poblacionInicial.addIndividuo(individuo)
    #FUNCION SOBEL EN X
    sobelx = imageProces.sobelX()
    individuo = Individuo(sobelx)
    poblacionInicial.addIndividuo(individuo)
    # FUNCION SOBEL EN Y
    sobely = imageProces.sobelY()
    individuo = Individuo(sobely)
    poblacionInicial.addIndividuo(individuo)
    #FUNCION CANNY
    canny = imageProces.canny()
    individuo = Individuo(canny)
    poblacionInicial.addIndividuo(individuo)
    """
    |||||||||||||||||||||||||||||||
    | MOSTRAR LA POBLACION INCIAL |
    |||||||||||||||||||||||||||||||
    """
    # poblacionInicial.mostrarPoblacion()

    """
    ||||||||||||||||||||||||||
    |   ALGORITMO GENETICO   |
    ||||||||||||||||||||||||||
    """

    algoritmoGenetico = AlgoritmoGenetico(poblacionInicial)
    """
    *******************************************
    | Generar una cantidad de generaciones    |
    *******************************************
    """
    generaciones = 10
    mejorIndividuo = algoritmoGenetico.generaciones(generaciones)
    # print(mejorIndividuo[0])
    cv2.imshow("mejor Individuo", poblacionInicial.seleccion(mejorIndividuo).getIndividuo())
    poblacionInicial.mostrarPoblacion()
    print("elitista ", mejorIndividuo)
    # print("mejor hijo", mejorHijo)
    # imgs = imageProces.canny()

    # sobel = cv2.addWeighted(sobelx, sobely)
    # print("poblacion", poblacionInicial) # cantidad de poblacion inicial relacionada
    # cv2.imshow('sobelx', sobelx)
    # cv2.imshow('soberly', sobely)
    # cv2.imshow('laPlace', laplace)
    # cv2.imshow('canny', canny)
    # cv2.imshow('mejorHijo', mejorHijo)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
