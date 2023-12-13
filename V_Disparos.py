import pygame

# disparar cada 1000 milis

class Disparo:
    def __init__(self, x, y, direccion, path):
        self.direccion = direccion  # para ver de donde y hacia donde va
        self.velocidad = 7          # velocidad a la que se mueve el disparo
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen, (10,10))
        self.imagen_volteada = pygame.transform.rotate(self.imagen, 90)

        self.sonido_disparo = pygame.mixer.Sound(r"Recursos\sonidos\laser-gun-shot.wav")

        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        
        self.choco = False

    def mover(self):
        if self.direccion == 'izquierda':
            self.rectangulo.x -= self.velocidad
        elif self.direccion == 'derecha':
            self.rectangulo.x += self.velocidad


    def actualizar(self, pantalla, enemigos, plataformas, jugador):
        self.mover()

        ancho = pantalla.get_width()
        if self.rectangulo.x < 0 or self.rectangulo.x > ancho:
            self.choco = True
        else:
            for plataforma in plataformas:
                if self.rectangulo.colliderect(plataforma.rectangulo):
                    self.choco = True
            for enemigo in enemigos:
                if self.rectangulo.colliderect(enemigo.rectangulo_principal):
                    self.choco = True
                    enemigo.vida -= 5
                    jugador.puntaje += 1

        if self.direccion == 'izquierda':
            pantalla.blit(self.imagen_volteada, self.rectangulo)
        elif self.direccion == 'derecha':
            pantalla.blit(self.imagen, self.rectangulo)
