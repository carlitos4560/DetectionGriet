from algoritmoGenetico.CruzaIndividuo import CruzaIndividuo
from algoritmoGenetico.SeleccionIndividuo import SeleccionIndividuo
import cv2

class AlgoritmoGenetico:
    def __init__(self, poblacion):
        self.__poblacion = poblacion

    def generaciones(self, generaciones):
        elitista = None
        mejorHijo = None
        while(generaciones > 0):
            """
            ----------------------------------------
            |      SELECCIONADOS DE INDIVIDUOS     |
            ----------------------------------------
            """
            seleccionDeIndividuos = SeleccionIndividuo(self.__poblacion)
            seleccion1, seleccion2 = seleccionDeIndividuos.torneo()
            # print(seleccionDeIndividuos)
            """
            ----------------------------------------
            | MOSTRAR LOS INDIVIDUOS SELECCIONADOS |
            ----------------------------------------
            """
            # seleccionDeIndividuos.mostrarSeleccion1()
            # seleccionDeIndividuos.mostrarSeleccion2()
            """
            | Cruza de individuos
            """
            cruza = CruzaIndividuo(seleccion1, seleccion2, self.__poblacion)
            mejoresHijos = cruza.cruza1puno()
            # cv2.imshow("mejorHijo1", mejoresHijos[0].getIndividuo())
            # cv2.imshow("mejorHijo2", mejoresHijos[1].getIndividuo())
            """
            |Agregar los hijos a la poblacion
            """
            self.agregarPoblacion(mejoresHijos)
            """
            | Elegir un individuo aleatorio para mutar
            """
            self.__poblacion.mutar()
            # mejorHijo.mostarIndividuo()
            # print(mejorHijo)
            """
            ______________________
            | Individuo Elitista |
            ______________________
            """
            elitista = self.__poblacion.elitista()
            # elitista.append(self.__poblacion.elitista())
            generaciones = generaciones - 1
        return elitista

    def agregarPoblacion(self, mejores):
        longitud = len(mejores)
        for i in range(longitud):
            self.__poblacion.addIndividuo(mejores[i])
