import pygame, sys
import pygame.mixer


'''------------------------------------------------------------------------
   -------------------  F U N C I O N E S  --------------------------------
   ------------------------------------------------------------------------'''

def girar_imagenes(lista_original,flip_x,flip_y):
    '''
    recibe una lista imagenes y 2 booleanos, que representa x e y
    depende los parametros que le pasemos va a girar la imagen

    devuelve la lista girada para donde quieras
    '''
    lista_girada = []
    for img in lista_original:
        lista_girada.append(pygame.transform.flip(img, flip_x, flip_y))
        
    return lista_girada

def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    '''
    recibe un diccionario de animaciones, alto y ancho.
    estos dos ultimos representan el tamaño al que queres reescalar.
    '''
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(img, (ancho, alto))

def obtener_rectangulos(principal: pygame.Rect):
    '''
    recibe un rectangulo y en base a ese, crea 5 rectangulos "secundarios"
    que se almacenan en un diccionario

    retorna el diccionario con los 5 rectangulos
    '''
    '''diccionario = {
        "main": principal,
        "bottom": pygame.Rect(principal.left, 
                              principal.bottom - 8,
                              principal.width,
                              10),
        "top": pygame.Rect(principal.left + 9,
                           principal.top + 5,
                           principal.width - 12,
                           10),
        "right": pygame.Rect(principal.right - 14,
                             principal.top + 5,
                             10,
                             principal.height),
        "left": pygame.Rect(principal.left + 3,
                            principal.top + 5,
                            10,
                            principal.height)
    }'''

    diccionario = {
        "main": principal,
        "bottom": pygame.Rect(principal.left, 
                              principal.bottom - 10,
                              principal.width,
                              10),
        "top": pygame.Rect(principal.left,
                           principal.top,
                           principal.width,
                           10),
        "right": pygame.Rect(principal.right - 10,
                             principal.top,
                             10,
                             principal.height),
        "left": pygame.Rect(principal.left,
                            principal.top,
                            10,
                            principal.height)
    }
    diccionario["left"].topleft = diccionario["top"].topleft
    diccionario["bottom"].bottomright = diccionario["right"].bottomright
    diccionario["top"].topright = diccionario["right"].topright
    diccionario["left"].bottomleft = diccionario["bottom"].bottomleft

    return diccionario

def reubicar_rectangulos(principal,rectangulos):
    rectangulos["bottom"].left = principal.left
    rectangulos["bottom"].top = principal.bottom - 8
    rectangulos["bottom"].width = principal.width
    rectangulos["bottom"].height = 10
    
    rectangulos["top"].left = principal.left + 9
    rectangulos["top"].top = principal.top + 5
    rectangulos["top"].width = principal.width - 12
    rectangulos["top"].height = 10

    rectangulos["right"].left = principal.right - 14
    rectangulos["right"].top = principal.top + 5
    rectangulos["right"].width = 10
    rectangulos["right"].height = principal.height

    rectangulos["left"].left = principal.left + 3
    rectangulos["left"].top = principal.top + 5
    rectangulos["left"].width = 10
    rectangulos["left"].height = principal.height

def reescalar_imagen(imagen, nuevo_ancho, nuevo_alto):
    return pygame.transform.scale(imagen, (nuevo_ancho, nuevo_alto))

def reescalar_lista_imagenes(lista_imagenes, nuevo_ancho, nuevo_alto):
    imagenes_reescaladas = []
    for imagen in lista_imagenes:
        imagenes_reescaladas.append(reescalar_imagen(imagen, nuevo_ancho, nuevo_alto))
    return imagenes_reescaladas

def you_win(fuente, color_letras, color_fondo, pantalla, superficie_opaca):
    
    tiempo_inicio = pygame.time.get_ticks()  # obtengo tiempo actual
    
    mensaje = fuente.render("¡GANASTE!", True, color_letras, color_fondo)
    mitad_x = pantalla.get_width() // 2 - mensaje.get_width() // 2
    pantalla.blit(superficie_opaca, (0,0))
    pantalla.blit(mensaje, (mitad_x, 360))


    pygame.display.flip()  # actualizo la pantalla

    # con este bucle creamos una espera de 2 segundos antes de cerrar la ventana
    while pygame.time.get_ticks() - tiempo_inicio < 3000: # (3000 milisegundos = 3 segundos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.quit()
    sys.exit()

