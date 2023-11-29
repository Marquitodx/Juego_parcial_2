import pygame
from V_Configuraciones import *
from V_Plataformas import *

class Monedas:
    def __init__(self, lista_imagenes, x, y):
        self.lista_imagenes = lista_imagenes
        self.rectangulo = lista_imagenes[0].get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y - 40
        self.contador_imagenes = 0
        self.imagen_actual = lista_imagenes[0]
        
        self.puntos = 20
        self.tocada = False

    def animar(self, pantalla):
        pantalla.blit(self.imagen_actual, self.rectangulo)

    def actualizar(self, pantalla):
        if not self.tocada:
            self.imagen_actual = self.lista_imagenes[self.contador_imagenes]
            self.animar(pantalla)
            self.contador_imagenes = (self.contador_imagenes + 1) % len(self.lista_imagenes)
    
    def detectar_colision(self, jugador, lista_monedas):
        if self.rectangulo.colliderect(jugador.rectangulo_principal):
            lista_monedas.remove(self)
            jugador.puntaje += 5
        
        
        
    # def crear_monedas(self, plataforma, lista_imagenes):
    #     tira_monedas = []
    #     largo = plataforma.width
    #     i = 0
    #     y = plataforma.y
    #     x = plataforma.x
    #     if i <= largo:
    #         moneda = Monedas(lista_imagenes, x, y, 20)
    #         tira_monedas.append(moneda)
    #         x = plataforma.x + 20
    #         i += 20
