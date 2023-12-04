import pygame
from V_Configuraciones import *
from V_Disparos import *

diccionario_animaciones = {"Quieto": personaje_quieto,
                        "Derecha": personaje_corre,
                        "Izquierda": personaje_camina_izquierda,
                        "Salta": personaje_salta,
                        "QuietoIzq": personaje_quieto_izquierda,
                        "SaltaIzq": personaje_salta_izquierda,
                        "DisparaDer": personaje_dispara,
                        "DisparaIzq": personaje_dispara_izquierda,
                        "CorreDisparaDer": personaje_corre_dispara,
                        "CorreDisparaIzq": personaje_corre_dispara_izquierda}

class Personaje:
    def __init__(self, tamaño, pos_x, pos_y, velocidad):
        self.animaciones = diccionario_animaciones
        reescalar_imagenes(self.animaciones, 50, 70)
        self.rectangulo_principal = self.animaciones["Quieto"][0].get_rect()
        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y
        self.velocidad = velocidad
        self.contador_pasos = 0
        self.que_hace = "Quieto"
        self.animacion_actual = self.animaciones["Quieto"]
        self.direccion = "derecha"
        self.disparo = True

        self.rectangulos = obtener_rectangulos(self.rectangulo_principal)
    
    # ------  VITALIDAD  -------
        self.vida = 50
        self.puntaje = 0

    # ------  SALTO  -------
        self.desplazamiento_y = 0 
        self.potencia_salto = -17
        self.limite_velocidad_salto = 17 
        self.esta_saltando = True
        self.gravedad = 1 

    # ------  DISPAROS  -------
        self.esta_disparando = False
        self.lista_disparos = []
        self.avanzar = True
    

    def caminar(self, pantalla, plataformas):
        velocidad_actual = self.velocidad
        if self.que_hace == "Izquierda" or self.que_hace == "CorreDisparaIzq":
            velocidad_actual *= -1
            
        nueva_posicion = self.rectangulos["main"].x + velocidad_actual
        if 0 <= nueva_posicion <= (pantalla.get_width() - self.rectangulos["main"].width) and self.avanzar:
                for lado in self.rectangulos:
                    self.rectangulos[lado].x += velocidad_actual
                    
                    # for piso in plataformas:
                    #     if self.rectangulos["right"].colliderect(piso.rectangulos["left"]):
                    #         self.avanzar = False
                    #         break


    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo_principal)
        self.contador_pasos +=1


    def saltar(self):
        if not self.esta_saltando:
            if self.direccion == "derecha":
                self.esta_saltando = True
                self.desplazamiento_y = self.potencia_salto
                self.animacion_actual = self.animaciones["Salta"]
            elif self.direccion == "izquierda":
                self.esta_saltando = True
                self.desplazamiento_y = self.potencia_salto
                self.animacion_actual = self.animaciones["SaltaIzq"]


    def actualizar(self, pantalla, plataformas, enemigos, fuente, jugador):
        
        TECLA_DERECHA = pygame.K_RIGHT
        TECLA_IZQUIERDA = pygame.K_LEFT
        TECLA_ESPACIO = pygame.K_SPACE
        TECLA_F = pygame.K_f
        NARANJA = (230, 120, 0)
        NEGRO = (0,0,0)
        
        keys = pygame.key.get_pressed()

        # --- camina a la derecha
        if keys[TECLA_DERECHA]:
            if keys[pygame.K_f]:
                self.que_hace = "CorreDisparaDer"
                self.disparar(enemigos)
            else:
                self.que_hace = "Derecha"
            self.direccion = "derecha"

        # --- camina a la izquierda
        elif keys[TECLA_IZQUIERDA]:
            if keys[pygame.K_f]:
                self.que_hace = "CorreDisparaIzq"
                self.disparar(enemigos)
            else:
                self.que_hace = "Izquierda"
            self.direccion = "izquierda"

        # --- salta
        elif keys[TECLA_ESPACIO]:
            self.saltar()

        # --- dispara quieto
        elif keys[TECLA_F]:
            if self.direccion == "derecha":
                self.que_hace = "DisparaDer"
                self.disparar(enemigos)
            elif self.direccion == "izquierda":
                self.que_hace = "DisparaIzq"
                self.disparar(enemigos)


        # --- esta quieto izquierda
        elif self.direccion == "izquierda":
            self.que_hace = "QuietoIzq"

        # --- esta quieto derecha
        elif self.direccion == "derecha":
                self.que_hace = "Quieto"


        match self.que_hace:

            case "Derecha":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["Derecha"]
                    self.animar(pantalla)
                self.caminar(pantalla, plataformas)

            case "Izquierda":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["Izquierda"]
                    self.animar(pantalla)
                self.caminar(pantalla, plataformas)

            case "Quieto":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["Quieto"]
                    self.animar(pantalla)
            
            case "QuietoIzq":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["QuietoIzq"]
                    self.animar(pantalla)
            
            case "DisparaDer":
                self.animacion_actual = self.animaciones["DisparaDer"]
                self.animar(pantalla)
            
            case "DisparaIzq":
                self.animacion_actual = self.animaciones["DisparaIzq"]
                self.animar(pantalla)
            
            case "CorreDisparaDer":
                self.animacion_actual = self.animaciones["CorreDisparaDer"]
                self.animar(pantalla)
                self.caminar(pantalla, plataformas)
            
            case "CorreDisparaIzq":
                self.animacion_actual = self.animaciones["CorreDisparaIzq"]
                self.animar(pantalla)
                self.caminar(pantalla, plataformas)


        self.aplicar_gravedad(pantalla, plataformas)

        i = 0
        while i < len(self.lista_disparos):
            self.lista_disparos[i].actualizar(pantalla, enemigos, plataformas, jugador)
            if self.lista_disparos[i].choco:
                del self.lista_disparos[i]
                i -= 1
            i += 1
        
        
        texto_puntaje = fuente.render(f"Puntaje: {self.puntaje}", True, NEGRO)
        sombra_texto_puntaje = fuente.render(f"Puntaje: {self.puntaje}", True, NARANJA)
        pantalla.blit(sombra_texto_puntaje, (13, 13))
        pantalla.blit(texto_puntaje, (10, 10))
        
        contador_vida = fuente.render(f"Vida: {self.vida}", True, NEGRO)
        sombra_contador_vida = fuente.render(f"Vida: {self.vida}", True, NARANJA)
        pantalla.blit(sombra_contador_vida, (1003, 13))
        pantalla.blit(contador_vida, (1000, 10))

    def aplicar_gravedad(self, pantalla, plataformas):
        
        velocidad_salto = self.desplazamiento_y

        if self.esta_saltando:
            self.animar(pantalla)

            for lado in self.rectangulos:
                self.rectangulos[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad

        for piso in plataformas:
            if self.rectangulos["bottom"].colliderect(piso.rectangulo):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.rectangulos["main"].bottom = piso.rectangulo.top
                reubicar_rectangulos(self.rectangulo_principal,self.rectangulos)
                break
            
            elif self.rectangulos["top"].colliderect(piso.rectangulos["bottom"]):
                self.desplazamiento_y *= -1
            
            # elif self.rectangulos["right"].colliderect(piso.rectangulo):
            #     self.rectangulos["main"].right = piso.rectangulo.left
            #     self.desplazamiento_y = 0
            #     self.esta_saltando = False

            else:
                self.esta_saltando = True


    def detectar_colision(self, enemigos, height, lista_monedas):
        lista_proyectiles = self.lista_disparos
        if self.rectangulo_principal.top > height:
            self.muere()
        for enemigo in enemigos:
            if self.rectangulos["main"].colliderect(enemigo.rectangulo_principal):
                self.vida -= 1
                break
            
            for proyectil in lista_proyectiles:
                if proyectil.rectangulo.colliderect(enemigo.rectangulo_principal):
                    self.puntaje += 1
        
        # for moneda in lista_monedas:
        #     if self.rectangulo_principal.colliderect(moneda.rectangulo):
        #         self.puntaje += 5


    def muere(self):
        self.rectangulo_principal.x = 50
        self.rectangulo_principal.y = 590
        self.esta_saltando = False
        self.desplazamiento_y = 0
        self.que_hace = "Quieto"
        self.rectangulos = obtener_rectangulos(self.rectangulo_principal)


    def disparar(self, enemigos):
        if self.direccion == "derecha":
            x = self.rectangulos["main"].x + 35
            y = self.rectangulos["main"].y + 32
        elif self.direccion == "izquierda":
            x = self.rectangulos["main"].centerx - 25
            y = self.rectangulos["main"].centery
        
        nuevo_disparo = Disparo(x, y, self.direccion, r"Recursos\robotfree\png\Objects\Bullet_000.png")
        nuevo_disparo.sonido_disparo.play()
        self.lista_disparos.append(nuevo_disparo)