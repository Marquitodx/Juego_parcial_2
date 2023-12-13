import pygame
from V_Disparos import *

class Disparo_enemigo(Disparo):  # esta la heredo de la clase disparo
    def __init__(self, x, y, direccion, path):

        super().__init__(x, y, direccion, path)
        
    # aca modifico un poco el comportamiento del proyectil    
    def actualizar(self, pantalla, plataformas, jugador):
        self.mover()

        ancho = pantalla.get_width()
        if self.rectangulo.x < 0 or self.rectangulo.x > ancho:
            self.choco = True
        elif self.rectangulo.colliderect(jugador.rectangulos["main"]):
            jugador.vida -= 2
            self.choco = True
        else:
            for plataforma in plataformas:
                if self.rectangulo.colliderect(plataforma.rectangulo):
                    self.choco = True

        if self.direccion == 'izquierda':
            pantalla.blit(self.imagen_volteada, self.rectangulo)
        elif self.direccion == 'derecha':
            pantalla.blit(self.imagen, self.rectangulo)
