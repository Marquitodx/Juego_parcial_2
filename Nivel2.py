import pygame
import random
from pygame.locals import *
from V_Player import *
from V_Configuraciones import *
from V_Modo import *
from V_Plataformas import *
from V_Items import *
from V_Listas import *

class Nivel_2:
    def __init__(self, pantalla: pygame.Surface) -> None:
        self._slave = pantalla
        self.ANCHO = pantalla.get_width()
        self.ALTO = pantalla.get_height()

        self.VELOCIDAD_FONDO = 3

        self.tiempo_inicial = pygame.time.get_ticks()
        self.duracion_minutos = 1
        self.duracion_milisegundos = self.duracion_minutos * 60 * 1000
        self.tiempo_transcurrido = 0

        self.paisaje = pygame.image.load(FONDO_MOVIBLE).convert()
        self.x = 0

        self.FONDO = pygame.image.load(FONDO_NIVEL_2).convert_alpha()
        self.FONDO = pygame.transform.scale(self.FONDO, (self.ANCHO, self.ALTO))

        pygame.display.set_caption("Robot vs todo")

        self.icono = pygame.image.load(ICONO_PNG)
        pygame.display.set_icon(self.icono)

        self.FUENTE = pygame.font.Font(FUENTE_TEXTO, 30)
        self.FUENTE_GRANDE = pygame.font.Font(FUENTE_TEXTO, 100)
        self.NEGRO = (0, 0, 0)
        self.BLANCO = (255, 255, 255)
        self.VERDE = (0, 220, 0)
        self.ROJO = (250, 0, 0)

        self.sonidos(MUSICA_NIVEL_2)

        self.jugador = Personaje((70, 70), plataforma1.rectangulo, 5)

        
        self.lista_enemigos = lista_de_enemigos_nivel_2
        self.tiempo_creacion_enemigo = pygame.USEREVENT + 1
        pygame.time.set_timer(self.tiempo_creacion_enemigo, 10000)

        self.plataformas = plataformas_nivel_2
        self.lista_monedas = lista_de_monedas_nivel_2

        tuerca1 = Vida(TUERCA_VIDA, self.ANCHO)
        self.lista_vidas = [tuerca1]

        self.superficie_opaca = pygame.Surface((self.ANCHO, self.ALTO), pygame.SRCALPHA)
        self.superficie_opaca.fill((0, 0, 0, 128))

        self.portal_creado = False

    def update(self, lista_eventos):
        piso_nuevo = random.choice(self.plataformas)
        piso_nuevo = piso_nuevo.rectangulo

        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()

            self.leer_inputs(lista_eventos, self.tiempo_creacion_enemigo, self.lista_enemigos,
                            Enemigo(piso_nuevo), Vida(TUERCA_VIDA, self.ANCHO), self.lista_vidas)

        self.x = self.fondo(self._slave, self.paisaje, self.ANCHO, self.FONDO, self.x)
        self.x -= self.VELOCIDAD_FONDO

        for monedas in self.lista_monedas:
            monedas.actualizar(self._slave)
            monedas.detectar_colision(self.jugador, self.lista_monedas)

        if len(self.lista_monedas) <= 0 and not self.portal_creado:
            self.portal = Portal(lista_imagenes_portal, 400, 160)
            self.portal_creado = True

        if self.portal_creado:
            self.portal.actualizar(self._slave, self.jugador, self.FUENTE_GRANDE,
                                   self.BLANCO, self.VERDE, self.superficie_opaca)

        for enemigo in self.lista_enemigos:
            enemigo.actualizar(self._slave, self.lista_enemigos, self.plataformas, self.jugador)
            enemigo.detectar_colision(self.jugador)

        tiempo_agotado = self.relojes_cronometro(self.tiempo_inicial, self.duracion_milisegundos,
                                                 self.FUENTE, self.NEGRO, self.BLANCO,
                                                 self._slave, self.jugador, self.ANCHO)

        self.jugador.actualizar(self._slave, self.plataformas, self.lista_enemigos, self.jugador,
                                self.FUENTE_GRANDE, self.BLANCO, self.ROJO, self.superficie_opaca, tiempo_agotado)
        self.jugador.detectar_colision(self.lista_enemigos, self.ALTO, piso_nuevo)

        for vida in self.lista_vidas:
            vida.animar(self._slave)
            vida.detectar_colision(self.jugador, self.lista_vidas, self.ALTO)

        if get_mode():
            self.pintar_lineas(self._slave, self.jugador, self.plataformas,
                               self.lista_enemigos, self.lista_monedas)

        pygame.display.flip()

    def sonidos(self, musica):
        pygame.mixer.music.load(musica)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def leer_inputs(self, eventos, tiempo_creacion_enemigo, lista_enemigos,
                    enemigo, vida, lista_vidas):
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                print(evento.pos)
            elif evento.type == tiempo_creacion_enemigo:
                nuevo_enemigo = enemigo
                lista_enemigos.append(nuevo_enemigo)
                nueva_vida = vida
                lista_vidas.append(nueva_vida)

    def fondo(self, pantalla, paisaje, ancho, fondo, x):
        x_relativa = x % paisaje.get_rect().width
        pantalla.blit(paisaje, (x_relativa - paisaje.get_rect().width, 0))
        if x_relativa < ancho:
            pantalla.blit(paisaje, (x_relativa, 0))
        pantalla.blit(fondo, (0, 0))
        return x

    def relojes_cronometro(self, tiempo_inicial, duracion_milisegundos,
                           fuente, negro, blanco, pantalla, jugador,
                           ancho):
        tiempo_agotado = False
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - tiempo_inicial
        segundos_restantes = max((duracion_milisegundos - tiempo_transcurrido) // 1000, 0)

        color_texto = blanco
        color_sombra = negro

        texto_segundos = fuente.render(f"{segundos_restantes}", True, color_texto)
        sombra_segundos = fuente.render(f"{segundos_restantes}", True, color_sombra)

        texto_puntaje = fuente.render(f"Puntaje: {jugador.puntaje}", True, color_texto)
        sombra_texto_puntaje = fuente.render(f"Puntaje: {jugador.puntaje}", True, color_sombra)

        contador_vida = fuente.render(f"Vida: {jugador.vida}", True, color_texto)
        sombra_contador_vida = fuente.render(f"Vida: {jugador.vida}", True, color_sombra)

        if segundos_restantes <= 0:
            tiempo_agotado = True
        else:
            pantalla.blit(sombra_segundos, ((ancho // 2) + 3, 33))
            pantalla.blit(texto_segundos, (ancho // 2, 30))

        pantalla.blit(sombra_texto_puntaje, (33, 33))
        pantalla.blit(texto_puntaje, (30, 30))

        pantalla.blit(sombra_contador_vida, (1033, 33))
        pantalla.blit(contador_vida, (1030, 30))

        return tiempo_agotado

    def pintar_lineas(self, pantalla, personaje, plataformas, enemigos, lista_monedas):
        pygame.draw.rect(pantalla, "blue", personaje.rectangulos["main"], 2)
        pygame.draw.rect(pantalla, "red", personaje.rectangulos["bottom"], 2)
        pygame.draw.rect(pantalla, "red", personaje.rectangulos["top"], 2)
        pygame.draw.rect(pantalla, "red", personaje.rectangulos["right"], 2)
        pygame.draw.rect(pantalla, "red", personaje.rectangulos["left"], 2)

        for plataforma in plataformas:
            pygame.draw.rect(pantalla, "pink", plataforma.rectangulos["main"], 2)
            pygame.draw.rect(pantalla, "magenta", plataforma.rectangulos["bottom"], 2)
            pygame.draw.rect(pantalla, "magenta", plataforma.rectangulos["top"], 2)
            pygame.draw.rect(pantalla, "magenta", plataforma.rectangulos["right"], 2)
            pygame.draw.rect(pantalla, "magenta", plataforma.rectangulos["left"], 2)

        for enemigo in enemigos:
            pygame.draw.rect(pantalla, "orange", enemigo.rectangulo_principal, 3)

        for moneda in lista_monedas:
            pygame.draw.rect(pantalla, "blue", moneda.rectangulo, 2)
