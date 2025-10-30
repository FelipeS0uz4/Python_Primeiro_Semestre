from typing import Dict
from abc import ABC

class Existe(ABC):
    def __init__(self, nome: str, vida_inicial: int, vida_atual: int = None):
        self.nome = nome
        self.vida_inicial = int(vida_inicial)
        self.vida_atual = int(vida_atual if vida_atual is not None else vida_inicial)

    def retirar_vida(self, dano: int) -> int:
        dano = max(0, int(dano))
        self.vida_atual -= dano
        if self.vida_atual <= 0:
            self.vida_atual = 0
            print('-' * 20)
            print(f'{self.nome} foi derrotado!')
            print(f'Vida Restante: {self.vida_atual}')
            print('-' * 20)
        else:
            print('-' * 20)
            print(f'{self.nome} recebeu {dano} de dano. Vida restante: {self.vida_atual}')
            print('-' * 20)
        return self.vida_atual

    def adicionar_vida(self, cura: int) -> int:
        cura = max(0, int(cura))
        self.vida_atual += cura
        if self.vida_atual >= self.vida_inicial:
            self.vida_atual = self.vida_inicial
            print('-' * 20)
            print(f'{self.nome} recuperou vida e está com a vida cheia ({self.vida_atual}).')
            print('-' * 20)
        else:
            print('-' * 20)
            print(f'{self.nome} recuperou {cura} de vida. Vida atual: {self.vida_atual}')
            print('-' * 20)
        return self.vida_atual

    @property
    def vivo(self) -> bool:
        return self.vida_atual > 0

    def exibir(self):
        print('-' * 20)
        print(f'DADOS DE {self.nome.upper()}')
        print('-' * 20)
        print(f'NOME: {self.nome}')
        print(f'VIDA INICIAL: {self.vida_inicial}')
        print(f'VIDA ATUAL: {self.vida_atual}')
        print('-' * 20)


class Player(Existe):
    def __init__(self, nome: str, vida_inicial: int, vida_atual: int = None, pe_inicial: int = 0, ph: int = 0, pu: int = 0):
        super().__init__(nome, vida_inicial, vida_atual)
        self.pe_inicial = int(pe_inicial)
        self.pe_atual = int(pe_inicial)
        self.ph = int(ph)
        self.pu = int(pu)


class Boss(Existe):
    pass


def preencher_player(dicionario_player: Dict[str, Player]) -> Dict[str, Player]:
    quantidade = int(input('Quantos Players? '))
    for i in range(1, quantidade + 1):
        print(f'\nDados do Player {i}')
        nome = input('Nome: ')
        vida = int(input(f'Vida inicial do {nome}: '))
        pe = input(f'PE inicial do {nome} (ou Enter para 0): ')
        pe = int(pe) if pe.strip() else 0
        ph = input(f'PH do {nome} (ou Enter para 0): ')
        ph = int(ph) if ph.strip() else 0
        pu = input(f'PU do {nome} (ou Enter para 0): ')
        pu = int(pu) if pu.strip() else 0

        resposta = input(f'O {nome} já levou dano? (S/N) ').strip().upper()
        vida_atual = vida
        if resposta == 'S':
            ferido = int(input('Quanto de dano ele levou? '))
            vida_atual = max(0, vida - ferido)

        dicionario_player[nome] = Player(nome, vida, vida_atual, pe, ph, pu)
        print('-' * 20)
    return dicionario_player


def preencher_inimigo(dicionario_inimigo: Dict[str, Boss]) -> Dict[str, Boss]:
    quantidade = int(input('Quantos Inimigos? '))
    for i in range(1, quantidade + 1):
        print(f'\nDados do Inimigo {i}')
        nome = input('Nome: ')
        vida = int(input(f'Vida inicial do {nome}: '))
        resposta = input(f'O {nome} já levou dano? (S/N) ').strip().upper()
        vida_atual = vida
        if resposta == 'S':
            ferido = int(input('Quanto de dano ele levou? '))
            vida_atual = max(0, vida - ferido)

        dicionario_inimigo[nome] = Boss(nome, vida, vida_atual)
        print('-' * 20)
    return dicionario_inimigo


