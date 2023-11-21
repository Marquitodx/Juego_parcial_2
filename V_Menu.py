import pygame, sys
from pygame.locals import *
from V_Player import *
from V_Configuraciones import *
from V_Modo import *
from V_Plataformas import *
from V_Enemigo import *
from V_Items import *


ANCHO, ALTO, FPS = 1280, 720, 20
 
#//////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////  INICIALIZACIONES    ////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////

pygame.init()

# ---------------  RELOJ  ---------------
RELOJ = pygame.time.Clock()


# ---------------  PANTALLA Y FONDO  ---------------
PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) # en pixeles

paisaje = pygame.image.load(r"Juego_plataforma-main\Recursos\alien-4852662.jpg").convert()
x = 0

fondo = pygame.image.load(r"Juego_plataforma-main\bardito\plataforma-01.png").convert_alpha()
fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))

pygame.display.set_caption("Robot vs todo")

icono = pygame.image.load(r"Juego_plataforma-main\Recursos\icono.png")
pygame.display.set_icon(icono)



# ---------------  MUSICA ---------------
sonidos()



# ---------------  PERSONAJE  ---------------

vardo = Personaje((70,60), 50, 600, 5)



#   ---------------  ENEMIGOS  ---------------
lista_enemigos = Enemigo.crear_lista()


#   --------------- PLATAFORMAS --------------
plataformas = [piso, piso2, piso3, piso4, piso5, piso6, piso7, piso8, piso9, piso10]


while True:
    RELOJ.tick(FPS) 
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
    

    PANTALLA.blit(paisaje, (x,-100))
    x -= 1

    PANTALLA.blit(fondo,(0,0))
    
    
    
    
# -------- Enemigos    
    for enemigo in lista_enemigos:
        enemigo.actualizar(PANTALLA, lista_enemigos)

# -------- Jugador
    vardo.actualizar(PANTALLA, plataformas, lista_enemigos)
    vardo.detectar_colision(lista_enemigos)        

            
    if get_mode() == True:
        #pygame.draw.rect(PANTALLA,"green", vardo.rectangulo_principal, 2)
        pygame.draw.rect(PANTALLA,"blue", vardo.rectangulos["main"], 2)
        pygame.draw.rect(PANTALLA,"red", vardo.rectangulos["bottom"], 2)
        pygame.draw.rect(PANTALLA,"red", vardo.rectangulos["top"], 2)
        pygame.draw.rect(PANTALLA,"red", vardo.rectangulos["right"], 2)
        pygame.draw.rect(PANTALLA,"red", vardo.rectangulos["left"], 2)

        for plataforma in plataformas:
            pygame.draw.rect(PANTALLA,"magenta",plataforma.rectangulo,3)
            
        for enemigo in lista_enemigos:
            pygame.draw.rect(PANTALLA,"orange", enemigo.rectangulo_principal, 3)
    
    pygame.display.flip()
