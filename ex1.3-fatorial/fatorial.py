class Fatorial:

    def calcular(self, n):
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos.")
        elif n == 0 or n == 1:
            return 1
        else:
            return n * self.calcular(n - 1)