from valorContainer import ValorContainer

def main():
    print("Programa para trocar valores entre dois objetos ValorContainer:")

    try:
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))

        obj_a = ValorContainer(valor1)
        obj_b = ValorContainer(valor2)

        print("Valores antes da troca:")
        obj_a.imprimir_valor()
        obj_b.imprimir_valor()

        ValorContainer.trocarValores(obj_a, obj_b)

        print("Valores após a troca:")
        obj_a.imprimir_valor()
        obj_b.imprimir_valor()

    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros válidos.")

if __name__ == "__main__":
    main()