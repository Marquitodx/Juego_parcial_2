import pygame, sys
from pygame.locals import *

pygame.init()

ANCHO, ALTO = 800, 600
FPS = 30
PANTALLA = pygame.display.set_mode((ANCHO,ALTO))
RELOJ = pygame.time.Clock()
NEGRO = (0,0,0)

fondo = pygame.image.load(r"bardito\nueva_plataforma-01.png").convert_alpha()
fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))


point = 0


while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    point += 1
    mensaje = fuente.render(f"Puntaje: {point}", True, NEGRO)

    PANTALLA.blit(fondo, (0,0))
    PANTALLA.blit(mensaje,(ANCHO // 2, 20))

    pygame.display.flip()