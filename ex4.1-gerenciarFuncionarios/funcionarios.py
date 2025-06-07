class Funcionario:
    def __init__(self, nome, id, salario, departamento):
        self.nome = nome
        self.id = id
        self.salario = salario
        self.departamento = departamento

    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.id}, Salário: {self.salario}, Departamento: {self.departamento}"

    def exibir_funcionarios(self):
        print("\nLista de Funcionários:")
        for funcionario in self.funcionarios:
            print(f"Nome: {funcionario.nome}, ID: {funcionario.id}, Salário: {funcionario.salario}, Departamento: {funcionario.departamento}")
    