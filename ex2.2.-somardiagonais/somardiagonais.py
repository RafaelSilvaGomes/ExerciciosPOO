class Matriz:
    def __init__(self, ordem):
        self.ordem = ordem
        self.dados = []

    def preencher_matriz(self):
        for i in range(self.ordem):
            linha = []
            for j in range(self.ordem):
                valor = int(input(f"Digite o elemento [{i}][{j}]: "))
                linha.append(valor)
            self.dados.append(linha)

    def somar_diagonal_principal(self):
        soma = 0
        for i in range(self.ordem):
            soma += self.dados[i][i]
        return soma
    
    def somar_diagonal_secundaria(self):
        soma = 0
        for i in range(self.ordem):
            soma += self.dados[i][self.ordem - 1 - i]
        return soma

