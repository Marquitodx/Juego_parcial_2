import pygame
from V_Configuraciones import *
from V_Enemigo import *
from V_Items import *
from V_Plataformas import *
from V_Enemigo import Enemigo

# ········· Plataformas ···········
piso = Plataforma("", 159, 10, 0, 679, False)
piso2 = Plataforma("", 300, 10, 242, 679, False)
piso3 = Plataforma("", 150, 45, 517, 630, False)
piso4 = Plataforma("", 123, 50, 835, 630, False)
piso5 = Plataforma("", 117, 20, 449, 474, False)
piso6 = Plataforma("", 200, 30, 864, 475, False)
piso7 = Plataforma("", 230, 80, 576, 260, False)
piso8 = Plataforma("", 220, 40, 135, 372, False)
piso9 = Plataforma("", 120, 130, 1152, 387, False)
piso10 = Plataforma("", 330, 10, 961, 680, False)

# piso_movible = Plataforma("bardito/bloque.png", 100, 70, 690, 605, True)


# ········· Enemigos ···········
# Moviminetos del enemigo

enemigo1 = Enemigo(piso10.rectangulo)
enemigo2 = Enemigo(piso4.rectangulo)
enemigo3 = Enemigo(piso2.rectangulo)
enemigo4 = Enemigo(piso5.rectangulo)
enemigo5 = Enemigo(piso7.rectangulo)


# @staticmethod
# def crear_lista():   # Como hago para mostrar enemigos aleatoriamente?
#     lista = []
    

    

#     enemigos_info = [
#         {"limite1": , },
#         {"limite1": },
#         {"limite1": 
#         ]

#     for info in enemigos_info:
#         enemigo = Enemigo(dic_enemigo, 
#                         info["limite1"], 
#                         info["limite2"],
#                         info["inicio_x"],
#                         info["inicio_y"])
        
#         lista.append(enemigo)

#     random.shuffle(lista)  # Aleatoriza la lista de enemigos

#     return lista



# ········· Monedas ···········
