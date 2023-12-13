import pygame
from pygame.locals import *

from UI.GUI_form import *
from UI.GUI_button_image import *

class FormContenedorNivel(Form):
    def __init__(self, pantalla: pygame.Surface, nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), "White")
        nivel._slave = self._slave
        self.nivel = nivel
        
        self._btn_home = Button_Image(screen = self._slave,
                                master_x = self._x,
                                master_y = self._y,
                                x = self._w - 100,
                                y = self._h - 100,
                                w = 50,
                                h = 50,
                                onclick = self._btn_home_click,
                                onclick_param = "",
                                path_image = r"Recursos\home.png")
        
        self.lista_widgets.append(self._btn_home)


    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()
    
    def _btn_home_click(self, param):
        self.end_dialog()