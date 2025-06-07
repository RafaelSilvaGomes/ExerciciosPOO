from conversor import ConversorTemperatura

def main():
    conversor = ConversorTemperatura()
    print("Conversor de Temperatura")

    while True:
        print("\nMenu:")
        print("1. Converter Celsius para Fahrenheit")
        print("2. Converter Fahrenheit para Celsius")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = conversor.celsius_para_fahrenheit(celsius)
            print(f"{celsius}°C é igual a {fahrenheit}°F")

        elif escolha == '2':
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = conversor.fahrenheit_para_celsius(fahrenheit)
            print(f"{fahrenheit}°F é igual a {celsius}°C")
        
        elif escolha == '3':
            print("Saindo do conversor.")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()