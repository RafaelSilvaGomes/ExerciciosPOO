from palindromo import Palindromo

class Main:
    def __init__(self):
        self.palavra = input("Digite uma palavra ou frase: ")
        self.palindromo = Palindromo(self.palavra)

    def executar(self):
        if self.palindromo.verificar_palindromo():
            print(f"{self.palavra} é um palíndromo.")
        else:
            print(f"{self.palavra} não é um palíndromo.")

if __name__ == "__main__":
    main = Main()
    main.executar()