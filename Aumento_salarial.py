class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumento_salario(self, valor):
        self.salario += valor

    def diminui_salario(self, valor):
        self.salario -= valor
        if self.salario < 0:
            self.salario = 0
    
    def mostrar(self):
        print(f'Nome: {self.nome}')
        print(f'Salário: R$ {self.salario:.2f}')
        print('-'*20)

qtd = int(input())
cont = 0
funcionarios = []

while cont < qtd:
    a,b = input().split()
    salario = float(b)
    funcionario = Funcionarios(a, salario)
    funcionarios.append(funcionario)
    cont += 1

while True:
    acon = input().split()
    if acon[0] == 'FIM': break
    valores = float(acon[1])
    nome = acon[2]

    for funcionario in funcionarios:
        if nome == funcionario.nome:
            if acon[0] == 'aumenta':
                funcionario.aumento_salario(valores)
            else:
                funcionario.diminui_salario(valores)

for funcionario in funcionarios:
    funcionario.mostrar()