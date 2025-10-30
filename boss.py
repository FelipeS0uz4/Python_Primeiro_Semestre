class Boss:
    def __init__(self,nome=None,vida_inicial=int,vida_atual=int):
        self.nome = nome
        self.vida_inicial = vida_inicial
        self.vida_atual = vida_atual

    def retirar_vida(self,dano):
        self.vida_atual -= dano
        if self.vida_atual <= 0:
            print('-'*20)
            print(f'O {self.nome} está morto')
            print(f'Vida Restante de: {self.vida_atual}')
            print('-'*20)
            
        else:
            print('-'*20)
            print(f'Vida Restante de: {self.vida_atual}')
            print('-'*20)
            
    def adicionar_vida(self,cura):
        self.vida_atual += cura
        if self.vida_atual >= self.vida_inicial:
            print('-'*20)
            print(f'O {self.nome} ja esta com vida cheia')
            self.vida_atual = self.vida_inicial
            print(f'O {self.nome} esta com {self.vida_atual} de vida')
            print('-'*20)
        else:
            print('-'*20)
            print(f'O {self.nome} esta com {self.vida_atual} de vida')
            print('-'*20)
            
    def exibir(self):
        print('-'*20)
        print(f'DADOS DO {self.nome.upper()}')
        print('-'*20)
        print(f'NOME: {self.nome}')
        print(f'VIDA INICIAL: {self.vida_inicial}')
        print(f'VIDA ATUAL: {self.vida_atual}')
        print('-'*20)

def main():
    quantidade = int(input('Quantos inimigos? '))
    dicionario = {}
    for _ in range(1,quantidade+1):
        print()
        print(f'Dados do Inimigo {_}')
        print()
        nome = input('Nome: ')
        vida = int(input(f'Vida inicial do {nome}: '))
        vida_atual = vida
        resposta = input('O monstro já levou dano: S/N ').upper()
        if resposta == 'S':
            ferido = int(input('Quanto de dano ele levou? '))
            vida_atual -= ferido
        print('-'*20)
        inimigos = Boss(nome,vida, vida_atual)
        dicionario[inimigos.nome] = [inimigos.vida_inicial,inimigos.vida_atual] 
        

    while True:
        print('Qual inimigo?')
        for i in dicionario.keys():
            print(i)
        escolhido = input() 
        for i in dicionario.keys():
            if i == escolhido:
                print('Ele recebeu?')
                print('Dano')
                print('Cura')
                print('Nada')
                acao = input().upper()
                if acao == "DANO":
                    dano = int(input('Quanto de Dano? '))
                    inimigos.retirar_vida(dano)
                elif acao == 'CURA':
                    healing = int(input('Quanto ele se curou? '))
                    inimigos.adicionar_vida(healing)
                else:
                    print(f'O {escolhido} fez nada')
                    break

                inimigos.exibir()



main()


