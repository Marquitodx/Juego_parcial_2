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
            jugador.puntaje += 2
            jugador.sonido_collec.play()
            
 

# PORTAL hereda de monedas
class Portal(Monedas):
    def __init__(self, lista_imagenes, x, y):
        super().__init__(lista_imagenes, x, y)
        self.lista_imagenes = lista_imagenes
        self.rectangulo = lista_imagenes[0].get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y - 40
        self.contador_imagenes = 0
        self.imagen_actual = lista_imagenes[0]

        self.portal_tocado = False

    
    def animar(self, pantalla):
        pantalla.blit(self.imagen_actual, self.rectangulo)
    
    def actualizar(self, pantalla, jugador, fuente, 
                   color_letras, color_fondo, superficie_opaca):
        
        self.imagen_actual = self.lista_imagenes[self.contador_imagenes]
        self.animar(pantalla)
        self.contador_imagenes = (self.contador_imagenes + 1) % len(self.lista_imagenes)

        self.detectar_colision(jugador, fuente, color_letras, color_fondo,
                                pantalla, superficie_opaca)
    
    def detectar_colision(self, jugador, fuente, color_letras, color_fondo,
                           pantalla, superficie_opaca):
        if self.rectangulo.colliderect(jugador.rectangulo_principal):
            jugador.puntaje += 100
            you_win(fuente, color_letras, color_fondo, pantalla, superficie_opaca)
            



class Vida:
    def __init__(self, path, ancho):
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen, (30, 30))
        self.imagen.set_colorkey((255,255,255))
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = random.randint(0, ancho - self.rectangulo.width)
        self.rectangulo.y = 0

    def animar(self, pantalla):
        self.rectangulo.y += 3
        pantalla.blit(self.imagen, self.rectangulo)
    
    def detectar_colision(self, jugador, lista_corazones, alto):
        if self.rectangulo.colliderect(jugador.rectangulo_principal):
            lista_corazones.remove(self)
            jugador.vida += 5
            jugador.sonido_vida.play()
        elif self.rectangulo.y > alto:
            lista_corazones.remove(self)
    
    
