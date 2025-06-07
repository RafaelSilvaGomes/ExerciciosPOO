from fatorial import Fatorial

def executar():
    fatorial = Fatorial()
    print("Calculadora de Fatorial")

    n = int(input("Digite um número inteiro positivo: "))
    resultado = fatorial.calcular(n)
    print(f"O fatorial de {n} é {resultado}")

if __name__ == "__main__":
    executar()