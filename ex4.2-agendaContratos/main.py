from contatos import Contato

lista_contatos = []

def adicionar_contatos():
    print("Cadastro de Contatos")
    for i in range(10):
        nome = input("Digite o nome do contato (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        
        novo_contato = Contato(nome, telefone, email)
        lista_contatos.append(novo_contato)

def listar_contatos():
    if not lista_contatos:
        print("Nenhum contato cadastrado.")
    else:
        print("\nLista de Contatos:")
        for contato in lista_contatos:
            print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")

def buscar_contato():
    nome_busca = input("Digite o nome do contato a ser buscado: ")
    for contato in lista_contatos:
        if contato.nome.lower() == nome_busca.lower():
            print(f"Contato encontrado: {contato}")
            return
    print(f"Nenhum contato encontrado com o nome '{nome_busca}'.")

def main():
    adicionar_contatos()
    
    while True:
        print("\nMenu:")
        print("1. Listar contatos")
        print("2. Buscar contato")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            listar_contatos()
        
        elif escolha == '2':
            buscar_contato()
        
        elif escolha == '3':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()