divida = int(input())
pago = int(input())
contador = 0
while divida > 0:
    contador += 1
    quitada = divida - pago
    
    if quitada < 0:
        quitada = 0
        
    print(f'pagamento: {contador}')
    print(f'antes = {divida}')
    print(f'depois = {quitada}')
    print(f'{"-"*5}')
    
    divida = quitada
    
