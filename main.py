from movimentacao import *
from SlenderMan import *
from ambiente import *

angx = 0
angy = 0
angz = 0
ang_a = 0
ang_b = 0
zoom = 80
fAspect = 0

i = 0
tempo = 0

slender = Slender(1.0)


def movimento_1_tentaculo(value):
    global tempo

    slender.set_curvatura_tentaculos_z(0, movimento_tentaculo_1[0][tempo])
    slender.set_tentaculo_angulo_a(0, movimento_tentaculo_1[1][tempo])
    slender.set_tentaculo_angulo_b(0, movimento_tentaculo_1[2][tempo])
    # time.sleep(0.13)
    # draw()

    # for tempo in range(0, 17):
    slender.set_curvatura_tentaculos_z(1, movimento_tentaculo_1[0][tempo])
    slender.set_tentaculo_angulo_a(1, movimento_tentaculo_1[1][tempo])
    slender.set_tentaculo_angulo_b(1, movimento_tentaculo_1[2][tempo])
    # time.sleep(0.13)
    # draw()

    # for tempo in range(0, 17):
    slender.set_curvatura_tentaculos_z(2, movimento_tentaculo_1[0][tempo])
    slender.set_tentaculo_angulo_a(2, movimento_tentaculo_1[1][tempo])
    slender.set_tentaculo_angulo_b(2, movimento_tentaculo_1[2][tempo])
    # time.sleep(0.13)
    # draw()

    # for tempo in range(0, 17):
    slender.set_curvatura_tentaculos_z(3, movimento_tentaculo_1[0][tempo])
    slender.set_tentaculo_angulo_a(3, movimento_tentaculo_1[1][tempo])
    slender.set_tentaculo_angulo_b(3, movimento_tentaculo_1[2][tempo])
    # time.sleep(0.13)
    # draw()

    # for tempo in range(0, 17):
    slender.set_curvatura_tentaculos_z(4, movimento_tentaculo_1[0][tempo])
    slender.set_tentaculo_angulo_a(4, movimento_tentaculo_1[1][tempo])
    slender.set_tentaculo_angulo_b(4, movimento_tentaculo_1[2][tempo])
    # time.sleep(0.13)
    # draw()

    # for tempo in range(0, 17):
    slender.set_curvatura_tentaculos_z(5, movimento_tentaculo_1[0][tempo])
    slender.set_tentaculo_angulo_a(5, movimento_tentaculo_1[1][tempo])
    slender.set_tentaculo_angulo_b(5, movimento_tentaculo_1[2][tempo])
    # draw()

    slender.set_curvatura_tentaculos_z(6, movimento_tentaculo_1[0][tempo])
    slender.set_tentaculo_angulo_a(6, movimento_tentaculo_1[1][tempo])
    slender.set_tentaculo_angulo_b(6, movimento_tentaculo_1[2][tempo])
    # desenha()

    slender.set_curvatura_tentaculos_z(7, movimento_tentaculo_1[0][tempo])
    slender.set_tentaculo_angulo_a(7, movimento_tentaculo_1[1][tempo])
    slender.set_tentaculo_angulo_b(7, movimento_tentaculo_1[2][tempo])
    #desenha()

    time.sleep(0.050)
    desenha()
    # glutPostRedisplay()
    if i == 1:
        if tempo <= 15:
            tempo += 1
        else:
            tempo = 0
        glutTimerFunc(40, movimento_1_tentaculo, 1)
    else:
        pass


def background():
    glPushMatrix()
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_id)
    glPushMatrix()

    glRotatef(270, 1.0, 0.0, 0.0)
    glTranslatef(0.0, 0.0, -350.0)
    glScalef(1.0, 1.0, 1.0)

    # desenhar_chao()
    glBegin(GL_QUADS)
    x = 200
    y = 200
    z = 200

    glVertex3f(-x, -y, z)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(x, -y, z)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(x, y, z)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-x, y, z)
    glTexCoord2f(0.0, 1.0)
    glEnd()
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()


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
    #glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, diffuse_light)
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

    #glPushMatrix()
    #background()
    #desenhar_chao()
    desenhar_fundo()
    #glPopMatrix()

    glutSwapBuffers()


def configurar_janela(w, h):
    global fAspect
    glViewport(0, 0, w, h)

    EspecificaParametrosVisualizacao()
    fAspect = int(w / h)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #glTranslatef(0.0, -10.0, -25.0)
    glTranslatef(0.0, -10.0, 55.0)


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
    global angy, angx, angz, ang_a, ang_b, tempo, i

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

    elif tecla == b's':
        i = 1
        glutTimerFunc(40, movimento_1_tentaculo, 1)

    elif tecla == b'S':
        i = 0
        glutTimerFunc(40, movimento_1_tentaculo, 0)

    elif tecla == b'i':
        fuck()

    elif tecla == b'o':
        tchau()

    elif tecla == b'h':
        home_mao()

    elif tecla == b'z':
        glutReshapeWindow(700, 700)

    elif tecla == b'x':
        glutFullScreen()

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
    init()
    glutMainLoop()


main()