idade = int(input('Qual a sua idade '))
if idade >= 18:
    cnh = input('Você tem CNH? (s/n)') 
    if cnh == 's':
        cnh_valida = input('Ela esta valida? (s/n)')
        if cnh_valida == 's':
            print('Você pode dirigir.')
        else:
             print('Você precisa renovar a CNH.')
    else:
        print('Você precisa tirar a CNH para dirigir.')
else:
    print('Você não pode dirigir.')
    tempo_falta= 18 - idade
    if tempo_falta <=2:
        print('Falta pouco para você pode dirigir.')
    else:
        print('vai demorar em fi.')
    if tempo_falta >8:
        print('Vai brincar de Hot Wheels.')
     
