import pygame, random
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


class Vida:
    def __init__(self, path, ancho):
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen, (80, 80))
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = random.randint(0, ancho - self.rectangulo.width)
        self.rectangulo.y = 0

    def animar(self, pantalla):
        self.rectangulo.y += 5
        pantalla.blit(self.imagen, self.rectangulo)
    
    def detectar_colision(self, jugador, lista_corazones, alto):
        if self.rectangulo.colliderect(jugador.rectangulo_principal):
            lista_corazones.remove(self)
            jugador.vida += 5
        elif self.rectangulo.y > alto:
            lista_corazones.remove(self)
    
    
