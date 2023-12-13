import pygame
from pygame.locals import *

from UI.GUI_button import *
from UI.GUI_slider import *
from UI.GUI_textbox import *
from UI.GUI_label import *
from UI.GUI_form import *
from UI.GUI_button_image import *
from GUI_form_menu_score import *
from GUI_form_menu_play import *


    
class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h,
                color_background,
                color_border = "Black",
                border_size = -1,
                active = True):
        
        super().__init__(screen, x, y, w, h,
                        color_background,
                        color_border,
                        border_size,
                        active)

        self.volumen = 0.2
        self.flag_play = True
        
        self.txt_nombre = TextBox(self._slave, 
                                x, y, 50, 50, 150, 50,
                                "grey", "white", "red", "orange", 3,
                                font = "Arial",
                                font_size = 20,
                                font_color = "black")


        

        self.slider_volumen = Slider(self._slave, x, y,
                                    100, 200,
                                    500,15,
                                    self.volumen, "White", "yellow")
        

        porcentaje_volumen = f"{self.volumen * 100}%"
        self.label_volumen = Label(self._slave, 650, 190, 100, 50,
                                    porcentaje_volumen,"Arial", 15, 
                                    "White", r"Recursos\Table.png")
        

        self.boton_play = Button_Image(self._slave, x, y,
                                        455, 100, 50, 50,
                                        r"Recursos\boton_play.png",
                                        self.btn_jugar_click, "")


        self.boton_score = Button_Image(self._slave, x, y,
                                        255, 100, 50, 50,
                                        r"Recursos\Menu_BTN.png",
                                        self.btn_tabla_click, "")
        
        

    
        self.lista_widgets.append(self.txt_nombre)
        self.lista_widgets.append(self.boton_play)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.boton_score)
        self.render()
    
       
    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)     
        else:
            self.hijo.update(lista_eventos)

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
    
    def btn_jugar_click(self, param):
        form_jugar = FormMenuPlay(screen = self._master,
                                  x = self._master.get_width() / 2 - 250,
                                  y = self._master.get_height() / 2 - 250,
                                  w = 500,
                                  h = 500,
                                  color_background = (220, 0, 220),
                                  color_border = (255, 255, 255),
                                  border_size = 1,
                                  active = True, 
                                  path_image = r"Recursos\Window.png")
        self.show_dialog(form_jugar)
        
    
    def btn_play_click(self, param):
        if self.flag_play:
                pygame.mixer.music.pause()
                self._color_background = "Yellow"
                self._color_border = "Blue"
                self.boton_play.set_text("Play")
        else:
                pygame.mixer.music.unpause()
                self._color_background = "Blue"
                self.boton_play.set_text("Pause")
            
        self.flag_play = not self.flag_play
    


    def btn_tabla_click(self, param):
       diccionario = [{"Jugador":"Paulo", "Score": "21"}, 
                      {"Jugador":"Lionel", "Score": "10"},
                      {"Jugador":"Emiliano", "Score": "23"}]
       
       nuevo_form = FormMenuScore(screen = self._master,
                                    x = 70, y = 70,
                                    w = 500, h = 550,
                                    color_background = "yellow",
                                    color_border = "black",
                                    active = True, 
                                    path_image = r"Recursos\Window.png",
                                    scoreboard = diccionario,
                                    margen_y = 100,
                                    margen_x = 10,
                                    espacio = 10)
       self.show_dialog(nuevo_form)