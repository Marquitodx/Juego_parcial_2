import pygame, random
from V_Configuraciones import *
from V_Plataformas import *
from V_Listas import *

dic_enemigo = {
    "Quieto": enemigo_quieto,
    "Derecha": enemigo_camina,
    "Izquierda": enemigo_camina_izquierda,
    "Salta": enemigo_salta,
    "QuietoIzq": enemigo_quieto_izquierda,
    "SaltaIzq": enemigo_salta_izquierda }



''' Heredar de personaje '''
class Enemigo:
    def __init__(self, plataforma) -> None:
        self.animaciones = dic_enemigo
        reescalar_imagenes(self.animaciones, 60, 80)
        self.rectangulo_principal = self.animaciones["Izquierda"][0].get_rect()
        self.rectangulo_principal.x = plataforma.x
        self.rectangulo_principal.y = plataforma.y - 80
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["Izquierda"]
        self.direccion = "izquierda"
        self.plataforma = plataforma
        
        self.vida = 20
        self.esta_muerto = False

    
    def avanzar(self):
        if not self.esta_muerto:
            if self.direccion == "izquierda":
                self.animacion_actual = self.animaciones["Izquierda"]
                self.rectangulo_principal.x -= 5
                if self.rectangulo_principal.left < self.plataforma.left:
                    self.rectangulo_principal.x = self.plataforma.left
                    self.direccion = "derecha"
            elif self.direccion == "derecha":
                self.animacion_actual = self.animaciones["Derecha"]
                self.rectangulo_principal.x += 5
                if self.rectangulo_principal.right > self.plataforma.right:
                    self.rectangulo_principal.x = self.plataforma.right - self.rectangulo_principal.width
                    self.direccion = "izquierda"


    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo_principal)
        self.contador_pasos +=1
        
        if self.esta_muerto and self.contador_pasos == largo:
            self.esta_muerto = True


    def actualizar(self, pantalla, lista_enemigos):
        if not self.esta_muerto:
            self.animar(pantalla)
            self.avanzar()
        if self.vida <= 0:
            self.esta_muerto = True
            lista_enemigos.remove(self)
    








# class Enemy:
#     def __init__(self):
#         # Inicialización de enemigo
#         self.image = pygame.image.load("ruta_imagen_enemigo.png")
#         self.rect = self.image.get_rect()
#         self.rect.x = 500  # Posición inicial en X
#         self.rect.y = 250  # Posición inicial en Y
#         # Otras propiedades del enemigo

#     def update(self):
#         pass
#         # Lógica de actualización del enemigo
#         # Por ejemplo, movimiento del enemigo

#     def draw(self, pantalla):
#         # Dibuja el enemigo en la pantalla
#         pantalla.blit(self.image, self.rect)















# class Enemy:
#     def __init__(self):
#         # Inicialización de enemigo
#         self.image = pygame.image.load("ruta_imagen_enemigo.png")
#         self.rect = self.image.get_rect()
#         self.rect.x = 500  # Posición inicial en X
#         self.rect.y = 250  # Posición inicial en Y
#         # Otras propiedades del enemigo

#     def update(self):
#         pass
#         # Lógica de actualización del enemigo
#         # Por ejemplo, movimiento del enemigo

#     def draw(self, pantalla):
#         # Dibuja el enemigo en la pantalla
#         pantalla.blit(self.image, self.rect)
