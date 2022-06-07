# as colunas indicam os tempos
# as linhas indicam a curvatura
# primeiro bloco de 3 linhas seria para o movimento do dedo 0
# segundo bloco de 3 linhas seria para o movimento do dedo 1
# e assim por diante
movimento_tentaculo_1 = [
                        [2, 5, 10, 15, 20, 15, 10, 0, -5, -10, -15, -20, -15, -10, -5, -2, 0],  # setCurvatura dedo[0]
                        [0, 15, 30, 45, 60, 45, 30, 15, 0, 15, 30, 45, 60, 45, 30, 15, 0],  # setAnguloA dedo[0]
                        [0, -15, -30, -15, 0, 15, 30, 15, 0, -15, -30, -15, 0, 15, 30, 15, 0]]  # setAnguloB dedo[0]

# 11
matriz_dedo_z = [[0, 15, 30, 45, 60, 75, 60, 45, 30, 15, 0]]

matriz_dedo_anelar = [[0, 15, 30, 60, 90, 60, 30, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# movimentação da perna é somente a curvatura e angulo A