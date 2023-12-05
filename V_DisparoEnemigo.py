import pygame
from V_Disparos import *

class Disparo_enemigo(Disparo):  # Hereda de la clase Disparo
    def __init__(self, x, y, direccion, path):
        # Llama al constructor de la clase base
        super().__init__(x, y, direccion, path)

        # Aquí puedes agregar atributos específicos de Disparo_enemigo si los necesitas
        
    # Puedes sobrescribir métodos de la clase base si es necesario
    def actualizar(self, pantalla, plataformas, jugador):
        self.mover()

        ancho = pantalla.get_width()
        if self.rectangulo.x < 0 or self.rectangulo.x > ancho:
            self.choco = True
        elif self.rectangulo.colliderect(jugador.rectangulos["main"]):
            self.choco = True
        else:
            for plataforma in plataformas:
                if self.rectangulo.colliderect(plataforma.rectangulo):
                    self.choco = True
                    jugador.vida -= 2

        if self.direccion == 'izquierda':
            pantalla.blit(self.imagen_volteada, self.rectangulo)
        elif self.direccion == 'derecha':
            pantalla.blit(self.imagen, self.rectangulo)


    # También puedes agregar nuevos métodos específicos de Disparo_enemigo si los necesitas
