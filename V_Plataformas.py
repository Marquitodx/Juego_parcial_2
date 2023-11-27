import pygame
from V_Configuraciones import *


class Plataforma:

    def __init__(self, path, ancho, alto, x, y, es_visible, tiene_premio):

        if es_visible:
            self.imagen = pygame.image.load(path)
            self.imagen = pygame.transform.scale(self.imagen, (ancho,alto))
        else:
            self.imagen = pygame.Surface((ancho, alto))
            
        self.rectangulo = self.imagen.get_rect() 
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.premio = tiene_premio
        self.rectangulos = obtener_rectangulos(self.rectangulo)



piso = Plataforma("", 159, 10, 0, 679, False, False)
piso2 = Plataforma("", 300, 10, 242, 679, False, False)
piso3 = Plataforma("", 150, 45, 517, 630, False, False)
piso4 = Plataforma("", 123, 50, 835, 630, False, False)
piso5 = Plataforma("", 117, 20, 449, 474, False, False)
piso6 = Plataforma("", 200, 30, 864, 475, False, False)
piso7 = Plataforma("", 230, 80, 576, 260, False, False)
piso8 = Plataforma("", 220, 40, 135, 372, False, False)
piso9 = Plataforma("", 120, 130, 1152, 387, False, False)
piso10 = Plataforma("", 330, 10, 961, 680, False, False)
