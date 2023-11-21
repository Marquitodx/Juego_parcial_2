import pygame

def girar_imagenes(lista_original,flip_x,flip_y):
    lista_girada = []
    for img in lista_original:
        lista_girada.append(pygame.transform.flip(img, flip_x, flip_y))
        
    return lista_girada

def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(img, (ancho, alto))

def obtener_rectangulos(principal: pygame.Rect):
    diccionario = {
        "main": principal,
        "bottom": pygame.Rect(principal.left, principal.bottom - 8, principal.width, 10),
        "top": pygame.Rect(principal.left + 9, principal.top + 5, principal.width - 12, 10),
        "right": pygame.Rect(principal.right - 14, principal.top + 5, 10, principal.height),
        "left": pygame.Rect(principal.left + 3, principal.top + 5, 10, principal.height)
    }

    return diccionario

def sonidos():
    pygame.mixer.music.load(r"Juego_plataforma-main\Recursos\sonidos\sonido-principal.wav")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)





'''------------------------------------------------------------------------
///////////////////////////////////////////////////////////////////////////
-------------------  P E R S O N A J E  P R I N C I P A L  -------------'''          

personaje_quieto = [pygame.image.load(r"Juego_plataforma-main\Jugador\Idle (1).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Idle (2).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Idle (3).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Idle (4).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Idle (5).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Idle (6).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Idle (7).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Idle (8).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Idle (9).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Idle (10).png")]

personaje_corre =  [pygame.image.load(r"Juego_plataforma-main\Jugador\Run (1).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Run (2).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Run (3).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Run (4).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Run (5).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Run (6).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Run (7).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Run (8).png"),]

personaje_salta =  [pygame.image.load(r"Juego_plataforma-main\Jugador\Jump (1).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Jump (2).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Jump (3).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Jump (4).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Jump (5).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Jump (6).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Jump (7).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Jump (8).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Jump (9).png"),
                    pygame.image.load(r"Juego_plataforma-main\Jugador\Jump (10).png")]

personaje_dispara = [pygame.image.load(r"Juego_plataforma-main\Jugador\Shoot (1).png"),
                     pygame.image.load(r"Juego_plataforma-main\Jugador\Shoot (2).png"),
                     pygame.image.load(r"Juego_plataforma-main\Jugador\Shoot (3).png"),
                     pygame.image.load(r"Juego_plataforma-main\Jugador\Shoot (4).png")]

personaje_corre_dispara = [pygame.image.load(r"Juego_plataforma-main\Jugador\RunShoot (1).png"),
                           pygame.image.load(r"Juego_plataforma-main\Jugador\RunShoot (2).png"),
                           pygame.image.load(r"Juego_plataforma-main\Jugador\RunShoot (3).png"),
                           pygame.image.load(r"Juego_plataforma-main\Jugador\RunShoot (4).png"),
                           pygame.image.load(r"Juego_plataforma-main\Jugador\RunShoot (5).png"),
                           pygame.image.load(r"Juego_plataforma-main\Jugador\RunShoot (6).png"),
                           pygame.image.load(r"Juego_plataforma-main\Jugador\RunShoot (7).png"),
                           pygame.image.load(r"Juego_plataforma-main\Jugador\RunShoot (8).png"),
                           pygame.image.load(r"Juego_plataforma-main\Jugador\RunShoot (9).png"),]


# ----------------------------------------------------------------------- REVISAR
personaje_camina_izquierda = girar_imagenes(personaje_corre, True, False)
personaje_quieto_izquierda = girar_imagenes(personaje_quieto, True, False)
personaje_salta_izquierda  = girar_imagenes(personaje_salta, True, False)
personaje_dispara_izquierda = girar_imagenes(personaje_dispara, True, False)
personaje_corre_dispara_izquierda = girar_imagenes(personaje_corre_dispara, True, False)
# -----------------------------------------------------------------------


'''------------------------------------------------------------------------
///////////////////////////////////////////////////////////////////////////
------------------------------------------------------------------------'''




'''------------------------------------------------------------------------
///////////////////////////////////////////////////////////////////////////
-------------------  E N E M I G O S  ----------------------------------'''

enemigo_camina = [pygame.image.load(r"Juego_plataforma-main\enemigo\run 1.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\run 2.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\run 3.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\run 4.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\run 5.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\run 6.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\run 7.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\run 8.png")]

enemigo_quieto = [pygame.image.load(r"Juego_plataforma-main\enemigo\idle1.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\idle2.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\idle3.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\idle4.png")]

enemigo_salta = [pygame.image.load(r"Juego_plataforma-main\enemigo\jump 1.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\jump 2.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\jump 3.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\jump 4.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\jump 5.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\jump 6.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\jump 7.png"),
                pygame.image.load(r"Juego_plataforma-main\enemigo\jump 8.png")]


enemigo_camina_izquierda = girar_imagenes(enemigo_camina, True, False)
enemigo_quieto_izquierda = girar_imagenes(enemigo_quieto, True, False)
enemigo_salta_izquierda  = girar_imagenes(enemigo_salta, True, False)


'''------------------------------------------------------------------------
///////////////////////////////////////////////////////////////////////////
------------------------------------------------------------------------'''


lista1_monedas = [pygame.image.load(r"Juego_plataforma-main\monedas\1.png"),
                pygame.image.load(r"Juego_plataforma-main\monedas\2.png"),
                pygame.image.load(r"Juego_plataforma-main\monedas\3.png"),
                pygame.image.load(r"Juego_plataforma-main\monedas\4.png"),
                pygame.image.load(r"Juego_plataforma-main\monedas\5.png"),]

lista2_monedas = [pygame.image.load(r"Juego_plataforma-main\monedas\6.png"),
                pygame.image.load(r"Juego_plataforma-main\monedas\7.png"),
                pygame.image.load(r"Juego_plataforma-main\monedas\8.png"),
                pygame.image.load(r"Juego_plataforma-main\monedas\9.png"),
                pygame.image.load(r"Juego_plataforma-main\monedas\10.png"),]





# class Game:
#     def __init__(self, pantalla):
#         self.pantalla = pantalla
#         self.clock = pygame.time.Clock()
#         self.FPS = 60
#         self.player = Player()
#         self.enemies = [Enemy() for _ in range(3)]

#     def run(self):
#         running = True
#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False

#             self.player.update()
#             for enemy in self.enemies:
#                 enemy.update()

#             self.draw()
#             self.clock.tick(self.FPS)

#     def draw(self):
#         self.pantalla.fill(colores.Azul_marino)
#         # Dibuja elementos del juego, como jugador y enemigos
#         self.player.draw(self.pantalla)
#         for enemy in self.enemies:
#             enemy.draw(self.pantalla)
#         pygame.display.flip()
