import pygame
from V_Configuraciones import *
from V_Plataformas import *
from V_DisparoEnemigo import *

dic_enemigo = {
    "Quieto": enemigo_quieto,
    "Derecha": enemigo_camina,
    "Izquierda": enemigo_camina_izquierda,
    "Salta": enemigo_salta,
    "QuietoIzq": enemigo_quieto_izquierda,
    "SaltaIzq": enemigo_salta_izquierda }

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
        
        self.lista_disparos = []
        self.disparando = False

    
    def avanzar(self):
        if not self.esta_muerto:
            if self.direccion == "izquierda":
                self.animacion_actual = self.animaciones["Izquierda"]
                self.rectangulo_principal.x -= 3
                if self.rectangulo_principal.left < self.plataforma.left:
                    self.disparar()
                    self.rectangulo_principal.x = self.plataforma.left
                    self.direccion = "derecha"
            elif self.direccion == "derecha":
                self.animacion_actual = self.animaciones["Derecha"]
                self.rectangulo_principal.x += 3
                if self.rectangulo_principal.right > self.plataforma.right:
                    self.disparar()
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


    def actualizar(self, pantalla, lista_enemigos, plataformas, jugador):
        if not self.esta_muerto:
            self.animar(pantalla)
            self.avanzar()
        if self.vida <= 0:
            self.esta_muerto = True
            lista_enemigos.remove(self)
        
        i = 0
        while i < len(self.lista_disparos):
            self.lista_disparos[i].actualizar(pantalla, plataformas, jugador)
            if self.lista_disparos[i].choco:
                del self.lista_disparos[i]
                i -= 1
            i += 1
    
    
    def disparar(self):
        if self.direccion == "derecha":
            x = self.rectangulo_principal.x + 35
            y = self.rectangulo_principal.y + 32
        elif self.direccion == "izquierda":
            x = self.rectangulo_principal.centerx - 25
            y = self.rectangulo_principal.centery
        
        nuevo_disparo = Disparo_enemigo(x, y, self.direccion, PROYECTIL_ENEMIGO)
        self.lista_disparos.append(nuevo_disparo)
    
    def detectar_colision(self, jugador):
        lista_proyectiles = self.lista_disparos
        for proyectil in lista_proyectiles:
            if proyectil.rectangulo.colliderect(jugador.rectangulo_principal):
                jugador.vida -= 2
                