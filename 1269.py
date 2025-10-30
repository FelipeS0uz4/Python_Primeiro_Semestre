def mapeamento(x, tipo):
    for i in range(len(x)):
        x[i] = tipo(x[i])
    return x

def exibir(lista): 
    mapeamento(lista,int)
    lista.sort()
    return lista

def adicionar (x):
    y = int(ordem[1])
    carrinho.append(y)

carrinho = []

inicio = input().split()

mapeamento(inicio,int)

carrinho.extend(inicio)

while True:

    ordem = input().split()

    if ordem[0] == 'adicionar':
        adicionar (ordem[1])
        
    if ordem[0] == 'exibir':
        print(*exibir(carrinho))

    if ordem[0] == 'remover':
        bye = int(ordem[1])
        if bye in carrinho:
            carrinho.remove(bye)
        else:
            print(f'código {bye} não encontrado')
    
    if ordem[0] == 'encerrar':
        print(*exibir(carrinho))
        break
