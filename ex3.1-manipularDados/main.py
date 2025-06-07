from numero import Numero

def main():
    print("Programa para manipular números:")

    numero = Numero(10)
    numero.imprimir_valor()

    numero.valor = 20
    numero.imprimir_valor()

    print(f"Objeto 'numero' criado no endereço de memória: {id(numero)}")

if __name__ == "__main__":
    main()
