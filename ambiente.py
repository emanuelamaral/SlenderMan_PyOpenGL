from OpenGL.GL import *
import pygame

textura_fundo = textura_chao = 0
texture = []


def configurar_ambiente():

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glEnable(GL_TEXTURE_2D)
    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)


def carregar_textura_fundo():
    global texture

    textura = pygame.image.load("C:\\Users\\amoz_\\PycharmProjects\\OpenGL\\SlenderMan\\images\\background_slender2_2.jpg")
    texture.append(pygame.image.tostring(textura, "RGBA", True))
    width = textura.get_width()
    height = textura.get_height()

    glGenTextures(1, textura_fundo)
    glBindTexture(GL_TEXTURE_2D, textura_fundo)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, texture[0])

    configurar_ambiente()


def carregar_texturas_chao():
    global texture

    textura = pygame.image.load("C:\\Users\\amoz_\\PycharmProjects\\OpenGL\\SlenderMan\\images\\gramado3_slender_2.jpg")
    texture.append(pygame.image.tostring(textura, "RGBA", True))
    width = textura.get_width()
    height = textura.get_height()

    glGenTextures(1, textura_chao)
    glBindTexture(GL_TEXTURE_2D, textura_chao)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, texture[1])

    configurar_ambiente()


def desenhar_chao():
    glPushMatrix()
    carregar_texturas_chao()
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_chao)
    glPushMatrix()

    glRotatef(270, 1.0, 0.0, 0.0)
    glTranslatef(0.0, 0.0, -350.0)
    glScalef(3.0, 3.0, 1.0)

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


def desenhar_fundo():
    glPushMatrix()
    carregar_textura_fundo()
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_fundo)
    glPushMatrix()

    glRotatef(270, 0.0, 0.0, 1.0)
    glTranslatef(0.0, 0.0, -1200.0)
    glScalef(5.0, 5.0, 1.0)

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
