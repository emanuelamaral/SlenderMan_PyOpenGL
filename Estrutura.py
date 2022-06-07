from OpenGL.GLU import *
from mao_testes.main import *

i = 0


class Estrutura:
    angulo = 0.0

    def __init__(self, a, l):
        self.conexao = None
        self.largura = l
        self.altura = a

    def set_conexao(self, estrutura, ang):
        self.conexao = estrutura
        self.angulo = ang

    def set_angulo(self, ang):
        self.angulo = ang

    def get_angulo(self):
        return self.angulo

    def desenha_estrutura(self, tipo="tentaculo"):
        global i
        glPushMatrix()
        glTranslatef(0.0, self.altura/2.0, 0.0)

        if tipo == "perna":
            glPushMatrix()
            glColor3f(0.0, 0.0, 0.0)
            glRotatef(90, 1.0, 0.0, 0.0)
            glScalef(0.47, 0.4, 2.0)
            glTranslatef(0.0, 0.0, -7.5)
            gluCylinder(gluNewQuadric(), 2.0, 2.0, 10, 20, 20)
            glPopMatrix()

        elif tipo == "braco":

            glPushMatrix()
            glColor3f(0.0, 0.0, 0.0)
            glRotatef(90, 1.0, 0.0, 0.0)
            glScalef(0.3, 0.3, 0.32)
            #glScalef(self.largura, self.altura, self.largura)
            #glPushMatrix()
            glTranslatef(0.0, 0.0, -7.5)
            gluCylinder(gluNewQuadric(), 2.0, 2.0, 18, 20, 20)
            #glPopMatrix()
            glPopMatrix()

        else:
            i += 1

            glPushMatrix()
            glColor3f(0.1, 0.1, 0.1)
            glScalef(self.largura, self.altura, self.largura)
            glutSolidCube(self.largura)
            glPopMatrix()

        glTranslatef(0.0, self.altura/2.0, 0.0)

        #glutSolidSphere(0.85 * self.largura, 8, 8)

        if isinstance(self.conexao, Estrutura):
            glRotatef(self.angulo, 1.0, 0.0, 0.0)
            self.conexao.desenha_estrutura(tipo)

        elif self.conexao is None and tipo == "tentaculo":
            glPushMatrix()
            glColor3f(0.0, 0.0, 0.0)
            glTranslatef(0.0, 0.10, 0.0)
            glRotatef(270, 1.0, 0.0, .0)
            glScalef(0.7, 0.7, 2.0)
            glutSolidCone(1.0, 1.0, 40, 40)
            glPopMatrix()

        elif self.conexao is None and tipo == "braco":
            glPushMatrix()
            glColor3f(1.0, 1.0, 1.0)
            glTranslatef(0.0, 0.8, 0.0)
            glRotatef(180, 0.0, 1.0, .0)
            glScalef(0.20, 0.20, 0.20)
            mao_direita = Mao(1.0)
            mao_direita.desenha_mao()


            glPopMatrix()

        glPopMatrix()