def game_over(fuente, color_letras, color_fondo, pantalla, superficie_opaca):
    '''
    esta funcion recibe una fuente, algunos colores, la pantalla donde
    se va a mostrar el "game over" y la superficie opaca es una surface
    con 50% de opacidad, una cuestion estetica.
    
    esta funcion la utilizo cuando el jugador se equivoca o se queda sin tiempo
    '''
    
    tiempo_inicio = pygame.time.get_ticks()  # obtengo tiempo actual
    
    mensaje = fuente.render("GAME OVER", True, color_letras, color_fondo)
    pantalla.blit(superficie_opaca, (0,0))
    pantalla.blit(mensaje, (275, 243))
        
    pygame.display.flip() 

    while pygame.time.get_ticks() - tiempo_inicio < 2000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.quit()
    sys.exit()




'''------------------------------------------------------------------------
   -------------------  P A T H S -----------------------------------------
   ------------------------------------------------------------------------'''

SONIDO_MONEDA = r"Recursos\sonidos\collectcoin.wav"
SONIDO_VIDA = r"Recursos\sonidos\vida.wav"
MUSICA_NIVEL_1 = r"Recursos\sonidos\sonido-principal.wav"
MUSICA_NIVEL_2 = r"Recursos\sonidos\password-infinity-123276.wav"
PROYECTIL_JUGADOR = r"Recursos\proyectil_jugador.png"
PROYECTIL_ENEMIGO = r"Recursos\proyectil.png"
ICONO_PNG = r"Recursos\icono.png"
FUENTE_TEXTO = r"Recursos\upheaval\upheavtt.ttf"
TUERCA_VIDA = r"Recursos\tuerca.png"
FONDO_MOVIBLE = r"Recursos\paisaje-fondo-01.jpg"
FONDO_NIVEL_1 = r"Recursos\plataforma_nivel1.png"
FONDO_NIVEL_2 = r"Recursos\plataforma_nivel2.png"





'''------------------------------------------------------------------------
   -------------------  P E R S O N A J E  P R I N C I P A L  -------------
   ------------------------------------------------------------------------''' 

personaje_quieto = [pygame.image.load(r"Jugador\Idle (1).png"),
                    pygame.image.load(r"Jugador\Idle (2).png"),
                    pygame.image.load(r"Jugador\Idle (3).png"),
                    pygame.image.load(r"Jugador\Idle (4).png"),
                    pygame.image.load(r"Jugador\Idle (5).png"),
                    pygame.image.load(r"Jugador\Idle (6).png"),
                    pygame.image.load(r"Jugador\Idle (7).png"),
                    pygame.image.load(r"Jugador\Idle (8).png"),
                    pygame.image.load(r"Jugador\Idle (9).png"),
                    pygame.image.load(r"Jugador\Idle (10).png")]

personaje_corre =  [pygame.image.load(r"Jugador\Run (1).png"),
                    pygame.image.load(r"Jugador\Run (2).png"),
                    pygame.image.load(r"Jugador\Run (3).png"),
                    pygame.image.load(r"Jugador\Run (4).png"),
                    pygame.image.load(r"Jugador\Run (5).png"),
                    pygame.image.load(r"Jugador\Run (6).png"),
                    pygame.image.load(r"Jugador\Run (7).png"),
                    pygame.image.load(r"Jugador\Run (8).png"),]

personaje_salta =  [pygame.image.load(r"Jugador\Jump (1).png"),
                    pygame.image.load(r"Jugador\Jump (2).png"),
                    pygame.image.load(r"Jugador\Jump (3).png"),
                    pygame.image.load(r"Jugador\Jump (4).png"),
                    pygame.image.load(r"Jugador\Jump (5).png"),
                    pygame.image.load(r"Jugador\Jump (6).png"),
                    pygame.image.load(r"Jugador\Jump (7).png"),
                    pygame.image.load(r"Jugador\Jump (8).png"),
                    pygame.image.load(r"Jugador\Jump (9).png"),
                    pygame.image.load(r"Jugador\Jump (10).png")]

personaje_dispara = [pygame.image.load(r"Jugador\Shoot (1).png"),
                    pygame.image.load(r"Jugador\Shoot (2).png"),
                    pygame.image.load(r"Jugador\Shoot (3).png"),
                    pygame.image.load(r"Jugador\Shoot (4).png")]

personaje_corre_dispara = [pygame.image.load(r"Jugador\RunShoot (1).png"),
                        pygame.image.load(r"Jugador\RunShoot (2).png"),
                        pygame.image.load(r"Jugador\RunShoot (3).png"),
                        pygame.image.load(r"Jugador\RunShoot (4).png"),
                        pygame.image.load(r"Jugador\RunShoot (5).png"),
                        pygame.image.load(r"Jugador\RunShoot (6).png"),
                        pygame.image.load(r"Jugador\RunShoot (7).png"),
                        pygame.image.load(r"Jugador\RunShoot (8).png"),
                        pygame.image.load(r"Jugador\RunShoot (9).png"),]

