import pygame, random
from V_Configuraciones import *
from V_Plataformas import *


class Enemigo:
    def __init__(self, animaciones, limite1, limite2, inicio_x, inicio_y) -> None:
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, 60, 80)
        self.rectangulo_principal = animaciones["Izquierda"][0].get_rect()
        self.rectangulo_principal.x = inicio_x
        self.rectangulo_principal.y = inicio_y
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["Izquierda"]
        self.direccion = "izquierda"
        self.limite1 = limite1
        self.limite2 = limite2
        
        self.vida = 20
        self.esta_muerto = False

    
    def avanzar(self):
        if not self.esta_muerto:
            if self.direccion == "izquierda":
                self.animacion_actual = self.animaciones["Izquierda"]
                self.rectangulo_principal.x -= 5
                if self.rectangulo_principal.left <= self.limite1:
                    self.rectangulo_principal.x = self.limite1
                    self.direccion = "derecha"
            elif self.direccion == "derecha":
                self.animacion_actual = self.animaciones["Derecha"]
                self.rectangulo_principal.x += 5
                if self.rectangulo_principal.right >= self.limite2:
                    self.rectangulo_principal.x = self.limite2 - self.rectangulo_principal.width
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
    


    @staticmethod
    def crear_lista():   # Como hago para mostrar enemigos aleatoriamente?
        lista = []
        
        dic_enemigo = {
            "Quieto": enemigo_quieto,
            "Derecha": enemigo_camina,
            "Izquierda": enemigo_camina_izquierda,
            "Salta": enemigo_salta,
            "QuietoIzq": enemigo_quieto_izquierda,
            "SaltaIzq": enemigo_salta_izquierda }
        

        enemigos_info = [
            {"limite1": 962, "limite2": 1280, "inicio_x": 1200, "inicio_y": 600},
            {"limite1": 243, "limite2": 520, "inicio_x": 515, "inicio_y": 600},
            {"limite1": 135, "limite2": 353, "inicio_x": 135, "inicio_y": 290},
            {"limite1": 575, "limite2": 806, "inicio_x": 800, "inicio_y": 180},
            {"limite1": 865, "limite2": 1060, "inicio_x": 850, "inicio_y": 397}
            ]

        for info in enemigos_info:
            enemigo = Enemigo(dic_enemigo, 
                            info["limite1"], 
                            info["limite2"],
                            info["inicio_x"],
                            info["inicio_y"])
            
            lista.append(enemigo)

        random.shuffle(lista)  # Aleatoriza la lista de enemigos

        return lista





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
