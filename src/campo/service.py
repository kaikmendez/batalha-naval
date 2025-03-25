from math import isqrt

class Campo:
    def __init__(self):
        self.eixos = 0
        self.lista = []

    def criar_campo(self,quantidade_casas):
        self.lista = [position for position in range(1,quantidade_casas+1)]
        self.eixos = int(isqrt(quantidade_casas))
        return self.lista

    def ver_campo(self):
        if self.eixos * self.eixos != len(self.lista):
            print('O valor inserido não retorna um quadrado perfeito.')
            return
        
        for _ in range(self.eixos):
            for _ in range(self.eixos):
                print(f' . ',end='')
            print('')





