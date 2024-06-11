import difflib

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

filmes = {'filmes': {1: {'filme': 'logan',
                         'sala': 'sala 1',
                         'horario': '16:00',
                         'classificacao': '16 anos',
                         'genero': 'ação',
                         'ingressos2D': '20',
                         'ingressos3D': '25',
                         'capacidade': '80'},

                     2: {'filme': 'Xmen',
                         'sala': 'sala 2',
                         'horario': '19:00 ',
                         'classificacao': '14 anos',
                         'genero': 'ação',
                         'ingressos2D': '15',
                         'ingressos3D': '20',
                         'capacidade': '80'}}}

adm = {'adm': {'joaoneto@gmail.com': {'nome': 'João Neto',
                                      'pin': '123456'}}}

usuarios = {'usuarios': {'dudu@gmail.com': {'nome': 'dudu',
                                            'pin': '654321'}}}

preferencias_cliente = {'dudu@gmail.com': 'logan'}


def criar_login():
    while (True):
        print(f'{BLUE}CADASTRANDO CONTA{RESET}')
        nome = input(f'{BLUE}Digite seu nome: {RESET}')
        login = input(f'{BLUE}Digite seu email: {RESET}')
        senha = input(f'{BLUE}Digite sua senha: {RESET}')
        return nome, login, senha


def mostrar_filmes():
    for valor in filmes['filmes'].values():
        print(f'{CYAN}Nome do Filme: {valor['filme']}{RESET}')
        print(f'{CYAN}Sala: {valor['sala']}{RESET}')
        print(f'{CYAN}Horário do FILME: {valor['horario']}{RESET}')
        print(f'{CYAN}Classificação Indicativa: {valor['classificacao']}{RESET}')
        print(f'{CYAN}Gênero: {valor['genero']}{RESET}')
        print(f'{CYAN}Valor do ingresso 2D: {valor['ingressos2D']}R${RESET}')
        print(f'{CYAN}Valor do ingresso 3D: {valor['ingressos3D']}R${RESET}')
        print(f'{CYAN}Quantidade de cadeiras: {valor['capacidade']}\n{RESET}')


def buscar_filme():
    filme = input('Digite o nome do filme que o senhor(a) deseja buscar: ')
    nomes_filmes = []
    for valor in filmes['filmes'].values():
        nomes_filmes.append(valor['filme'])
    filme_proximo = difflib.get_close_matches(filme, nomes_filmes, n=1, cutoff=0.5)

    if (filme_proximo):
        filme_encontrado = filme_proximo[0]
        for valor in filmes['filmes'].values():
            if (valor['filme'] == filme_encontrado):
                print(f'{CYAN}Filme encontrado{RESET}')
                print(f'{CYAN}Nome do Filme: {valor['filme']}{RESET}')
                print(f'{CYAN}Sala: {valor['sala']}{RESET}')
                print(f'{CYAN}Horário do FILME: {valor['horario']}{RESET}')
                print(f'{CYAN}Classificação Indicativa aconselhada: {valor['classificacao']}{RESET}')
                print(f'{CYAN}Gênero: {valor['genero']}{RESET}')
                print(f'{CYAN}Valor do ingresso 2D: {valor['ingressos2D']}{RESET}')
                print(f'{CYAN}Valor do ingresso 3D: {valor['ingressos3D']}{RESET}')
                print(f'{CYAN}Quantidade de cadeiras: {valor['capacidade']}\n{RESET}')
                return
    else:
        print('Filme não encontrado')
        return None


def comprar_filme():
    nome_filme = input(f'Digite o nome do Filme que o senhor(a) deseja comprar:')
    nomes_filmes = []
    for valor in filmes['filmes'].values():
        nomes_filmes.append(valor['filme'])
    filme_proximo = difflib.get_close_matches(nome_filme, nomes_filmes, n=1, cutoff=0.5)
    if(filme_proximo):
        filme_encontrado = filme_proximo[0]
        for filme in filmes['filmes'].values():
            if filme['filme'] == filme_encontrado:
                ingressos2D = int(filme['ingressos2D'])
                ingressos3D = int(filme['ingressos3D'])
                capacidade = int(filme['capacidade'])
                comprar_filme = input(f'\n{MAGENTA}Qual a opção de visualização de filme você deseja: digite 2D ou 3D. {RESET}')
                numero_ingressos = int(input('Quantos ingressos o senhor(a) deseja comprar:'))
                if (numero_ingressos > 0):
                    if (comprar_filme == '3D'):
                        valor_da_compra = ingressos3D * numero_ingressos
                    elif (comprar_filme == '2D'):
                        valor_da_compra = ingressos2D * numero_ingressos
                    else:
                        print(f'{RED}Opção de visualização inválida.{RESET}')

                    if (numero_ingressos <= capacidade):
                        capacidade -= numero_ingressos
                        filme['capacidade'] = capacidade
                        print(f'{GREEN}Pedido realizado com sucesso{RESET}')
                        if (valor_da_compra > 0):
                            pedido = []
                            pedido.append((filme['filme'], filme['sala'], filme['horario'],numero_ingressos, valor_da_compra))
                            salvar_pedido(filme['filme'], filme['sala'], filme['horario'],numero_ingressos, valor_da_compra)
                            print(f'{pedido}')
                        else:
                            print(f'Pedido não pode ser realizado')
                    else:
                        print(
                            f'{RED}Número de ingressos solicitado excede a capacidade disponível. Disponível: {filme["capacidade"]}{RESET}')
                else:
                    print(f'Número de ingressos inválido\n')


