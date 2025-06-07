class Matriz:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

    def preencher_matriz(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                self.matriz[i][j] = int(input(f"Digite o elemento [{i}][{j}]: "))

    def encontrar_maior(self):
        maior = self.matriz[0][0]
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.matriz[i][j] > maior:
                    maior = self.matriz[i][j]
        return maior
    
    def encontrar_menor(self):
        menor = self.matriz[0][0]
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.matriz[i][j] < menor:
                    menor = self.matriz[i][j]
        return menor
        
    