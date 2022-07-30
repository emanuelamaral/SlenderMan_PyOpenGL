from constantes import *
from SlenderMan import *
from ambiente import *


# seta os parametros de vizualição
angx = 0
angy = 0
angz = 0
ang_a = 0
ang_b = 0
zoom = 80
fAspect = 0
z = z_1 = 0

# na hora de parar uma movitação nao interferir nas outras
i = h = j = k = l = 0

# seta tempos diferentes para cada movimentação
tempo_tentaculos = tempo_braco_fuck = tempo_braco_xoinha = 0
tempo_andar_perna = tempo_tentaculos_2 = tempo_ataque = 0


slender = Slender(1.0)


def movimento_1_tentaculo(value):
    global tempo_tentaculos

    slender.set_curvatura_tentaculos_z(0, mexer_tentaculos[0][tempo_tentaculos])
    slender.set_tentaculo_angulo_a(0, mexer_tentaculos[1][tempo_tentaculos])
    slender.set_tentaculo_angulo_b(0, mexer_tentaculos[2][tempo_tentaculos])

    slender.set_curvatura_tentaculos_z(1, mexer_tentaculos[0][tempo_tentaculos])
    slender.set_tentaculo_angulo_a(1, mexer_tentaculos[1][tempo_tentaculos])
    slender.set_tentaculo_angulo_b(1, mexer_tentaculos[2][tempo_tentaculos])

    slender.set_curvatura_tentaculos_z(2, mexer_tentaculos[0][tempo_tentaculos])
    slender.set_tentaculo_angulo_a(2, mexer_tentaculos[1][tempo_tentaculos])
    slender.set_tentaculo_angulo_b(2, mexer_tentaculos[2][tempo_tentaculos])

    slender.set_curvatura_tentaculos_z(3, mexer_tentaculos[0][tempo_tentaculos])
    slender.set_tentaculo_angulo_a(3, mexer_tentaculos[1][tempo_tentaculos])
    slender.set_tentaculo_angulo_b(3, mexer_tentaculos[2][tempo_tentaculos])

    slender.set_curvatura_tentaculos_z(4, mexer_tentaculos[0][tempo_tentaculos])
    slender.set_tentaculo_angulo_a(4, mexer_tentaculos[1][tempo_tentaculos])
    slender.set_tentaculo_angulo_b(4, mexer_tentaculos[2][tempo_tentaculos])

    slender.set_curvatura_tentaculos_z(5, mexer_tentaculos[0][tempo_tentaculos])
    slender.set_tentaculo_angulo_a(5, mexer_tentaculos[1][tempo_tentaculos])
    slender.set_tentaculo_angulo_b(5, mexer_tentaculos[2][tempo_tentaculos])

    slender.set_curvatura_tentaculos_z(6, mexer_tentaculos[0][tempo_tentaculos])
    slender.set_tentaculo_angulo_a(6, mexer_tentaculos[1][tempo_tentaculos])
    slender.set_tentaculo_angulo_b(6, mexer_tentaculos[2][tempo_tentaculos])

    slender.set_curvatura_tentaculos_z(7, mexer_tentaculos[0][tempo_tentaculos])
    slender.set_tentaculo_angulo_a(7, mexer_tentaculos[1][tempo_tentaculos])
    slender.set_tentaculo_angulo_b(7, mexer_tentaculos[2][tempo_tentaculos])

    desenha()

    if i == 1:
        if tempo_tentaculos <= 15:
            tempo_tentaculos += 1
        else:
            tempo_tentaculos = 0

        glutTimerFunc(73, movimento_1_tentaculo, 1)

    else:
        pass


def movimento_2_tentaculo(value):
    global tempo_ataque

    # pares de cima
    slender.set_tentaculo_angulo_a(0, ataque_tentaculo_par_cima[0][tempo_ataque])
    slender.set_tentaculo_angulo_a(4, ataque_tentaculo_par_cima[0][tempo_ataque])

    # pares do meio
    slender.set_tentaculo_angulo_a(1, ataque_tentaculo_par_meio[0][tempo_ataque])
    slender.set_tentaculo_angulo_a(2, ataque_tentaculo_par_meio[0][tempo_ataque])
    slender.set_tentaculo_angulo_a(5, ataque_tentaculo_par_meio[0][tempo_ataque])
    slender.set_tentaculo_angulo_a(6, ataque_tentaculo_par_meio[0][tempo_ataque])

    # pares de baixo
    slender.set_tentaculo_angulo_a(3, ataque_tentaculo_par_baixo[0][tempo_ataque])
    slender.set_tentaculo_angulo_a(7, ataque_tentaculo_par_baixo[0][tempo_ataque])

    desenha()

    if j == 1:
        if tempo_ataque <= 41:
            tempo_ataque += 1
        else:
            tempo_ataque = 0

        glutTimerFunc(15, movimento_2_tentaculo, 1)

    else:
        pass


