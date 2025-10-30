A,B,C,D = input().split()
A = float(A)
B = float(B)
C = float(C)
D = float(D)

media = (A*2 + B*3 + C*4 + D*1) / 10

print (f'Media: {media:.1f}')

if media >=7.0:
    print ('Aluno aprovado.')
    
elif media <5.0:
    print ('Aluno reprovado.')
    
elif  5.0<= media <=6.9 :
    print('Aluno em exame.')
    exame = float(input())
    nota_final = (media + exame)/2
    print(f'Nota do exame: {exame:.1f}')
    if nota_final >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {nota_final:.1f}')