def salvar_pedido(filme, sala, horario,num_ingressos,valor_total):  
    with open('pedidos.txt', 'a') as arquivo:
        arquivo.write(f'Filme: {filme}\n')
        arquivo.write(f'Sala: {sala}\n')
        arquivo.write(f'Horário: {horario}\n')
        arquivo.write(f'Número de Ingressos: {num_ingressos}\n')
        arquivo.write(f'Valor Total: R${valor_total}\n\n')


def verificar_pedidos():
    try:
        arquivo = open('pedidos.txt', 'r')
    except:
        print('Arquivo de pedidos não encontrado.')
        return
    pedidos = arquivo.read()
    arquivo.close()
    if(pedidos.strip()):
        print('------PEDIDOS------')
        print(pedidos)
    else:
        print('Não há pedidos registrados.')


def cadastrar_filme():
    filme = input(f'{GREEN}Digite o nome do filme:{RESET}')
    sala = input(f'{GREEN}Digite a sala do filme:{RESET}')
    horario = input(f'{GREEN}Digite o horario do filme:{RESET}')
    classificacao = input(f'{GREEN}Digite a classificação indicativa do filme:{RESET}')
    genero = input(f'{GREEN}Digite o gênero do filme:{RESET}')
    ingressos2D = input(f'{GREEN}Digite o valor do ingresso 2D:{RESET}')
    ingressos3D = input(f'{GREEN}Digite o valor do ingresso 3D:{RESET}')
    capacidade = input(f'{GREEN}Digite a capacidade da sala:{RESET}')
    if(len(filme) == 0 or len(sala) == 0 or len(horario) == 0 or len(classificacao) == 0 or len(genero) == 0 or len(
            ingressos2D) == 0 or len(ingressos3D) == 0 or len(capacidade) == 0):
        print(f'{RED}\nFilme não cadastrado por falta de informações.\n{RESET}')
    else:
        novo_filme = len(filmes['filmes']) + 1
        filmes['filmes'][novo_filme] = {'filme': filme, 'sala': sala, 'horario': horario,
                                        'classificacao': classificacao, 'genero': genero, 'ingressos2D': ingressos2D,
                                        'ingressos3D': ingressos3D, 'capacidade': capacidade}
        print(f'{GREEN}\nFilme salvo com sucesso!!!\n{RESET}')
        print(f'{CYAN}\n------CATALOGO DE FILMES------\n{RESET}')
        mostrar_filmes()


def mudar_filme():
    filme = input(f'{GREEN}Digite o nome do filme que você deseja mudar catalogo:{RESET}')
    for chave, valor in filmes['filmes'].items():
        if (valor['filme'] == filme):
            novo_filme = input(f'{GREEN}Digite o novo nome do filme:{RESET}')
            sala = input(f'{GREEN}Digite a nova sala:{RESET}')
            horario = input(f'{GREEN}Digite o novo horário:{RESET}')
            classificacao = input(f'{GREEN}Digite a nova classificação indicativa:{RESET}')
            genero = input(f'{GREEN}Digite o novo gênero do filme:{RESET}')
            ingressos2D = input(f'{GREEN}Digite o novo valor do ingresso 2D:{RESET}')
            ingressos3D = input(f'{GREEN}Digite o valor do ingresso 3D:{RESET}')
            capacidade = input(f'{GREEN}Digite a capacidade da sala:{RESET}\n')
            if(len(novo_filme) == 0):
                novo_filme = valor['filme']
            if(len(sala) == 0):
                sala = valor['sala']
            if(len(horario) == 0):
                horario = valor['horario']
            if(len(classificacao) == 0):
                classificacao = valor['classificacao']
            if(len(genero) == 0):
                genero = valor['genero']
            if(len(ingressos2D) == 0):
                ingressos2D = valor['ingressos2D']
            if(len(ingressos3D) == 0):
                ingressos3D = valor['ingressos3D']
            if(len(capacidade) == 0):
                capacidade = valor['capacidade']

            filmes['filmes'][chave] = {'filme': novo_filme, 'sala': sala, 'horario': horario,
                                       'classificacao': classificacao, 'genero': genero,
                                       'ingressos2D': ingressos2D, 'ingressos3D': ingressos3D, 'capacidade': capacidade}
            mostrar_filmes()
        else:
            print(f'Filme não foi encontrado')
            break

def recomendar_filmes(cliente):
    filme_assistido = preferencias_cliente.get(cliente)
    genero_assistido = None
    for filme in filmes['filmes'].values():
        if(filme['filme'] == filme_assistido):
            genero_assistido = filme['genero']
            break
    if(genero_assistido):
        filmes_recomendados = []
        for filme in filmes['filmes'].values():
            if(filme['genero'] == genero_assistido and filme['filme'] != filme_assistido):
                filmes_recomendados.append(filme)
        return filmes_recomendados
    else:
        return None