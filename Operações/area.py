A,B,C =input().split()

A= float(A)
B= float(B)
C= float(C)

print(f'TRIANGULO: {(A * C)/2:.3f}')

print(f'CIRCULO: {3.14159 * C ** 2:.3f}')

print(f'TRAPEZIO: {(B + A) * C / 2:.3f}')

print(f'QUADRADO: {B ** 2:.3f}')

print(f'RETANGULO: {A * B:.3f}')
