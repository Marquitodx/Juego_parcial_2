import pygame, sys, random
from pygame.locals import *
from V_Player import *
from V_Configuraciones import *
from V_Modo import *
from V_Plataformas import *
from V_Items import *
from V_Listas import *   


ANCHO, ALTO, FPS = 1280, 720, 20
VELOCIDAD_FONDO = 3

'''
Guardar pùntajes en una base de datos

Trampas (descuenta vida)

Item para vida

Cronometro

Sonido a los enemigos

Segundo nivel (sin piso solo saltar por plataformas)

Registrar errores en un txt

LAMBDA

ReGex


Ultimo=
GUI
SQL
'''

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

fondo = pygame.image.load(r"bardito\nueva_plataforma-01.png").convert_alpha()
fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))

pygame.display.set_caption("Robot vs todo")

icono = pygame.image.load(r"Recursos\icono.png")
pygame.display.set_icon(icono)

FUENTE = pygame.font.SysFont("Arial", 30)



# ---------------  MUSICA ---------------
#sonidos()


# ---------------  PERSONAJE  ---------------
vardo = Personaje((70,60), 50, 600, 5)


#   ---------------  ENEMIGOS  ---------------
lista_enemigos = lista_de_enemigos

tiempo_creacion_enemigo = pygame.USEREVENT + 1
pygame.time.set_timer(tiempo_creacion_enemigo, 10000)


#   --------------- PLATAFORMAS --------------
plataformas = plataformas_para_jugador

plataformas_enemigos = plataformas_para_enemigos


# ---------------  MONEDAS ---------------
lista_monedas = lista_de_monedas




while True:
    RELOJ.tick(FPS) 
    
    piso_nuevo = random.choice(plataformas_enemigos)
    piso_nuevo = piso_nuevo.rectangulo
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
        elif evento.type == tiempo_creacion_enemigo:
            nuevo_enemigo = Enemigo(piso_nuevo)
            lista_enemigos.append(nuevo_enemigo)
    
    
    x_relativa = x % paisaje.get_rect().width
    PANTALLA.blit(paisaje, (x_relativa - paisaje.get_rect().width, 0))
    if x_relativa < ANCHO:
        PANTALLA.blit(paisaje, (x_relativa, 0))
    x -= VELOCIDAD_FONDO
    PANTALLA.blit(fondo,(0,0))
    
    # -------- Monedas
    for monedas in lista_monedas:
        monedas.actualizar(PANTALLA)
        monedas.detectar_colision(vardo, lista_monedas)
    
    # -------- Enemigos    
    for enemigo in lista_enemigos:
        enemigo.actualizar(PANTALLA, lista_enemigos, plataformas, vardo)
        enemigo.detectar_colision(vardo)

    # -------- Jugador
    vardo.actualizar(PANTALLA, plataformas, lista_enemigos, FUENTE, vardo)
    vardo.detectar_colision(lista_enemigos, ALTO, lista_monedas)
    
    
    
    if get_mode():
        pintar_lineas(PANTALLA, vardo, plataformas, lista_enemigos)
    
    pygame.display.flip()

