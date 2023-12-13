import pygame, sys
from Nivel1 import Nivel_1
from Nivel2 import Nivel_2
from GUI_form_prueba import FormPrueba


pygame.init()

ANCHO, ALTO = 1280, 720
pantalla = pygame.display.set_mode((ANCHO, ALTO))

RELOJ = pygame.time.Clock()
FPS = 30


form_prueba = FormPrueba(pantalla, 100, 100, 800, 300, "black", "red", 5, True)


while True:
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    form_prueba.update(lista_eventos)



    pygame.display.flip()