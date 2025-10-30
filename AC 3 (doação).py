doado = 0.00
dinheiro = 0.00

n = float(input())

while n != -1:
    doado += n
    dinheiro += (n * 2.50)
    n = float(input())

print (f'VC$ {doado:.2f}')
print (f'R$ {dinheiro:.2f}')
