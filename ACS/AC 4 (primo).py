def primo(n):
    if n < 2: 
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

inicio = int(input())
fim = int(input())
repeticao = 0
for n in range (inicio, fim+1):
    if primo(n):
        print(n)
        repeticao += 1
print(f'primos: {repeticao}')
