from abc import ABC, abstractmethod

class Existe(ABC):
    def __init__(self,nome=None,vida_inicial=int,vita_atual=int):
        self.nome = nome
        self.vida_inicial = vida_inicial
        self.vida_atual = vita_atual
        
    @abstractmethod
    def retirar_vida(self,dano):
        self.vida_atual -= dano
        if self.vida_atual <= 0:
            print('-'*20)
            print(f'O {self.nome} está morto')
            print(f'Vida Restante de: {self.vida_atual}')
            print('-'*20)
        else:
            print('-'*20)
            print(f'O {self.nome} está com {self.vida_atual} vida restante')
            print('-'*20)
        return self.vida_atual
    
    
    @abstractmethod
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
        return self.vida_atual
        
class Player(Existe):
    def __init__(self, nome=None, vida_inicial=int, vita_atual=int,pe_inicial=int,pe_atual=int,ph_inicial=int,pu=None,):
        super().__init__(nome, vida_inicial, vita_atual)
        self.pe_inicial = pe_inicial
        self.pe_atual = pe_atual
        
        self.ph = ph_inicial
        self.pu = pu

class Boss(Existe):
    def __init__(self,nome=None,vida_inicial=int,vida_atual=int,):
        super().__init__(nome,vida_inicial,vida_atual)


    def retirar_vida(self,dano):
        self.vida_atual -= dano
        if self.vida_atual <= 0:
            print('-'*20)
            print(f'O {self.nome} está morto')
            print(f'Vida Restante de: {self.vida_atual}')
            print('-'*20)
        else:
            print('-'*20)
            print(f'O {self.nome} está com {self.vida_atual} vida restante')
            print('-'*20)
        return self.vida_atual
    
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
        return self.vida_atual
    
    def exibir(self):
        print('-'*20)
        print(f'DADOS DO {self.nome.upper()}')
        print('-'*20)
        print(f'NOME: {self.nome}')
        print(f'VIDA INICIAL: {self.vida_inicial}')
        print(f'VIDA ATUAL: {self.vida_atual}')
        print('-'*20)
        
        
def inicio():
    print('-'*20)
    print('')
    
def preencher_player(dicionario_player):
    quantidade = int(input(f'Quantos Player'))
    for _ in range(1,quantidade+1):
        print()
        print(f'Dados do Inimigos {_}')
        print()
        nome = input('Nome: ')
        vida = int(input(f'Vida inicial do {nome}: '))
        vida_atual = vida
        print(f'O {nome} já levou dano: S/N ')
        pe = int(input(f'PE inicial do {nome}: '))
        pe_atual = pe 
        pu = int(input(f'PU inicial do {nome}: '))
        pu_atual = pu
        ph
        resposta = input().upper()
        if resposta == 'S':
            ferido = int(input('Quanto de dano ele levou? '))
            vida_atual -= ferido
        
        
        dicionario_player[nome] = [vida, vida_atual]
        print()
        print('-'*20)
    return dicionario_player
        
def preeecher_inimigo(dicionario_inimigo):
    quantidade = int(input(f'Quantos Inimigos? '))
    for _ in range(1,quantidade+1):
        print()
        print(f'Dados do Inimigos {_}')
        print()
        nome = input('Nome: ')
        vida = int(input(f'Vida inicial do {nome}: '))
        vida_atual = vida
        print(f'O {nome} já levou dano: S/N ')
        resposta = input().upper()
        if resposta == 'S':
            ferido = int(input('Quanto de dano ele levou? '))
            vida_atual -= ferido
        dicionario_inimigo[nome] = [vida, vida_atual]
        print()
        print('-'*20)
    return dicionario_inimigo

def escolha(dicionario):
        print(f'Qual Inimigo')
        for nome, (vida, vida_atual) in dicionario.items():
            if vida_atual > 0:
                print()
                print(nome)
        print()
        escolhido = input(f"Escolha o Inimigo: ")
        info_inimigo = dicionario.get(escolhido)
        return (info_inimigo, escolhido)
    
def ação(dicionario,escolhido,info_inimigo):
    if info_inimigo:
        inimigo = Boss(escolhido, info_inimigo[0], info_inimigo[1])
        print('-'*20)
        acao = input( "Ele recebeu?\n \nDano \n \nCura \n \nExibir \n \nNada \n \n").upper()
        print("-"*20)
        if acao == "DANO":
            dano = int(input("Quanto de Dano? "))
            dicionario[escolhido][1] = inimigo.retirar_vida(dano)
        elif acao == "CURA":
            cura = int(input("Quanto ele se curou? "))
            dicionario[escolhido][1] = inimigo.adicionar_vida(cura)
        elif acao == "EXIBIR":
            inimigo.exibir()
        else:
            print(f"O {escolhido} fez nada")
    else:
        print("Inimigo não encontrado")



def main():
    dicionario_Inimigo = {}
    dicionario_Player = {}
    inicio()
    personagem= input().upper
    if personagem == 'INIMIGO':
        personagem = 'Inimigo'
        preeecher_inimigo(dicionario_Inimigo)
    else:
        personagem = 'Player'
        preencher_player(dicionario_Player)

    if personagem == 'Inimigo':
        while True:
            pergunta  = escolha(dicionario_Inimigo)
            info_inimigo = pergunta[0]
            escolhido = pergunta[1]
            ação(dicionario_Inimigo,escolhido,info_inimigo)
    else:
        
        
main()