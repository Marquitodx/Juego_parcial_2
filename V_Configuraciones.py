import pygame
import pygame.mixer

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


# def sonidos():
#     pygame.mixer.music.load(r"Recursos\sonidos\sonido-principal.wav")
#     pygame.mixer.music.set_volume(0.3)
#     pygame.mixer.music.play(-1)


def pintar_lineas(pantalla, personaje, plataformas, enemigos):
    pygame.draw.rect(pantalla,"blue", personaje.rectangulos["main"], 2)
    pygame.draw.rect(pantalla,"red", personaje.rectangulos["bottom"], 2)
    pygame.draw.rect(pantalla,"red", personaje.rectangulos["top"], 2)
    pygame.draw.rect(pantalla,"red", personaje.rectangulos["right"], 2)
    pygame.draw.rect(pantalla,"red", personaje.rectangulos["left"], 2)
    
    

    for plataforma in plataformas:
        pygame.draw.rect(pantalla,"pink",plataforma.rectangulos["main"], 2)
        pygame.draw.rect(pantalla,"magenta", plataforma.rectangulos["bottom"], 2)
        pygame.draw.rect(pantalla,"magenta", plataforma.rectangulos["top"], 2)
        pygame.draw.rect(pantalla,"magenta", plataforma.rectangulos["right"], 2)
        pygame.draw.rect(pantalla,"magenta", plataforma.rectangulos["left"], 2)
        
        
    for enemigo in enemigos:
        pygame.draw.rect(pantalla,"orange", enemigo.rectangulo_principal, 3)




'''-------------------  P E R S O N A J E  P R I N C I P A L  -------------'''          
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




'''-------------------  E N E M I G O S  ----------------------------------'''
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



def reescalar_imagen(imagen, nuevo_ancho, nuevo_alto):
    return pygame.transform.scale(imagen, (nuevo_ancho, nuevo_alto))

def reescalar_lista_imagenes(lista_imagenes, nuevo_ancho, nuevo_alto):
    imagenes_reescaladas = []
    for imagen in lista_imagenes:
        imagenes_reescaladas.append(reescalar_imagen(imagen, nuevo_ancho, nuevo_alto))
    return imagenes_reescaladas

lista1_monedas = [pygame.image.load(r"monedas\1.png"),
                pygame.image.load(r"monedas\2.png"),
                pygame.image.load(r"monedas\3.png"),
                pygame.image.load(r"monedas\4.png"),
                pygame.image.load(r"monedas\5.png"),]
primera_lista_monedas = reescalar_lista_imagenes(lista1_monedas, 20, 20)

lista2_monedas = [pygame.image.load(r"monedas\6.png"),
                pygame.image.load(r"monedas\7.png"),
                pygame.image.load(r"monedas\8.png"),
                pygame.image.load(r"monedas\9.png"),
                pygame.image.load(r"monedas\10.png"),]
segunda_lista_monedas = reescalar_lista_imagenes(lista2_monedas, 20, 20)







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
