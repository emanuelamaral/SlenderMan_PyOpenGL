from Estrutura import *

class Braco:
    def __init__(self, comprimento, largura):
        self.a = Estrutura(comprimento * 0.40, largura)
        self.b = Estrutura(comprimento * 0.45, largura)
        self.c = Estrutura(comprimento * 0.35, largura)

        self.a.set_conexao(self.b, 0.0)
        self.b.set_conexao(self.c, 0.0)

    def set_curvatura_braco(self, curvatura):
        self.a.set_angulo(curvatura * 0.9)
        self.b.set_angulo(curvatura * 0.9)

    def desenha_braco(self):
        self.a.desenha_estrutura("braco")

    def curvatura_braco_conexao_a(self, curvatura):
        self.a.set_angulo(curvatura * 0.9)

    def curvatura_braco_conexao_b(self, curvatura):
        self.b.set_angulo(curvatura * 0.9)

    def get_curvatura_braco(self):
        return self.a.get_angulo() * 100 / 90
