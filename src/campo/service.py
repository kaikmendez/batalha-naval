from math import sqrt

class Campo:
    def __init__(self):
        pass

    def criar_campo(self,quantidade_casas):
        lista = []
        for position in range(1,quantidade_casas+1):
            lista.append(position)
        self.eixos = int(sqrt(quantidade_casas))
        return lista

    def ver_campo(self):
        for eixo_y in range(self.eixos):
            for eixo_x in range(self.eixos):
                print(f' . ',end='')
            print('')





