import pygame, random
from V_Configuraciones import *
from V_Enemigo import Enemigo
from V_Items import *
from V_Plataformas import *




''' -----------------------------------------------------------------------
----------------------  P L A T A F O R M A S  ----------------------------
------------------------------------------------------------------------ '''

piso1  = Plataforma("", 159, 10,  0,    679, False)
piso2  = Plataforma("", 300, 10,  242,  679, False)
piso3  = Plataforma("", 150, 45,  517,  630, False)
piso4  = Plataforma("", 123, 50,  835,  630, False)
piso5  = Plataforma("", 117, 20,  449,  474, False)
piso6  = Plataforma("", 200, 30,  864,  475, False)
piso7  = Plataforma("", 230, 80,  576,  260, False)
piso8  = Plataforma("", 220, 40,  135,  372, False)
piso9  = Plataforma("", 120, 130, 1152, 387, False)
piso10 = Plataforma("", 330, 10,  961,  680, False)
piso11 = Plataforma("", 135, 30,  679,  557, False)
piso12 = Plataforma("", 135, 30,  936,  324, False)
piso13 = Plataforma("", 135, 30,  336,  232, False)
piso14 = Plataforma("", 135, 30,  97,   161, False)

plataformas_nivel_1 = [piso1,   piso2,  piso3,  piso4, piso5, 
                      piso6,  piso7,  piso8,  piso9, piso10,
                      piso11, piso12, piso13, piso14
                      ]


plataforma1  = Plataforma("", 230, 30, 82,  593, False)
plataforma2  = Plataforma("", 115, 30, 414, 532, False)
plataforma3  = Plataforma("", 165, 30, 648, 607, False)
plataforma4  = Plataforma("", 300, 40, 936, 543, False)
plataforma5  = Plataforma("", 227, 30, 978, 381, False)
plataforma6  = Plataforma("", 145, 20, 676, 456, False)
plataforma7  = Plataforma("", 130, 30, 423, 363, False)
plataforma8  = Plataforma("", 230, 30, 47,  398, False)
plataforma9  = Plataforma("", 140, 30, 126, 216, False)
plataforma10 = Plataforma("", 112, 30, 659, 260, False)
plataforma11 = Plataforma("", 330, 30, 831, 159, False)

plataformas_nivel_2 =  [plataforma1, plataforma2, plataforma3, 
                        plataforma4, plataforma5, plataforma6, 
                        plataforma7, plataforma8, plataforma9, 
                        plataforma10, plataforma11]





''' -----------------------------------------------------------------------
----------------------  E N E M I G O S  ----------------------------------
------------------------------------------------------------------------ '''

plataformas_para_enemigos_nivel_1 = [piso2, piso3, piso4, piso5,
                                    piso6, piso7, piso8, piso9, piso10]


primer_piso_enemigo_nivel_1 = random.choice(plataformas_para_enemigos_nivel_1)
primer_piso_enemigo_nivel_1 = primer_piso_enemigo_nivel_1.rectangulo

enemigo1_nivel1 = Enemigo(primer_piso_enemigo_nivel_1)
lista_de_enemigos_nivel_1 = [enemigo1_nivel1]



primer_piso_enemigo_nivel_2 = random.choice(plataformas_nivel_2)
primer_piso_enemigo_nivel_2 = primer_piso_enemigo_nivel_2.rectangulo

enemigo1_nivel2 = Enemigo(primer_piso_enemigo_nivel_2)
lista_de_enemigos_nivel_2 = [enemigo1_nivel2]







''' -----------------------------------------------------------------------
----------------------  M O N E D A S  ------------------------------------
------------------------------------------------------------------------ '''

# ----- Bloque 1
m1 = Monedas(primera_lista_monedas, 97, 161)
m2 = Monedas(primera_lista_monedas, 127, 161)
m3 = Monedas(primera_lista_monedas, 157, 161)
m4 = Monedas(primera_lista_monedas, 187, 161)
m5 = Monedas(primera_lista_monedas, 217, 161)

# ----- Bloque 2
m6  = Monedas(segunda_lista_monedas, 336, 232)
m7  = Monedas(segunda_lista_monedas, 366, 232)
m8  = Monedas(segunda_lista_monedas, 396, 232)
m9  = Monedas(segunda_lista_monedas, 426, 232)
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

