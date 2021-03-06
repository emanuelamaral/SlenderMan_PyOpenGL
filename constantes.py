# as colunas indicam os tempos
# as linhas indicam a curvatura
# primeiro bloco de 3 linhas seria para o movimento do dedo 0
# segundo bloco de 3 linhas seria para o movimento do dedo 1
# e assim por diante

# [3][17]
mexer_tentaculos = [
    [2, 5, 10, 15, 20, 15, 10, 0, -5, -10, -15, -20, -15, -10, -5, -2, 0],  # setCurvatura
    [0, 15, 30, 45, 60, 45, 30, 15, 0, 15, 30, 45, 60, 45, 30, 15, 0],  # setAnguloA
    [0, -15, -30, -15, 0, 15, 30, 15, 0, -15, -30, -15, 0, 15, 30, 15, 0]]  # setAnguloB

# [1][43]
ataque_tentaculo_par_cima = [
    [0, 0, 0, 0, 0, 2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 75,
     70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 2, 0, 0, 0, 0, 0]]
"""
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 5, 10, 15, 20, 25, 30, 25, 20, 15, 10,
     5, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""

ataque_tentaculo_par_meio = [
    [0, 2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100,
     95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 2, 0]]
"""    
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 55,
     50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 2, 1, 0, 0, 0, 0, 0, 0, 0]]
"""

ataque_tentaculo_par_baixo = [
    [0, 2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100,
     95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 2, 0]]
"""
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 5, 10, 15, 20, 25, 30, 25, 20, 15, 10,
     5, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""


# [2][65]
mexer_tentaculos_par_cima = [[0, 2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 70, 65, 60, 55, 50, 45,
                             40, 35, 30, 25, 20, 15, 10, 5, 2, 0, -2, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50,
                              -55, -60, -65, -70, -75, -70, -65, -60, -55, -50, -45, -40, -35, -30, -25, -20, -15, -10,
                              -5, -2, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0]]


mexer_tentaculos_par_meio = [[0, 2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 70, 65, 60, 55, 50, 45,
                              40, 35, 30, 25, 20, 15, 10, 5, 2, 0, -2, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50,
                              -55, -60, -65, -70, -75, -70, -65, -60, -55, -50, -45, -40, -35, -30, -25, -20, -15, -10,
                              -5, -2, 0],
                             [0, -2, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50, -55, -60, -65, -70, -75, -70, -65,
                              -60, -55, -50, -45, -40, -35, -30, -25, -20, -15, -10, -5, -2, 0, 2, 5, 10, 15, 20, 25,
                              30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15,
                              10, 5, 2, 0]]

mexer_tentaculos_par_baixo = [[0, 2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 70, 65, 60, 55, 50, 45,
                              40, 35, 30, 25, 20, 15, 10, 5, 2, 0, 2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65,
                               70, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 2, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0]]


# [1][23]

abaixa_braco_direto_eixo_z_45 = [[0, -3, -7, -15, -20, -23, -27, -30, -33, -35, -40, -45, -40, -35, -33, -30, -27, -23,
                                  -20, -15, -7, -3, 0]]

gira_e_levanta_braco_direito_eixo_x_90 = [[0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -100, -100, -90, -80,
                                           -70, -60, -50, -40, -30, -20, -10, 0]]

gira_mao = [[0, 0, 0, 0, 0, 0, -10, -25, -40, -65, -80, -90, -80, -65, -40, -25, -10, 0, 0, 0, 0, 0, 0]]

abaixar_braco_direito_eixo_z_45 = [
                                  [0, 3, 7, 15, 20, 23, 27, 30, 33, 35, 40, 50, 40, 35, 33, 30, 27, 23, 20, 15, 7, 3, 0]
                                    ]

abaixar_braco_esquerdo_eixo_z_45 = [[0, -3, -7, -15, -20, -23, -27, -30, -33, -35, -40, -45, -40, -35, -33, -30, -27,
                                     -23, -20, -15, -7, -3, 0]]

# [1][14]
levanta_braco_direito = [[0, -1, -3, -5, -7, -10, -13, -15, 0, 0, 0, 0, 0, 0]]
levanta_braco_esquerdo = [[0, -1, -3, -5, -7, -10, -13, -15, 0, 0, 0, 0, 0, 0]]
girar_curvatura_a_direito = [[0, 10, 15, 20, 25, 30, 0, 0, 0, 0, 0, 0, 0, 0]]


# [2][43]
andar_perna_direita = [[0, -3, -5, -7, -10, -13, -15, -17, -20, -25, -30, -33, -30, -25, -20, -17, -15, -13, -10, -7,
                        -5, -3, 0, 0, 3, 5, 7, 9, 10, 12, 15, 17, 20, 17, 15, 12, 10, 9, 7, 5, 3, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, -5, -7, -9, -11, -13, -15,
                        -17, -19, -21, -23, -21, -19, -17, -15, -13, -11, -9, -7, -5, 0]]

andar_perna_esquerda = [[0, 0, 3, 5, 7, 9, 10, 12, 15, 17, 20, 17, 15, 12, 10, 9, 7, 5, 3, 0, 0, -3, -5, -7, -10, -13,
                         -15, -17, -20, -25, -30, -33, -30, -25, -20, -17, -15, -13, -10, -7, -5, -3, 0],
                        [-2, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -21, -19, -17, -15, -13, -11, -9, -7, -5,
                         -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

andar_braco_direito = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2,
                        -3, -4, -5, -6, -7, -7, -7, -7, -7, -7, -6, -5, -4, -3, -2, -1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -2, -5, -10, -13, -15,
                        -17, -20, -20, -20, -20, -20, -20, -20, -17, -15, -10, -5, -2, -1, 0]]

andar_braco_esquerdo = [[0, -1, -2, -3, -4, -5, -6, -7, -7, -7, -7, -7, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6,
                         7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
                        [0, 1, 2, 5, 10, 13, 15, 17, 20, 20, 20, 20, 20, 20, 20, 17, 15, 13, 10, 5, 2,
                         1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
