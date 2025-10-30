x = int(input()) #Teste por diversão
while x >= 1:
    print(f'{x:.3f}', end=' ')
    x /= 2
print ('boa')

y = 100 #Exercico 2 - fazer de 100 até 200 em forma crescente
while y >= 100 and y <=200 :
    print(f'{y}', end=' ')
    y += 1
print ('boa 2')

z = 200 #Exercico 2 - fazer de 200 até 100 em forma decrescente
while z >= 100 and z <=200 :
    print(f'{z}', end=' ')
    z -= 1
print ('boa 3')


n = int(input()) #Exercicio 3
w = 0
n2 = 0
while w < n :
    print( n2, end=' ')
    n2 += 2
    w += 1
print ('boa 4')

x = int(input()) # exercicio 4
y = int(input())

quociente = 0

while (x - y) > 0:
    x -= y
    quociente += 1
print (quociente)


