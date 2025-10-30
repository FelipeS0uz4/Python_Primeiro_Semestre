def exibir(a,b,c):
    print(f'EPR: {a}')
    print(f'EHD: {b}')
    print(f'INTRUSOS: {c}')

Numero_alunos= int(input())
EPR = 0
EHD = 0
INTRUSOS = 0
while True:
    try:
        for i in range(Numero_alunos):
            a, b= input().split(' ')
            curso = b
            if curso == 'EPR':
                EPR += 1
            elif curso == 'EHD':
                EHD += 1
            else:
                INTRUSOS += 1
    except:
        break
    exibir(EPR,EHD,INTRUSOS)