lista_de_monedas_nivel_1 = [m1,  m2,  m3,  m4,  m5,  m6,  m7,  m8,  m9, m10,
                            m11, m12, m13, m14, m15, m16, m17, m18, m19, m20,
                            m21, m22, m23, m24, m25, m26, m27, m28, m29, m30,
                            m31, m32, m33, m34, m35, m36]


# ----- Plataforma 2 (referencia)
m37 = Monedas(primera_lista_monedas, 414, 532)
m38 = Monedas(primera_lista_monedas, 444, 532)
m39 = Monedas(primera_lista_monedas, 474, 532)
m40 = Monedas(primera_lista_monedas, 504, 532)
m41 = Monedas(primera_lista_monedas, 534, 532)
m88 = Monedas(primera_lista_monedas, 564, 532)
m89 = Monedas(primera_lista_monedas, 594, 532)


# ----- Plataforma 4 (referencia)
m42 = Monedas(segunda_lista_monedas, 936 , 543)
m43 = Monedas(segunda_lista_monedas, 966 , 543)
m44 = Monedas(segunda_lista_monedas, 996 , 543)
m45 = Monedas(segunda_lista_monedas, 1026, 543)
m46 = Monedas(segunda_lista_monedas, 1056, 543)
m86 = Monedas(segunda_lista_monedas, 1086, 543)
m87 = Monedas(segunda_lista_monedas, 1116, 543)


# ----- Plataforma 6 (referencia)
m47 = Monedas(primera_lista_monedas, 676, 456)
m48 = Monedas(primera_lista_monedas, 706, 456)
m49 = Monedas(primera_lista_monedas, 736, 456)
m50 = Monedas(primera_lista_monedas, 766, 456)
m51 = Monedas(primera_lista_monedas, 796, 456)


# ----- Plataforma 8 (referencia)
m52 = Monedas(segunda_lista_monedas, 47 , 398)
m53 = Monedas(segunda_lista_monedas, 77 , 398)
m54 = Monedas(segunda_lista_monedas, 107, 398)
m55 = Monedas(segunda_lista_monedas, 137, 398)
m56 = Monedas(segunda_lista_monedas, 167, 398)
m83 = Monedas(segunda_lista_monedas, 197, 398)
m84 = Monedas(segunda_lista_monedas, 227, 398)
m85 = Monedas(segunda_lista_monedas, 257, 398)

# ----- Plataforma 10 (referencia)
m57 = Monedas(primera_lista_monedas, 659,  260)
m58 = Monedas(primera_lista_monedas, 689,  260)
m59 = Monedas(primera_lista_monedas, 719,  260)
m60 = Monedas(primera_lista_monedas, 749,  260)


# ----- Plataforma 11 (referencia)
m66 = Monedas(segunda_lista_monedas, 831 , 159)
m67 = Monedas(segunda_lista_monedas, 861 , 159)
m68 = Monedas(segunda_lista_monedas, 891 , 159)
m69 = Monedas(segunda_lista_monedas, 921 , 159)
m70 = Monedas(segunda_lista_monedas, 951 , 159)
m71 = Monedas(segunda_lista_monedas, 981 , 159)
m72 = Monedas(segunda_lista_monedas, 1011, 159)
m80 = Monedas(segunda_lista_monedas, 1041, 159)
m81 = Monedas(segunda_lista_monedas, 1071, 159)
m82 = Monedas(segunda_lista_monedas, 1101, 159)


m73 = Monedas(primera_lista_monedas,  978, 381)
m74 = Monedas(primera_lista_monedas, 1008, 381)
m75 = Monedas(primera_lista_monedas, 1038, 381)
m76 = Monedas(primera_lista_monedas, 1068, 381)
m77 = Monedas(primera_lista_monedas, 1098, 381)
m78 = Monedas(primera_lista_monedas, 1128, 381)
m79 = Monedas(primera_lista_monedas, 1158, 381)

lista_de_monedas_nivel_2 = [m37, m38, m39, m40, m41, m42, m43, m44, m45, m46, 
                           m47, m48, m49, m50, m51, m52, m53, m54, m55, m56,
                           m57, m58, m59, m60, m66, m67, m68, m69, m70, m71,
                           m72, m73, m74, m75, m76, m77, m78, m79, m80, m81,
                           m82, m83, m84, m85, m86, m87, m88]