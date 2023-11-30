import pygame
from V_Configuraciones import *
from V_Enemigo import *
from V_Items import *
from V_Plataformas import *
from V_Enemigo import Enemigo

# ///////////// Plataformas /////////////
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
piso11 = Plataforma("", 135, 30, 679, 557, False)
piso12 = Plataforma("", 135, 30, 936, 324, False)
piso13 = Plataforma("", 135, 30, 336, 232, False)
piso14 = Plataforma("", 135, 30, 97, 161, False)

plataformas_para_jugador = [piso, piso2, piso3, piso4, piso5, piso6, piso7,
                            piso8, piso9, piso10, piso11, piso12, piso13, piso14]

plataformas_para_enemigos = [piso2, piso3, piso4, piso5,
                            piso6, piso7, piso8, piso9, piso10]


# ///////// Enemigos /////////
enemigo1 = Enemigo(piso10.rectangulo)
enemigo2 = Enemigo(piso4.rectangulo)
enemigo3 = Enemigo(piso2.rectangulo)
enemigo4 = Enemigo(piso5.rectangulo)
enemigo5 = Enemigo(piso7.rectangulo)

lista_de_enemigos = [enemigo1, enemigo2, enemigo3, enemigo4, enemigo5]




# ///////// Monedas /////////

# ----- Bloque 1
m1 = Monedas(primera_lista_monedas, 97, 161)
m2 = Monedas(primera_lista_monedas, 127, 161)
m3 = Monedas(primera_lista_monedas, 157, 161)
m4 = Monedas(primera_lista_monedas, 187, 161)
m5 = Monedas(primera_lista_monedas, 217, 161)

# ----- Bloque 2
m6 = Monedas(segunda_lista_monedas, 336, 232)
m7 = Monedas(segunda_lista_monedas, 366, 232)
m8 = Monedas(segunda_lista_monedas, 396, 232)
m9 = Monedas(segunda_lista_monedas, 426, 232)
m10 = Monedas(segunda_lista_monedas, 456, 232)

# ----- Bloque 3
m11 = Monedas(primera_lista_monedas, 936, 324)
m12 = Monedas(primera_lista_monedas, 966, 324)
m13 = Monedas(primera_lista_monedas, 996, 324)
m14 = Monedas(primera_lista_monedas, 1026, 324)
m15 = Monedas(primera_lista_monedas, 1056, 324)

# ----- Bloque 4
m16 = Monedas(segunda_lista_monedas, 679, 557)
m17 = Monedas(segunda_lista_monedas, 709, 557)
m18 = Monedas(segunda_lista_monedas, 739, 557)
m19 = Monedas(segunda_lista_monedas, 769, 557)
m20 = Monedas(segunda_lista_monedas, 799, 557)

# ----- Bloque 5
m21 = Monedas(primera_lista_monedas, 242, 679)
m22 = Monedas(primera_lista_monedas, 272, 679)
m23 = Monedas(primera_lista_monedas, 302, 679)
m24 = Monedas(primera_lista_monedas, 332, 679)
m25 = Monedas(primera_lista_monedas, 362, 679)
m26 = Monedas(primera_lista_monedas, 392, 679)
m27 = Monedas(primera_lista_monedas, 422, 679)
m28 = Monedas(primera_lista_monedas, 452, 679)
m29 = Monedas(primera_lista_monedas, 482, 679)

# ----- Bloque 6
m30 = Monedas(segunda_lista_monedas, 135, 372)
m31 = Monedas(segunda_lista_monedas, 165, 372)
m32 = Monedas(segunda_lista_monedas, 195, 372)
m33 = Monedas(segunda_lista_monedas, 225, 372)
m34 = Monedas(segunda_lista_monedas, 255, 372)
m35 = Monedas(segunda_lista_monedas, 285, 372)
m36 = Monedas(segunda_lista_monedas, 315, 372)

lista_de_monedas = [m1,  m2,  m3,  m4,  m5,  m6,  m7,  m8,  m9,  m10,
                    m11, m12, m13, m14, m15, m16, m17, m18, m19, m20,
                    m21, m22, m23, m24, m25, m26, m27, m28, m29, m30,
                    m31, m32, m33, m34, m35, m36]