repeticoes = 0
maior_numero = 0
posição = 0


while repeticoes <= 99:
    repeticoes += 1
    n2 = int(input())
    if n2 > maior_numero :
        maior_numero = n2
        posição = repeticoes

print (f'{maior_numero}')
print (f'{posição}')
