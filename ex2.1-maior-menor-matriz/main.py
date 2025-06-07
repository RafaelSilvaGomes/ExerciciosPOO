from encontrar_maior_menor import Matriz


def main():
    print("Programa para encontrar o maior e o menor número da matriz:")

    try:
        linhas = int(input("Digite o número de linhas da matriz: "))
        colunas = int(input("Digite o número de colunas da matriz: "))

        if linhas <= 0 or colunas <= 0:
            print("O número de linhas e colunas deve ser maior que zero.")
            return

        matriz = Matriz(linhas, colunas)
        matriz.preencher_matriz()

        maior = matriz.encontrar_maior()
        menor = matriz.encontrar_menor()

        print(f"O maior número da matriz é: {maior}")
        print(f"O menor número da matriz é: {menor}")

    except ValueError:
        print(
            "Entrada inválida. Por favor, insira números inteiros válidos para linhas e colunas.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
