from palindromo import Palindromo

def executar():
    palindromo = Palindromo()
    print("Verificador de Palíndromos")
    palavra = input("Digite uma palavra ou frase: ")

    if palindromo.eh_palindromo(palavra):
        print(f"{palavra} é um palíndromo.")
    else:
        print(f"{palavra} não é um palíndromo.")

if __name__ == "__main__":
    executar()