x = int(input())
y = int(input())

if x > y:
  x, y = y, x

soma = 0
i = x + 1

while i < y:
  if i % 2 != 0:
    soma += i
  i += 1

print(soma)
