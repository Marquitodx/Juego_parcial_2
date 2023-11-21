import pygame
from V_Configuraciones import *

class Monedas:
    def __init__(self, animaciones, pos_x, pos_y, puntos):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, 50, 50)
        self.rectangulo = animaciones[0].get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.contador_pasos = 0
        self.animacion_actual = animaciones[0]

        self.puntos = puntos
        self.tocada = False

    
    def animar(self, pantalla):
        largo = len(self.animaciones)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
        self.contador_pasos += 1


    def actualizar(self, pantalla):
        if not self.tocada:
            self.animar(pantalla)
    


    