def listar_vivos(dicionario: Dict[str, Existe]):
    for nome, personagem in dicionario.items():
        status = f'{personagem.vida_atual}/{personagem.vida_inicial}'
        vivo_text = '' if personagem.vivo else ' (morto)'
        print(f'- {nome} {status}{vivo_text}')


def escolher_personagem(dicionarios: Dict[str, Dict[str, Existe]]):
    print('\nEscolha o lado do personagem que vai agir:')
    lados = [k for k in dicionarios.keys()]
    for i, lado in enumerate(lados, 1):
        print(f'{i}. {lado}')
    escolha_lado = input('Escolha (número ou nome): ').strip()
    if escolha_lado.isdigit():
        escolha_lado = lados[int(escolha_lado) - 1]
    else:
        escolha_lado = escolha_lado.capitalize()

    if escolha_lado not in dicionarios:
        print('Lado inválido.')
        return None, None, None

    print(f'\nPersonagens disponíveis em {escolha_lado}:')
    listar_vivos(dicionarios[escolha_lado])
    nome = input('Escolha o personagem (exact name): ')
    personagem = dicionarios[escolha_lado].get(nome)
    if not personagem:
        print('Personagem não encontrado.')
        return None, None, None
    return escolha_lado, nome, personagem


def escolher_alvo(dicionario_oponente: Dict[str, Existe]):
    print('\nAlvos disponíveis:')
    listar_vivos(dicionario_oponente)
    alvo_nome = input('Escolha o alvo (exact name): ')
    alvo = dicionario_oponente.get(alvo_nome)
    if not alvo:
        print('Alvo não encontrado.')
        return None, None
    if not alvo.vivo:
        print('Alvo já está morto.')
        return None, None
    return alvo_nome, alvo


def acao(personagem: Existe, lado: str, diccionarios: Dict[str, Dict[str, Existe]]):
    print('\nAções:')
    print('1. Atacar')
    print('2. Curar')
    print('3. Exibir')
    print('4. Nada')
    escolha = input('Escolha a ação: ').strip()

    if escolha in ['1', 'Atacar', 'ATACAR']:
        alvo_lado = 'Inimigo' if lado == 'Player' else 'Player'
        if alvo_lado not in diccionarios or not diccionarios[alvo_lado]:
            print('Não há oponentes cadastrados.')
            return
        alvo = escolher_alvo(diccionarios[alvo_lado])
        if alvo:
            dano = int(input('Quanto de dano causado? '))
            alvo.retirar_vida(dano)
    elif escolha in ['2', 'Curar', 'CURAR']:
        cura = int(input('Quanto de cura? '))
        personagem.adicionar_vida(cura)
    elif escolha in ['3', 'Exibir', 'EXIBIR']:
        personagem.exibir()
    else:
        print('Nenhuma ação realizada.')


def main():
    dic_players: Dict[str, Player] = {}
    dic_inimigos: Dict[str, Boss] = {}

    print('-' * 20)
    print('Cadastro de Players:')
    preencher_player(dic_players)
    print('\nCadastro de Inimigos:')
    preencher_inimigo(dic_inimigos)

    diccionarios = {'Player': dic_players, 'Inimigo': dic_inimigos}

    try:
        while True:
            print('\n--- Turno ---')
            lado, nome, personagem = escolher_personagem(diccionarios)
            if not personagem:
                continue
            if not personagem.vivo:
                print('Esse personagem está morto e não pode agir.')
                continue
            acao(personagem, lado, diccionarios)

            todos_players_mortos = all(not p.vivo for p in dic_players.values()) if dic_players else True
            todos_inimigos_mortos = all(not i.vivo for i in dic_inimigos.values()) if dic_inimigos else True
            if todos_players_mortos:
                print('\nTodos os Players foram derrotados. Fim do jogo.')
                break
            if todos_inimigos_mortos:
                print('\nTodos os Inimigos foram derrotados. Fim do jogo.')
                break

    except KeyboardInterrupt:
        print('\nExecução interrompida pelo usuário.')


if __name__ == '__main__':
    main()