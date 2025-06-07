from somardiagonais import Matriz

def main():
    print("Programa para somar os elementos das diagonais de uma matriz quadrada:")

    try:
        ordem = int(input("Digite a ordem da matriz (número de linhas/colunas): "))

        if ordem <= 0:
            print("A ordem da matriz deve ser maior que zero.")
            return

        matriz = Matriz(ordem)
        matriz.preencher_matriz()

        soma_principal = matriz.somar_diagonal_principal()
        soma_secundaria = matriz.somar_diagonal_secundaria()

        print(f"Soma da diagonal principal: {soma_principal}")
        print(f"Soma da diagonal secundária: {soma_secundaria}")

    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro válido para a ordem da matriz.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()