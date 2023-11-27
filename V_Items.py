import pygame
from V_Configuraciones import *

class Monedas:
    def __init__(self, lista_imagenes, pos_x, pos_y, puntos):
        self.lista_imagenes = lista_imagenes
        self.rectangulo = lista_imagenes[0].get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.contador_imagenes = 0
        self.imagen_actual = lista_imagenes[0]

        self.puntos = puntos
        self.tocada = False

    def animar(self, pantalla):
        pantalla.blit(self.imagen_actual, self.rectangulo)

    def actualizar(self, pantalla):
        if not self.tocada:
            self.imagen_actual = self.lista_imagenes[self.contador_imagenes]
            self.animar(pantalla)
            self.contador_imagenes = (self.contador_imagenes + 1) % len(self.lista_imagenes)
    

    
    
    # def animar(self, pantalla):
    #     largo = len(self.lista_imagenes)
    #     if self.contador_imagenes >= largo:
    #         self.contador_imagenes = 0
    #     pantalla.blit(self.imagen_actual[self.contador_imagenes], self.rectangulo)
    #     self.contador_imagenes += 1

    # def actualizar(self, pantalla):
    #     if not self.tocada:
    #         self.animar(pantalla)
    

