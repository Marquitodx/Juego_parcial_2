import pygame

# disparar cada 1000 milis

class Disparo:
    def __init__(self, x, y, direccion):
        self.direccion = direccion # para ver de donde y hacia donde va
        self.velocidad = 10  # velocidad a la que se mueve el disparo

        path_disparo = r"Recursos\robotfree\png\Objects\Bullet_000.png"
        self.imagen = pygame.image.load(path_disparo)
        self.imagen = pygame.transform.scale(self.imagen, (10,10))
        self.imagen_volteada = pygame.transform.rotate(self.imagen, 90)

        self.sonido_disparo = pygame.mixer.Sound(r"Recursos\sonidos\corte.wav")

        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        
        self.choco = False

    def mover(self):
        if self.direccion == 'izquierda':
            self.rectangulo.x -= self.velocidad
        elif self.direccion == 'derecha':
            self.rectangulo.x += self.velocidad


    def actualizar(self, pantalla, enemigos, plataformas):
        self.mover()

        ancho = pantalla.get_width()
        if self.rectangulo.x < 0 or self.rectangulo.x > ancho:
            self.choco = True
        else:
            for enemigo in enemigos:
                if self.rectangulo.colliderect(enemigo.rectangulo_principal):
                    self.choco = True
                    enemigo.vida -= 5
                    print(enemigo.vida)

        if self.direccion == 'izquierda':
            pantalla.blit(self.imagen_volteada, self.rectangulo)
        elif self.direccion == 'derecha':
            pantalla.blit(self.imagen, self.rectangulo)
    
        # flag_disparo = True
        # ultimo_disparo = 0

        # if flag_disparo:
        #     tiempo_actual = pygame.time.get_ticks()
        #     if tiempo_actual - ultimo_disparo >= 1000:
        #         self.disparar()
        #         flag_disparo = False
        #         ultimo_disparo = tiempo_actual