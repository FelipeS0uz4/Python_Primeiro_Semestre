def alfabeto (n):
    X = 'a'
    if n == 1:
        X = 'A'
    elif n == 2:
        X = 'B'
    elif n == 3:
        X = 'C'
    elif n == 4:
        X = 'D'
    elif n == 5:
        X = 'E'
    elif n == 6:
        X = 'F'
    elif n == 7:
        X = 'G'
    elif n == 8:
        X = 'H'
    elif n == 9:
        X = 'I'
    elif n == 10:
        X = 'J'
    elif n == 11:
        X = 'K'
    elif n == 12:
        X = 'L'
    elif n == 13:
        X = 'M'
    elif n == 14:
        X = 'N'
    elif n == 15:
        X = 'O'
    elif n == 16:
        X = 'P'
    elif n == 17:
        X = 'Q'
    elif n == 18:
        X = 'R'
    elif n == 19:
        X = 'S'
    elif n == 20:
        X = 'T'
    elif n == 21:
        X = 'U'
    elif n == 22:
        X = 'V'
    elif n == 23:
        X = 'W'
    elif n == 24:
        X = 'X'
    elif n == 25:
        X = 'Y'
    elif n == 26:
        X = 'Z'
    
    return (X)
num_linhas = int(input())
letra = 1
while letra <= num_linhas:
    contador = 1
    while contador <= letra:
        contador += 1
        print(f'{alfabeto(letra)}', end="")     
    print()
    letra += 1
