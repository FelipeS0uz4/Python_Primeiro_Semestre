class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumenta_salario(self, valor):
        self.salario += valor

    def reduz_salario(self, valor):
        if self.salario >= valor:
            self.salario -= valor
        else:
            self.salario = 0


def imprimir_funcionarios(funcionarios):
    for funcionario in funcionarios:
        print(f'Nome: {funcionario.nome}')
        print(f'Salário: R$ {funcionario.salario:.2f}')
        print('-' * 20)



funcionarios = []
n = int(input())

for _ in range(n):
    nome, salario = input().split()
    salario = float(salario)
    funcionario = Funcionario(nome, salario)
    funcionarios.append(funcionario)

while True:
    operacao = input().split()
    if operacao[0] == 'FIM':
        break

    nome_operacao = operacao[2]
    valor = float(operacao[1])

    for funcionario in funcionarios:
        if funcionario.nome == nome_operacao:
            if operacao[0] == 'aumenta':
                funcionario.aumenta_salario(valor)
            elif operacao[0] == 'reduz':
                funcionario.reduz_salario(valor)

imprimir_funcionarios(funcionarios)