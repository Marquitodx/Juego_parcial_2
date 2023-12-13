import pygame
from V_Configuraciones import *


class Plataforma:
    def __init__(self, path, ancho, alto, x, y, es_visible):

        if es_visible:
            self.imagen = pygame.image.load(path)
            self.imagen = pygame.transform.scale(self.imagen, (ancho,alto))
        else:
            self.imagen = pygame.Surface((ancho, alto))
            
        self.rectangulo = self.imagen.get_rect() 
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.rectangulos = obtener_rectangulos(self.rectangulo)
