soma_idades = 0
quantidade = 0
anos = int(input())

while anos > 0:
    quantidade +=1
    soma_idades += anos
    anos = int(input())
    
soma = soma_idades/quantidade
print(f'{soma:.2f}')
