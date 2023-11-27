import pygame, sys
from pygame.locals import *
from V_Player import *
from V_Configuraciones import *
from V_Modo import *
from V_Plataformas import *
from V_Enemigo import *
from V_Items import *   


ANCHO, ALTO, FPS = 1280, 720, 20
VELOCIDAD_FONDO = 3

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

# tiempo_creacion_enemigo = pygame.USEREVENT + 1
# pygame.time.set_timer(tiempo_creacion_enemigo, 5000)



# ---------------  MUSICA ---------------
sonidos()


# ---------------  PERSONAJE  ---------------
vardo = Personaje((70,60), 50, 600, 5)


#   ---------------  ENEMIGOS  ---------------
lista_enemigos = Enemigo.crear_lista()


#   --------------- PLATAFORMAS --------------
plataformas = [piso, piso2, piso3, piso4, piso5, piso6, piso7, piso8, piso9, piso10]

# ---------------  MONEDAS ---------------
lista_monedas = [Monedas(primera_lista_monedas, 250, 635, 20),
                Monedas(primera_lista_monedas, 275, 635, 20),
                Monedas(primera_lista_monedas, 300, 635, 20)]


while True:
    RELOJ.tick(FPS) 
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
        # elif evento.type == tiempo_creacion_enemigo:
        #     nuevo_enemigo = Enemigo(dic_enemigo, limite1, limite2, inicio_x, inicio_y)
        #     lista_enemigos.append(nuevo_enemigo)
    
    
    x_relativa = x % paisaje.get_rect().width
    PANTALLA.blit(paisaje, (x_relativa - paisaje.get_rect().width, 0))
    if x_relativa < ANCHO:
        PANTALLA.blit(paisaje, (x_relativa, 0))
    x -= VELOCIDAD_FONDO
    PANTALLA.blit(fondo,(0,0))
    
    # -------- Monedas
    for monedas in lista_monedas:
        monedas.actualizar(PANTALLA)
    
    # -------- Enemigos    
    for enemigo in lista_enemigos:
        enemigo.actualizar(PANTALLA, lista_enemigos)

    # -------- Jugador
    vardo.actualizar(PANTALLA, plataformas, lista_enemigos)
    vardo.detectar_colision(lista_enemigos, ALTO)
    

    
    

    if get_mode():
        pintar_lineas(PANTALLA, vardo, plataformas, lista_enemigos)
    
    pygame.display.flip()