personaje_camina_izquierda = girar_imagenes(personaje_corre, True, False)

personaje_quieto_izquierda = girar_imagenes(personaje_quieto, True, False)

personaje_salta_izquierda  = girar_imagenes(personaje_salta, True, False)

personaje_dispara_izquierda = girar_imagenes(personaje_dispara, True, False)

personaje_corre_dispara_izquierda = girar_imagenes(personaje_corre_dispara, True, False)






''' -----------------------------------------------------------------------
----------------------  E N E M I G O S  ----------------------------------
------------------------------------------------------------------------ '''

enemigo_camina = [pygame.image.load(r"enemigo\run 1.png"),
                pygame.image.load(r"enemigo\run 2.png"),
                pygame.image.load(r"enemigo\run 3.png"),
                pygame.image.load(r"enemigo\run 4.png"),
                pygame.image.load(r"enemigo\run 5.png"),
                pygame.image.load(r"enemigo\run 6.png"),
                pygame.image.load(r"enemigo\run 7.png"),
                pygame.image.load(r"enemigo\run 8.png")]

enemigo_quieto = [pygame.image.load(r"enemigo\idle1.png"),
                pygame.image.load(r"enemigo\idle2.png"),
                pygame.image.load(r"enemigo\idle3.png"),
                pygame.image.load(r"enemigo\idle4.png")]

enemigo_salta = [pygame.image.load(r"enemigo\jump 1.png"),
                pygame.image.load(r"enemigo\jump 2.png"),
                pygame.image.load(r"enemigo\jump 3.png"),
                pygame.image.load(r"enemigo\jump 4.png"),
                pygame.image.load(r"enemigo\jump 5.png"),
                pygame.image.load(r"enemigo\jump 6.png"),
                pygame.image.load(r"enemigo\jump 7.png"),
                pygame.image.load(r"enemigo\jump 8.png")]

enemigo_camina_izquierda = girar_imagenes(enemigo_camina, True, False)

enemigo_quieto_izquierda = girar_imagenes(enemigo_quieto, True, False)

enemigo_salta_izquierda  = girar_imagenes(enemigo_salta, True, False)





''' -----------------------------------------------------------------------
----------------------  M O N E D A S  ------------------------------------
------------------------------------------------------------------------ '''

lista1_monedas =   [pygame.image.load(r"monedas\1.png"),
                    pygame.image.load(r"monedas\2.png"),
                    pygame.image.load(r"monedas\3.png"),
                    pygame.image.load(r"monedas\4.png"),
                    pygame.image.load(r"monedas\5.png"),]
primera_lista_monedas = reescalar_lista_imagenes(lista1_monedas, 20, 20)

lista2_monedas =   [pygame.image.load(r"monedas\6.png"),
                    pygame.image.load(r"monedas\7.png"),
                    pygame.image.load(r"monedas\8.png"),
                    pygame.image.load(r"monedas\9.png"),
                    pygame.image.load(r"monedas\10.png"),]
segunda_lista_monedas = reescalar_lista_imagenes(lista2_monedas, 20, 20)




''' -----------------------------------------------------------------------
----------------------  P O R T A L  ------------------------------------
------------------------------------------------------------------------ '''

imagenes_portal =  [pygame.image.load(r"Recursos\portal1.png"),
                    pygame.image.load(r"Recursos\portal2.png"),
                    pygame.image.load(r"Recursos\portal3.png"),
                    pygame.image.load(r"Recursos\portal4.png"),
                    pygame.image.load(r"Recursos\portal5.png"),
                    pygame.image.load(r"Recursos\portal6.png"),
                    pygame.image.load(r"Recursos\portal7.png"),
                    pygame.image.load(r"Recursos\portal8.png"),
                    pygame.image.load(r"Recursos\portal9.png"),
                    pygame.image.load(r"Recursos\portal10.png"),
                    pygame.image.load(r"Recursos\portal11.png"),
                    pygame.image.load(r"Recursos\portal12.png"),
                    pygame.image.load(r"Recursos\portal13.png"),
                    pygame.image.load(r"Recursos\portal14.png"),
                    pygame.image.load(r"Recursos\portal15.png"),
                    pygame.image.load(r"Recursos\portal16.png")]

lista_imagenes_portal = reescalar_lista_imagenes(imagenes_portal, 120, 120)


