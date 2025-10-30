n1 = int(input())
n2 = int(input())
numeros = 0
n3 = n1

while n3 <= n2:
    if n3 % 4 == 0 and (n3 % 100 != 0 or n3 % 400 == 0):
        print (f'{n3}')
        numeros += 1
        n3 += 1
    else:
        n3 += 1
     
    
print (f'Bissextos: {numeros}')


ano_inicio = int(input())
ano_fim = int(input())

ano_atual = ano_inicio
qtde_bissextos = 0

while ano_atual <= ano_fim:
    if ano_atual % 4 == 0 and (ano_atual % 100 != 0 or ano_atual % 400 == 0):
        print(ano_atual)
        qtde_bissextos += 1
    ano_atual += 1

print(qtde_bissextos)
