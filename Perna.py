from Estrutura import *


class Perna:
    def __init__(self, comprimento, largura):
        self.a = Estrutura(comprimento * 0.6, largura)
        self.b = Estrutura(comprimento * 0.75, largura)

        self.a.set_conexao(self.b, 0.0)

    def set_curvatura_perna(self, curvatura):
        self.a.set_angulo(curvatura * 0.9)
        self.b.set_angulo(curvatura * 0.9)

    def desenha_perna(self):
        self.a.desenha_estrutura("perna")

    def curvatura_perna_conexao_a(self, curvatura):
        self.a.set_angulo(curvatura * 0.9)

    def curvatura_perna_conexao_b(self, curvatura):
        self.b.set_angulo(curvatura * 0.9)

    def get_curvatura_perna(self):
        return self.a.get_angulo() * 100 / 90
