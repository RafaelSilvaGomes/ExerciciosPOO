class ValorContainer:
    def __init__(self, valor):
        self.valor = valor

    def imprimir_valor(self):   
        print(f"O valor armazenado é: {self.valor}")

    @staticmethod
    def trocarValores(ref_a, ref_b):
        temp = ref_a.valor
        ref_a.valor = ref_b.valor
        ref_b.valor = temp
        