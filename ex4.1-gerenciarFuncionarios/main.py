from funcionarios import Funcionario

lista_funcionarios = []

def cadastrar_funcionarios():
    print("Cadastro de Funcionários")
    while True:
        nome = input("Digite o nome do funcionário (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        try:
            id = int(input("Digite o ID do funcionário: "))
            salario = float(input("Digite o salário do funcionário: "))
            departamento = input("Digite o departamento do funcionário: ")
            
            novo_funcionario = Funcionario(nome, id, salario, departamento)
            lista_funcionarios.append(novo_funcionario)

        except ValueError:
            print("Entrada inválida. Por favor, insira valores válidos.")

def exibir_salarios():
    buscar_departamento = input("Digite o nome do departamento: ")
    soma = 0.0
    encontrados = 0

    for funcionario in lista_funcionarios:
        if funcionario.departamento.lower() == buscar_departamento.lower():
            print(f"Funcionário: {funcionario.nome}, Salário: {funcionario.salario}")
            soma += funcionario.salario
            encontrados += 1
    
    if encontrados > 0:
        print(f"Soma dos salários do departamento '{buscar_departamento}': {soma}")
    else:
        print(f"Nenhum funcionário encontrado no departamento '{buscar_departamento}'.")
    
def exibir_funcionarios():
    if not lista_funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        print("\nLista de Funcionários:")
        for funcionario in lista_funcionarios:
            print(f"Nome: {funcionario.nome}, ID: {funcionario.id}, Salário: {funcionario.salario}, Departamento: {funcionario.departamento}")
    
def main():
    cadastrar_funcionarios()
    
    while True:
        print("\nMenu:")
        print("1. Exibir salários de um departamento")
        print("2. Exibir todos os funcionários")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            exibir_salarios()
        
        elif escolha == '2':
            exibir_funcionarios()
        
        elif escolha == '3':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida, tente novamente.")
    
if __name__ == "__main__":
    main()