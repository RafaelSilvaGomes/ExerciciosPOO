from calculadora import Calculadora

def main():
    calc = Calculadora()

    print("Bem-vindo à Calculadora Simples!")

    while True:
        print("\nCalculadora")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            valor1 = float(input("Digite o primeiro número: "))
            valor2 = float(input("Digite o segundo número: "))
            resultado = calc.somar(valor1, valor2)
            print(f"Resultado: {resultado}")

        elif escolha == '2':
            valor1 = float(input("Digite o primeiro número: "))
            valor2 = float(input("Digite o segundo número: "))
            resultado = calc.subtrair(valor1, valor2)
            print(f"Resultado: {resultado}")

        elif escolha == '3':
            valor1 = float(input("Digite o primeiro número: "))
            valor2 = float(input("Digite o segundo número: "))
            resultado = calc.multiplicar(valor1, valor2)
            print(f"Resultado: {resultado}")

        elif escolha == '4':
            valor1 = float(input("Digite o primeiro número: "))
            valor2 = float(input("Digite o segundo número: "))
            resultado = calc.dividir(valor1, valor2)
            print(f"Resultado: {resultado}")

        elif escolha == '5':
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()