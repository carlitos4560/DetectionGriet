import cv2
import numpy as np
import math

class ImageProces:

    def __init__(self, img):
        self.__img = self.__gaussian(img)

    def canny(self):
        return cv2.Canny(self.__img, 100, 200)

    def laplace(self):
        laplace = cv2.Laplacian(self.__img, cv2.CV_8U, ksize=1)
        kernel = np.ones((1, 1), np.uint8)
        mediaBlur= cv2.medianBlur(laplace, kernel)
        laplace = cv2.erode(mediaBlur, kernel, iterations=3)
        laplace = cv2.morphologyEx(laplace, cv2.MORPH_CLOSE, kernel)
        binario = self.__binario(laplace)
        # binario = cv2.morphologyEx(binario, cv2.MORPH_OPEN, kernel)
        return binario

    def sobelX(self):
        # sobelx = cv2.Sobel(self.__img, cv2.CV_64F, 1, 0, ksize=1)
        sobelx = cv2.Sobel(self.__img, cv2.CV_8U, 1, 0, ksize=1)
        kernel = np.ones((1, 1), np.uint8)
        # sobelx = cv2.bitwise_not(sobelx)
        sobelx = cv2.morphologyEx(sobelx, cv2.MORPH_OPEN, kernel)
        sobelx = cv2.morphologyEx(sobelx, cv2.MORPH_CLOSE, kernel)
        binario = self.__binario(sobelx)
        return binario

    def sobelY(self):
        sobelY = cv2.Sobel(self.__img, cv2.CV_8U, 0, 1, ksize=1)
        kernel = np.ones((3, 3), np.uint8)
        sobely = cv2.morphologyEx(sobelY, cv2.MORPH_OPEN, kernel)
        sobelY = cv2.morphologyEx(sobely, cv2.MORPH_CLOSE, kernel)
        binario = self.__binario(sobelY)
        return binario

    def __binario(self, sobel):
        widht, heihgt = self.__img.shape
        binario = np.zeros((widht, heihgt), dtype=np.uint8)
        for i in range(0, widht):
            for j in range(0, heihgt):
                if sobel[i][j] < 5:
                    binario[i][j] = int(0)
                else:
                    binario[i][j] = int(255)
        return binario

    def __gaussian(self, img):
        #blur funciona bien para todos los casos
        # blur = cv2.blur(img, (5, 5))
        # sigma = 21  # for Gaussian Kernel
        # kernel = 2 * math.ceil(2 * sigma) + 1
        #tambien funciona bien pero con fixma de 3
        blur = cv2.GaussianBlur(img, (5, 5), 3)
        # blur = cv2.subtract(img, blur)
        return blur
