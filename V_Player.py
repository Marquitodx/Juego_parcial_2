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
        reescalar_imagenes(self.animaciones, 50, 75)
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
        self.vida = 4
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
    

    def caminar(self, pantalla, plataformas):
        velocidad_actual = self.velocidad
        if self.que_hace == "Izquierda" or self.que_hace == "CorreDisparaIzq":
            velocidad_actual *= -1
            
        nueva_posicion = self.rectangulos["main"].x + velocidad_actual
        if 0 <= nueva_posicion <= (pantalla.get_width() - self.rectangulos["main"].width):
                for lado in self.rectangulos:
                    self.rectangulos[lado].x += velocidad_actual


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


    def actualizar(self,evento_tiempo,pantalla, plataformas, enemigos):
        
        keys = pygame.key.get_pressed()
       
        for evento in pygame.event.get():
            if evento.type == evento_tiempo:
                self.disparo = True

# --- camina a la derecha
        if keys[pygame.K_RIGHT]:
            if keys[pygame.K_f] and self.disparo:
                self.que_hace = "CorreDisparaDer"
                self.disparar(enemigos)
                self.disparo = False
            else:
                self.que_hace = "Derecha"
            self.direccion = "derecha"

# --- camina a la izquierda
        elif keys[pygame.K_LEFT]:
            if keys[pygame.K_f] and self.disparo:
                self.que_hace = "CorreDisparaIzq"
                self.disparar(enemigos)
                self.disparo = False
            else:
                self.que_hace = "Izquierda"
            self.direccion = "izquierda"

# --- salta
        elif keys[pygame.K_SPACE]:
            self.saltar()

# --- dispara quieto
        elif keys[pygame.K_f] and self.disparo:
            if self.direccion == "derecha":
                self.que_hace = "DisparaDer"
                self.disparar(enemigos)
            elif self.direccion == "izquierda":
                self.que_hace = "DisparaIzq"
                self.disparar(enemigos)

            self.disparo = False

# --- esta quieto izquierda
        elif self.direccion == "izquierda":
            self.que_hace = "QuietoIzq"

# --- esta quieto derecha
        elif self.direccion == "derecha":
                self.que_hace = "Quieto"

# Si esta quieto y la direccion es izquierda, que quede para la izquierda y viceversa

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
            self.lista_disparos[i].actualizar(pantalla, enemigos, plataformas)
            if self.lista_disparos[i].choco:
                del self.lista_disparos[i]
                i -= 1
            i += 1

# acomodar <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
                #self.rectangulos = obtener_rectangulos(self.rectangulo_principal)
                reubicar_rectangulos(self.rectangulo_principal,self.rectangulos)
                break
            elif self.rectangulos["top"].colliderect(piso.rectangulo):
                self.desplazamiento_y *= -1
            else:
                self.esta_saltando = True
        
        
            # Crear una bandera para que los cuadrados no puedan irse de los margenes del principal


    def detectar_colision(self, enemigos, height):
        if self.rectangulo_principal.top > height:
            self.muere()
        for enemigo in enemigos:
            if self.rectangulos["main"].colliderect(enemigo.rectangulo_principal):
                self.muere()
                break


    def muere(self):
        vida = self.vida
        print("¡El personaje ha muerto! ahora le quedan", {vida}, "vidas")
        self.vida -= 1
        self.rectangulo_principal.x = 50
        self.rectangulo_principal.y = 600
        self.esta_saltando = False
        self.desplazamiento_y = 0
        self.que_hace = "Quieto"
        self.rectangulos = obtener_rectangulos(self.rectangulo_principal)


# agregar lapso de disparo <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def disparar(self, enemigos):
        if self.direccion == "derecha":
            x = self.rectangulos["main"].x + 35
            y = self.rectangulos["main"].y + 32
        elif self.direccion == "izquierda":
            x = self.rectangulos["main"].centerx - 25
            y = self.rectangulos["main"].centery
        
        nuevo_disparo = Disparo(x, y, self.direccion)
#        nuevo_disparo.sonido_disparo.play()
        self.lista_disparos.append(nuevo_disparo)

        for enemigo in enemigos:
            if nuevo_disparo.rectangulo.colliderect(enemigo.rectangulo_principal):
                self.puntaje += 1
                print("Puntaje: ", self.puntaje)


        # flag_disparo = True
        # ultimo_disparo = 0

        # if flag_disparo:
        #     tiempo_actual = pygame.time.get_ticks()
        #     if tiempo_actual - ultimo_disparo >= 1000:
        #         self.disparar()
        #         flag_disparo = False
        #         ultimo_disparo = tiempo_actual