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
Guardar puntajes en una base de datos
Trabajar los rectangulos para colisiones
Acomodar el contador de vidas

Trampas (descuenta vida)

Segundo nivel (sin piso solo saltar por plataformas)

Registrar errores en un txt

LAMBDA

ReGex

Boss (nene super poderoso)

Trabajar vida negativa

Colisiones de costado

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
    
    # ------ Cronómetro
tiempo_inicial = pygame.time.get_ticks()
duracion_minutos = 1
duracion_milisegundos = duracion_minutos * 60 * 1000
tiempo_transcurrido = 0


# ---------------  PANTALLA Y FONDO  ---------------
PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) # en pixeles

paisaje = pygame.image.load(r"Recursos\paisaje-fondo-01.jpg").convert()
x = 0

FONDO = pygame.image.load(r"bardito\nueva_plataforma-01.png").convert_alpha()
FONDO = pygame.transform.scale(FONDO, (ANCHO,ALTO))

pygame.display.set_caption("Robot vs todo")

icono = pygame.image.load(r"Recursos\icono.png")
pygame.display.set_icon(icono)

FUENTE = pygame.font.Font(r"Recursos\upheaval\upheavtt.ttf", 30)
NEGRO = (0,0,0)
BLANCO = (255,255,255)
NARANJA = (230, 120, 0)

# Trabajar los update con una bandera
# bandera_termino = False



# ---------------  MUSICA ---------------
sonidos()


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


# ---------------  VIDAS ---------------
tuerca1 = Vida(r"Recursos\tuerca.png", ANCHO)
lista_vidas = [tuerca1]




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
            nueva_vida = Vida(r"Recursos\tuerca.png", ANCHO)
            lista_vidas.append(nueva_vida)

    
    

    # ----- Fondo en movimiento
    x_relativa = x % paisaje.get_rect().width
    PANTALLA.blit(paisaje, (x_relativa - paisaje.get_rect().width, 0))
    if x_relativa < ANCHO:
        PANTALLA.blit(paisaje, (x_relativa, 0))
    x -= VELOCIDAD_FONDO
    PANTALLA.blit(FONDO,(0,0))
    


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
    


    # -------- Vidas
    for vida in lista_vidas:
        vida.animar(PANTALLA)
        vida.detectar_colision(vardo, lista_vidas, ALTO)
    
    
    # ----- Cronometro
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    segundos_restantes = max((duracion_milisegundos - tiempo_transcurrido) // 1000, 0)
    texto = FUENTE.render(f"{segundos_restantes}", True, NEGRO)
    sombra = FUENTE.render(f"{segundos_restantes}", True, NARANJA)

    if segundos_restantes == 0:
        mensaje = FUENTE.render("¡Se agotó el tiempo!", True, NEGRO)
        PANTALLA.blit(mensaje, (ANCHO // 2 - mensaje.get_width() // 2, ALTO // 2 - mensaje.get_height() // 2))
    else:
        PANTALLA.blit(sombra, ((ANCHO // 2) + 3, 13))
        PANTALLA.blit(texto, (ANCHO // 2, 10))


    # ----- Mostrar lineas
    if get_mode():
        pintar_lineas(PANTALLA, vardo, plataformas, lista_enemigos, lista_vidas)
    
    pygame.display.flip()

