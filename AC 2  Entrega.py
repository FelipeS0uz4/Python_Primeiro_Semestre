def dias (n1):      #com função
    if n1 == 'domingo':
        n3 = 0
    elif n1 == 'segunda':
        n3 = 1
    elif n1 == 'terca':
        n3 = 2
    elif n1 == 'quarta':
        n3 = 3
    elif n1 == 'quinta':
        n3 = 4
    elif n1 == 'sexta':
        n3 = 5
    else:
        n3 = 6
        
    return (n3)

def dta (entrega):
    if entrega == 0:
        n5 = 'domingo'
    elif entrega == 1:
        n5 = 'segunda'
    elif entrega == 2:
        n5 = 'terca'
    elif entrega == 3:
        n5 = 'quarta'
    elif entrega == 4:
        n5 = 'quinta'
    elif entrega == 5:
        n5 = 'sexta'
    else:
        n5 = 'sabado'
    
    return (n5)

n1 = input() 
n2 = int(input()) 

A = dias (n1)
entrega = (A + n2) % 7
Data = dta (entrega)

if n2 == 0:
    print ('chega hoje!')
else:
    print(f'sera entregue {Data}')



dia_da_semana = input() #sem função
prazo = int(input())

if dia_da_semana == 'domingo':
    dia = 0
elif dia_da_semana == 'segunda':
    dia = 1
elif dia_da_semana == 'terca':
    dia = 2
elif dia_da_semana == 'quarta':
    dia = 3
elif dia_da_semana == 'quinta':
    dia = 4
elif dia_da_semana == 'sexta':
    dia = 5
else:
    dia = 6

dia_entrega = (dia + prazo) % 7

if prazo == 0:
    print('chega hoje!')
else:
    if dia_entrega == 0:
        print('sera entregue domingo')
    elif dia_entrega == 1:
        print('sera entregue segunda')
    elif dia_entrega == 2:
        print('sera entregue terca')
    elif dia_entrega == 3:
        print('sera entregue quarta')
    elif dia_entrega == 4:
         print('sera entregue quinta')
    elif dia_entrega == 5:
        print('sera entregue sexta')
    else:
        print('sera entregue sabado')

