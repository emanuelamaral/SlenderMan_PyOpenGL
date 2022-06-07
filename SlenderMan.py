from Tentaculo import *
from Perna import *
from Braco import *

angx = 0
angy = 0
angz = 0
ang_a = 0
ang_b = 0
zoom = 80
fAspect = 0


i = 0
tempo = 0


class Slender:
    curvatura_tentaculo = []
    curvatura_z_tentaculo = []
    curvatura_perna = []
    curvatura_z_perna = []
    curvatura_braco = []
    curvatura_z_braco = []

    def __init__(self, gross):
        self.grossura = gross

        # Tentaculos esquerdo
        self.tentaculo_cima_esquerdo = Tentaculo(8 * self.grossura, self.grossura)
        self.tentaculo_meio_esquerdo = Tentaculo(20 * self.grossura, self.grossura)
        self.tentaculo_meio_esquerdo_2 = Tentaculo(20 * self.grossura, self.grossura)
        self.tentaculo_baixo_esquerdo = Tentaculo(14 * self.grossura, self.grossura)

        # Tentaculos direito
        self.tentaculo_cima_direito = Tentaculo(8 * self.grossura, self.grossura)
        self.tentaculo_meio_direito = Tentaculo(20 * self.grossura, self.grossura)
        self.tentaculo_meio_direito_2 = Tentaculo(20 * self.grossura, self.grossura)
        self.tentaculo_baixo_direito = Tentaculo(14 * self.grossura, self.grossura)

        # Pernas
        self.perna_esquerda = Perna(16 * self.grossura, self.grossura)
        self.perna_direita = Perna(16 * self.grossura, self.grossura)

        # Braços
        self.braco_esquerdo = Braco(10 * self.grossura, self.grossura)
        self.braco_direito = Braco(10 * self.grossura, self.grossura)

        for i in range(0, 9):
            self.curvatura_tentaculo.append(0)
            self.curvatura_z_tentaculo.append(0)

        for i in range(0, 5):
            self.curvatura_perna.append(0)
            self.curvatura_z_perna.append(0)
            self.curvatura_braco.append(0)
            self.curvatura_z_braco.append(0)

    def get_curvatura_tentaculo(self, tentaculo):
        return self.curvatura_tentaculo[tentaculo]

    def get_curvatura_z_tentaculo(self, tentaculo):
        return self.curvatura_z_tentaculo[tentaculo]

    def get_curvatura_perna(self, perna):
        return self.curvatura_perna[perna]

    def get_curvatura_z_perna(self, perna):
        return self.curvatura_z_perna[perna]

    def get_curvatura_braco(self, braco):
        return self.curvatura_braco[braco]

    def get_curvatura_z_braco(self, braco):
        return self.curvatura_z_braco[braco]

    def desenha_tentaculos_esquerdo(self):
        # Tentaculos esquerdos
        ############################################################
        glPushMatrix()
        glTranslatef(-2.75, 8.0 * self.grossura, 0.0)  # posiciona o Tentaculo
        glPushMatrix()
        glColor3f(0.0, 0.0, 0.0)
        #glutSolidSphere(self.grossura, 3, 3)
        glPopMatrix()
        glRotatef(self.curvatura_tentaculo[0] * 0.9, 1.0, 0.0, 0.0)
        glRotatef(self.curvatura_z_tentaculo[0] * 0.9, 0.0, 0.0, 1.0)
        glRotatef(90, 0.0, 0.0, 1.0)  # inicia o Tentaculo deitado
        self.tentaculo_cima_esquerdo.desenha_tentaculo()
        # glRotatef(270, 1.0, 0.0, 0.0)
        # glTranslatef(0.0, 0.0, 5.5)
        # glutSolidCone(0.6, 1.0, 10, 10)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-2.75, 6.0 * self.grossura, 0.0)
        #glutSolidSphere(self.grossura, 3, 3)
        glRotatef(self.curvatura_tentaculo[1] * 0.9, 1.0, 0.0, 0.0)
        glRotatef(self.curvatura_z_tentaculo[1] * 0.9, 0.0, 0.0, 1.0)
        glRotatef(90, 0.0, 0.0, 1.0)
        self.tentaculo_meio_esquerdo.desenha_tentaculo()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-2.75, 4.0 * self.grossura, 0.0)
        #glutSolidSphere(self.grossura, 3, 3)
        glRotatef(self.curvatura_tentaculo[2] * 0.9, 1.0, 0.0, 0.0)
        glRotatef(self.curvatura_z_tentaculo[2] * 0.9, 0.0, 0.0, 1.0)
        glRotatef(90, 0.0, 0.0, 1.0)
        self.tentaculo_meio_esquerdo_2.desenha_tentaculo()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-2.75, 2.0 * self.grossura, 0.0)
        #glutSolidSphere(self.grossura, 3, 3)
        glRotatef(self.curvatura_tentaculo[3] * 0.9, 1.0, 0.0, 0.0)
        glRotatef(self.curvatura_z_tentaculo[3] * 0.9, 0.0, 0.0, 1.0)
        glRotatef(90, 0.0, 0.0, 1.0)
        self.tentaculo_baixo_esquerdo.desenha_tentaculo()
        glPopMatrix()

    def desenha_tentaculos_direito(self):
        # Tentaculos direitos
        #########################################################
        glPushMatrix()
        glTranslatef(2.75, 8.0 * self.grossura, 0.0)  # posiciona o Tentaculo
        #glutSolidSphere(self.grossura, 3, 3)
        glRotatef(self.curvatura_tentaculo[4] * 0.9, 1.0, 0.0, 0.0)
        glRotatef(self.curvatura_z_tentaculo[4] * 0.9, 0.0, 0.0, 1.0)
        glRotatef(270, 0.0, 0.0, 1.0)  # inicia o Tentaculo deitado
        self.tentaculo_cima_direito.desenha_tentaculo()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(2.75, 6.0 * self.grossura, 0.0)
        #glutSolidSphere(self.grossura, 3, 3)
        glRotatef(self.curvatura_tentaculo[5] * 0.9, 1.0, 0.0, 0.0)
        glRotatef(self.curvatura_z_tentaculo[5] * 0.9, 0.0, 0.0, 1.0)
        glRotatef(270, 0.0, 0.0, 1.0)
        self.tentaculo_meio_direito.desenha_tentaculo()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(2.75, 4.0 * self.grossura, 0.0)
        #glutSolidSphere(self.grossura, 3, 3)
        glRotatef(self.curvatura_tentaculo[6] * 0.9, 1.0, 0.0, 0.0)
        glRotatef(self.curvatura_z_tentaculo[6] * 0.9, 0.0, 0.0, 1.0)
        glRotatef(270, 0.0, 0.0, 1.0)
        self.tentaculo_meio_direito_2.desenha_tentaculo()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(2.75, 2.0 * self.grossura, 0.0)
        # glutSolidSphere(self.grossura, 3, 3)
        glRotatef(self.curvatura_tentaculo[7] * 0.9, 1.0, 0.0, 0.0)
        glRotatef(self.curvatura_z_tentaculo[7] * 0.9, 0.0, 0.0, 1.0)
        glRotatef(270, 0.0, 0.0, 1.0)
        self.tentaculo_baixo_direito.desenha_tentaculo()
        glPopMatrix()
        ###############################################################

    def desenha_tronco(self):
        glPushMatrix()
        # glTranslatef(-0.75 * self.grossura, 3.0 * self.grossura, 0.0)
        # glScalef(5.5 * self.grossura, 6.0 * self.grossura, 1.25 * self.grossura)

        # glutSolidCube(1.0)
        glColor3f(0.0, 0.0, 0.0)
        glScalef(2.0, 0.7, 1.2)
        glRotatef(90, 1.0, 0.0, 0.0)
        glTranslatef(0.0, 1.0, -14.0)
        new_quadric = gluNewQuadric()

        gluCylinder(new_quadric, 1.5, 1.5, 17, 40, 20)
        glPopMatrix()

    def desenha_pernas(self):

        # desenha a perna direita
        glPushMatrix()
        # desenha bacia direita
        glPushMatrix()
        glTranslatef(1.45, -2.0, 1.15)
        glRotatef(90, 1.0, 0.0, 0.0)
        glColor3f(0.0, 0.0, 0.0)
        glScalef(0.9, 0.8, 0.7)
        gluCylinder(gluNewQuadric(), 1.75, 0.85, 4, 20, 20)
        glPopMatrix()

        #glutSolidSphere(self.grossura/1.5, 32, 32)
        glTranslatef(1.45, -3.5 * self.grossura, 1.1)
        glRotatef(self.curvatura_perna[0] * 0.9, 1.0, 0.0, 0.0)
        glRotatef(self.curvatura_z_perna[0] * 0.9, 0.0, 0.0, 1.0)
        glRotatef(180, 0.0, 0.0, 1.0)
        self.perna_direita.desenha_perna()
        glPopMatrix()

        # desenha a perna esquerda
        glPushMatrix()

        # desneha bacia esquerda
        glPushMatrix()
        glTranslatef(-1.45, -2.0, 1.15)
        glRotatef(90, 1.0, 0.0, 0.0)
        glColor3f(0.0, 0.0, 0.0)
        glScalef(0.9, 0.8, 0.7)
        gluCylinder(gluNewQuadric(), 1.75, 0.85, 4, 20, 20)
        glPopMatrix()

        glTranslatef(-1.45, -3.5 * self.grossura, 1.1)
        glutSolidSphere(self.grossura / 1.5, 32, 32)
        glRotatef(self.curvatura_perna[1] * 0.9, 1.0, 0.0, 0.0)
        glRotatef(self.curvatura_z_perna[1] * 0.9, 0.0, 0.0, 1.0)
        glRotatef(180, 0.0, 0.0, 1.0)
        self.perna_esquerda.desenha_perna()
        glPopMatrix()

    def desenha_bracos(self):
        # braco esquerdo
        glPushMatrix()
        glTranslatef(-2.75, 7.5 * self.grossura, 1.0)
        # glutSolidSphere(self.grossura, 16, 16)
        glRotatef(self.curvatura_braco[0] * 0.9, 1.0, 0.0, 0.0)
        glRotatef(self.curvatura_z_braco[0] * 0.9, 0.0, 0.0, 1.0)
        glRotatef(135, 0.0, 0.0, 1.0)
        #glRotatef(90, 0.0, 0.0, 1.0)
        self.braco_esquerdo.desenha_braco()
        # glRotatef(self.braco_esquerdo.c, 1.0, 0.0, 0.0)
        glPopMatrix()

        # braco direito
        glPushMatrix()
        glTranslatef(2.75, 7.5 * self.grossura, 1.0)
        # glutSolidSphere(self.grossura, 16, 16)
        glRotatef(self.curvatura_braco[1] * 0.9, 1.0, 0.0, 0.0)
        glRotatef(self.curvatura_z_braco[1] * 0.9, 0.0, 0.0, 1.0)
        glRotatef(220, 0.0, 0.0, 1.0)
        #glRotatef(270, 0.0, 0.0, 1.0)
        self.braco_direito.desenha_braco()
        glPopMatrix()

    def desenha_pescoco(self):

        glPushMatrix()
        glColor3f(0.0, 0.0, 0.0)
        glTranslatef(0.0, 11.0, 1.25)
        glRotatef(90, 1.0, 0.0, 0.0)
        glScalef(1.5, 0.95, 0.85)
        gluCylinder(gluNewQuadric(), 0.75, 2.0, 1.38, 20, 20)
        glPopMatrix()

        glPushMatrix()
        glColor3f(0.0, 0.0, 0.0)
        glTranslatef(0.0, 12.3, 1.0)
        glRotatef(90, 1.0, 0.0, 0.0)
        glScalef(1.0, 0.85, 0.95)
        gluCylinder(gluNewQuadric(), 0.70, 1.25, 1.38, 20, 20)
        glPopMatrix()

    def desenha_cabeca(self):
        glPushMatrix()
        glColor3f(1.0, 1.0, 1.0)
        glTranslatef(0.0, 13.5, 1.0)
        glutSolidSphere(1.5, 16, 16)
        glPopMatrix()

    def desenha_slender(self):
        glPushMatrix()
        glTranslatef(0.0, 6.0 * self.grossura, 0.0)

        self.desenha_tentaculos_esquerdo()
        self.desenha_tentaculos_direito()
        self.desenha_tronco()
        self.desenha_pernas()
        self.desenha_bracos()
        self.desenha_pescoco()
        self.desenha_cabeca()

        glPopMatrix()

    def set_curvatura_tentaculos(self, tentaculo, curv):
        self.curvatura_tentaculo[tentaculo] = curv

        if tentaculo == 0:
            self.tentaculo_cima_esquerdo.set_curvatura_tentaculo(curv)
        elif tentaculo == 1:
            self.tentaculo_meio_esquerdo.set_curvatura_tentaculo(curv)
        elif tentaculo == 2:
            self.tentaculo_baixo_esquerdo.set_curvatura_tentaculo(curv)
        elif tentaculo == 3:
            self.tentaculo_cima_direito.set_curvatura_tentaculo(curv)
        elif tentaculo == 4:
            self.tentaculo_meio_direito.set_curvatura_tentaculo(curv)
        elif tentaculo == 5:
            self.tentaculo_baixo_direito.set_curvatura_tentaculo(curv)

    def set_curvatura_tentaculos_2(self, tentaculo, curv):
        self.curvatura_tentaculo[tentaculo] = curv

    def set_curvatura_tentaculos_z(self, tentaculo, curv):
        self.curvatura_z_tentaculo[tentaculo] = curv

    def set_tentaculo_angulo_a(self, tentaculo, curv):
        if tentaculo == 0:
            self.tentaculo_cima_esquerdo.curvatura_tentaculo_conexao_a(curv)
        elif tentaculo == 1:
            self.tentaculo_meio_esquerdo.curvatura_tentaculo_conexao_a(curv)
        elif tentaculo == 2:
            self.tentaculo_baixo_esquerdo.curvatura_tentaculo_conexao_a(curv)
        elif tentaculo == 3:
            self.tentaculo_cima_direito.curvatura_tentaculo_conexao_a(curv)
        elif tentaculo == 4:
            self.tentaculo_meio_direito.curvatura_tentaculo_conexao_a(curv)
        elif tentaculo == 5:
            self.tentaculo_baixo_direito.curvatura_tentaculo_conexao_a(curv)

    def set_tentaculo_angulo_b(self, tentaculo, curv):
        if tentaculo == 0:
            self.tentaculo_cima_esquerdo.curvatura_tentaculo_conexao_b(curv)
        elif tentaculo == 1:
            self.tentaculo_meio_esquerdo.curvatura_tentaculo_conexao_b(curv)
        elif tentaculo == 2:
            self.tentaculo_baixo_esquerdo.curvatura_tentaculo_conexao_b(curv)
        elif tentaculo == 3:
            self.tentaculo_cima_direito.curvatura_tentaculo_conexao_b(curv)
        elif tentaculo == 4:
            self.tentaculo_meio_direito.curvatura_tentaculo_conexao_b(curv)
        elif tentaculo == 5:
            self.tentaculo_baixo_direito.curvatura_tentaculo_conexao_b(curv)