def movimento_3_tentaculo(value):
    global tempo_tentaculos_2

    # par de cima
    slender.set_curvatura_tentaculos(0, mexer_tentaculos_par_cima[0][tempo_tentaculos_2])
    slender.set_curvatura_tentaculos(4, mexer_tentaculos_par_cima[0][tempo_tentaculos_2])

    # pares do meio
    slender.set_tentaculo_angulo_a(1, mexer_tentaculos_par_meio[1][tempo_tentaculos_2])
    slender.set_tentaculo_angulo_a(2, mexer_tentaculos_par_meio[0][tempo_tentaculos_2])
    slender.set_tentaculo_angulo_a(5, mexer_tentaculos_par_meio[1][tempo_tentaculos_2])
    slender.set_tentaculo_angulo_a(6, mexer_tentaculos_par_meio[0][tempo_tentaculos_2])

    # par de baixo
    slender.set_tentaculo_angulo_a(3, mexer_tentaculos_par_baixo[0][tempo_tentaculos_2])
    slender.set_tentaculo_angulo_a(7, mexer_tentaculos_par_baixo[0][tempo_tentaculos_2])

    desenha()
    if k == 1:
        if tempo_tentaculos_2 <= 63:
            tempo_tentaculos_2 += 1
        else:
            tempo_tentaculos_2 = 0

        glutTimerFunc(40, movimento_3_tentaculo, 1)

    else:
        pass


def fuck_braco_levantado(value):
    global tempo_braco_fuck

    slender.set_curvatura_bracos_2(0, gira_e_levanta_braco_direito_eixo_x_90[0][tempo_braco_fuck])
    slender.set_braco_angulo_b(0, gira_mao[0][tempo_braco_fuck])

    desenha()

    if l == 1:
        if tempo_braco_fuck <= 21:
            tempo_braco_fuck += 1
            if tempo_braco_fuck == 12:
                time.sleep(1.5)
            if tempo_braco_fuck == 22:
                home_mao()

        glutTimerFunc(40, fuck_braco_levantado, 1)
    else:
        pass


def andar_pernas(value):
    global tempo_andar_perna

    slender.set_curvatura_pernas_2(0, andar_perna_direita[0][tempo_andar_perna])
    slender.set_curvatura_bracos_2(0, andar_braco_direito[0][tempo_andar_perna])
    slender.set_braco_angulo_a(0, andar_braco_direito[1][tempo_andar_perna])
    slender.set_perna_angulo_a(0, andar_perna_direita[1][tempo_andar_perna])

    slender.set_curvatura_pernas_2(1, andar_perna_esquerda[0][tempo_andar_perna])
    slender.set_curvatura_bracos_2(1, andar_braco_esquerdo[0][tempo_andar_perna])
    slender.set_perna_angulo_a(1, andar_perna_esquerda[1][tempo_andar_perna])
    slender.set_braco_angulo_a(1, andar_braco_esquerdo[1][tempo_andar_perna])

    desenha()

    if h == 1:
        if tempo_andar_perna <= 41:
            tempo_andar_perna += 1
        else:
            tempo_andar_perna = 0
        glutTimerFunc(40, andar_pernas, 1)
    else:
        pass

def init():
    glutReshapeWindow(1080, 720)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)


def configura_iluminacao():
    diffuse_light = [1.0, 1.0, 1.0, 0.0]
    ambient_light = [0.4, 0.4, 0.4, 1.0]
    light_pos = [350.0, 350.0, -350.0, 1.0]
    glEnable(GL_LIGHTING)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)
    glLightfv(GL_LIGHT0, GL_SPECULAR, diffuse_light)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColor3f(1.0, 1.0, 1.0)
    glMateriali(GL_FRONT_AND_BACK, GL_SHININESS, 50)


def configura_slender():
    glPushMatrix()
    # glTranslatef(-35.0, 0.0, -75.0)
    glTranslatef(0.0, 0.0, -75.0)
    # glScalef(1.0, 1.5, 1.5)
    glRotatef(angx, 1.0, 0.0, 0.0)
    glRotatef(angy, 0.0, 1.0, 0.0)
    glRotatef(angz, 0.0, 0.0, 1.0)
    glColor3f(1.0, 0.8, 0)
    slender.desenha_slender()
    glPopMatrix()


def desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    configura_iluminacao()
    configura_slender()
    desenhar_fundo()
    desenhar_chao()

    glutSwapBuffers()


def configurar_janela(w, h):
    global fAspect
    glViewport(0, 0, w, h)

    EspecificaParametrosVisualizacao()
    fAspect = int(w / h)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #glTranslatef(0.0, -10.0, -25.0)
    glTranslatef(0.0, -10.0, 40.0)


def EspecificaParametrosVisualizacao():
    global fAspect, zoom

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(zoom, fAspect, 0.5, 1500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 10.0, 120.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
    glLoadIdentity()
    glTranslatef(0.0, -10.0, -15.0)


def gerencia_mouse(button, state, x, y):
    global zoom

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            if zoom >= 10:
                zoom -= 5

    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            if zoom <= 110:
                zoom += 5

    EspecificaParametrosVisualizacao()
    glutPostRedisplay()


def eventos_teclado(tecla, x, y):
    global angy, angx, angz, ang_a, ang_b, i, h, j, k, l, g, tempo_braco_fuck, tempo_braco_xoinha

    if tecla == b'.':
        angy += 5
        if angy > 360:
            angy -= 360

    elif tecla == b',':
        angy -= 5
        if angy < 0:
            angy += 360

    elif tecla == b']':
        angx += 5
        if angx > 360:
            angx -= 360

    elif tecla == b'[':
        angx -= 2
        if angx < 0:
            angx += 360

    elif tecla == b'-':
        angz += 5
        if angz > 360:
            angz -= 360

    elif tecla == b'=':
        angz -= 5
        if angz < 0:
            angz += 360

    elif tecla == b'q':
        i = 1
        glutTimerFunc(75, movimento_1_tentaculo, 1)

    elif tecla == b'Q':
        i = 0
        glutTimerFunc(0, movimento_1_tentaculo, 0)

    elif tecla == b'w':
        j = 1
        glutTimerFunc(15, movimento_2_tentaculo, 1)

    elif tecla == b'W':
        j = 0
        glutTimerFunc(0, movimento_2_tentaculo, 0)

    elif tecla == b'e':
        k = 1
        glutTimerFunc(40, movimento_3_tentaculo, 1)

    elif tecla == b'E':
        k = 0
        glutTimerFunc(40, movimento_3_tentaculo, 0)

    elif tecla == b'a':
        l = 1
        glutTimerFunc(40, fuck_braco_levantado, 1)
        fuck()

    elif tecla == b'A':
        l = 0
        tempo_braco_fuck = 0
        glutTimerFunc(0, fuck_braco_levantado, 0)
        home_mao()

    elif tecla == b's':
        h = 1
        glutTimerFunc(40, andar_pernas, 1)

    elif tecla == b'S':
        h = 0
        glutTimerFunc(40, andar_pernas, 0)

    elif tecla == b'd':
        h = 1
        fechar_mao(True)
        glutTimerFunc(40, andar_pernas, 1)

    elif tecla == b'D':
        h = 0
        glutTimerFunc(0, andar_pernas, 0)
        home_mao()

    elif tecla == b'z':
        glutReshapeWindow(700, 700)

    elif tecla == b'x':
        glutFullScreen()

    glutPostRedisplay()


def teclas_especiais(tecla, x, y):
    global z, z_1, angy

    if tecla == GLUT_KEY_UP:
        z -= 0.03
        glTranslatef(0.0, 0.0, z)
        glutPostRedisplay()

    elif tecla == GLUT_KEY_DOWN:
        z_1 += 0.03
        glTranslatef(0.0, 0.0, z_1)
        glutPostRedisplay()

    elif tecla == GLUT_KEY_LEFT:
        angy -= 5
        if angy < 0:
            angy += 360
        glutPostRedisplay()

    elif tecla == GLUT_KEY_RIGHT:
        angy += 5
        if angy > 360:
            angy -= 360
        glutPostRedisplay()


def movimento_mouse(x, y):
    print("[{}, {}]".format(x, y))


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutCreateWindow("SlenderMan")
    glutDisplayFunc(desenha)
    glutKeyboardFunc(eventos_teclado)
    glutPassiveMotionFunc(movimento_mouse)
    glutReshapeFunc(configurar_janela)
    glutMouseFunc(gerencia_mouse)
    glutSpecialFunc(teclas_especiais)
    init()
    glutMainLoop()


main()
