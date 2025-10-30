def exibe (noiva, noivo):
    print('-'*20)
    print('LISTA FINAL')
    print('-'*20)
    if noivo and noiva:
        Lista = sorted(noivo | noiva)
        for nome in Lista:
            print(nome)
        print()
    else:
        print()

    print('-'*20)
    print('APENAS NOIVA')
    print('-'*20)
    if noiva:
        Lista_Noiva = sorted(noiva- noivo)
        for nome in Lista_Noiva:
            print(nome)
        print()
    else:
        print()

    print('-'*20)
    print('APENAS NOIVO')
    print('-'*20)
    if noivo:
        Lista_Noivo = sorted(noivo- noiva)
        for nome in Lista_Noivo:
            print(nome)
        print()
    else:
        print()
    
    print('-'*20)
    print('POR AMBOS')
    print('-'*20)
    if noivo & noiva:
        ambas = sorted(noivo & noiva)
        for nome in ambas:
            print(nome)
        print()
    else:
        print()

    print('-'*20)
    print('POR APENAS UM DELES')
    print('-'*20) 
    if noivo and noiva:
        ApenasUm = sorted( (noivo - noiva) | (noiva - noivo))
        for nome in ApenasUm:
            print(nome)


noiva = set()
noivo = set()


while True:
    convidado= input().split(";")
    if convidado[0] == 'ACABOU': break
    if convidado[1] == 'noivo':
        noivo.add(convidado[0])
    if convidado[1] == 'noiva':
        noiva.add(convidado[0])
exibe(noiva,noivo)