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

paisaje = pygame.image.load(r"Recursos\paisaje-fondo-01.jpg").convert()
x = 0

fondo = pygame.image.load(r"bardito\plataforma-01.png").convert_alpha()
fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))

pygame.display.set_caption("Robot vs todo")

icono = pygame.image.load(r"Recursos\icono.png")
pygame.display.set_icon(icono)

tiempo_disparo = pygame.USEREVENT
pygame.time.set_timer(tiempo_disparo,1000)





# ---------------  MUSICA ---------------
# sonidos()



# ---------------  PERSONAJE  ---------------

vardo = Personaje((70,60), 50, 600, 5)



#   ---------------  ENEMIGOS  ---------------
lista_enemigos = Enemigo.crear_lista()


#   --------------- PLATAFORMAS --------------
plataformas = [piso, piso2, piso3, piso4, piso5, piso6, piso7, piso8, piso9, piso10]


while True:
    RELOJ.tick(FPS) 
    
    x_relativa = x % paisaje.get_rect().width
    PANTALLA.blit(paisaje, (x_relativa - paisaje.get_rect().width, 0))
    if x_relativa < ANCHO:
        PANTALLA.blit(paisaje, (x_relativa, 0))
    x -= 1
    PANTALLA.blit(fondo,(0,0))
    
    
# -------- Enemigos    
    for enemigo in lista_enemigos:
        enemigo.actualizar(PANTALLA, lista_enemigos)

# -------- Jugador
    vardo.actualizar(tiempo_disparo, PANTALLA,plataformas, lista_enemigos)
    vardo.detectar_colision(lista_enemigos, ALTO)        

            
    if get_mode() == True:
        pintar_lineas(PANTALLA, vardo, plataformas, lista_enemigos)
    
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)

    
    pygame.display.flip()

