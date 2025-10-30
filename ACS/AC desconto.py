preco = float(input())
quantidade = int(input())

total = preco * quantidade
desconto = 10/100 + (quantidade * 1/100)
total_desconto = total*(1 - desconto)
print(f'{total:.2f}')
print(f'{total_desconto:.2f}')
