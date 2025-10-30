def primo(n):
    if n < 2: 
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

entrada = int(input())

for i in range (entrada):
    numeros = int(input())
    if primo(numeros) == True:
        print(f'{numeros} eh primo')
    else:
        print(f'{numeros} nao eh primo')