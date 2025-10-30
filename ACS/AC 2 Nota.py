n1 = float(input()) #Codigo 1
n2 = float(input())

n3 = (n1+n2)/2
n4 = (n1+10)/2

if n1 <= 1:
    print('reprovado')

else:
    if n3 >= 6:
        print('aprovado')

    elif n4 >6:
        print('talvez com a sub')
    
    else:
        print('reprovado')



trabalhos = float(input()) #tentativa 2
prova_regular = float(input())

media_final = (trabalhos + prova_regular) / 2

if media_final >= 6:
    print("aprovado")
else:
    nota_necessaria = (6 - (0.5 * trabalhos)) / 0.5
    if nota_necessaria > 10:
        print("reprovado")
    else:
        if nota_necessaria <= prova_regular:
            print("talvez com a sub")
        else:
            print("reprovado")
