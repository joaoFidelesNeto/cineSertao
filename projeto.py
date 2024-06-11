from funcoes import *

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

while (True):
    print(f'{BLUE}MENU PRINCIPAL\n')
    print(f'{BLUE}[1]Fazer login\n[2]Cadastrar conta\n{RESET}')
    menu_principal = input(f'{BLUE}Digite a opção desejada:{RESET}')
    if (menu_principal == '1'):
        login = input(f'{BLUE}Digite seu login: {RESET}')
        senha = input(f'{BLUE}Digite sua senha: {RESET}')
        if('@gmail.com' in login and len(senha) == 6):
            if(login in usuarios['usuarios'] and senha == usuarios['usuarios'][login]['pin']):
                print(f'{MAGENTA}Login efetuado com sucesso{RESET}')
                while (True):
                    print(f'{MAGENTA}MENU DO CLIENTE\n{RESET}')
                    print(f'{MAGENTA}[1] Catalogo de filmes\n[2] Buscar Filme\n[3] Comprar Filme\n[4] Recomendar Filme\n[5] Sair\n{RESET}')
                    menu_usuario = input(f'{MAGENTA}Digite a opção desejada:\n{RESET}')
                    if(menu_usuario == '1'):
                        mostrar_filmes()
                    elif(menu_usuario == '2'):
                        buscar_filme()
                    elif (menu_usuario == '3'):
                        comprar_filme()
                    elif(menu_usuario == '4'):
                        cliente = usuarios['usuarios'][login]['nome']
                        recomendados = recomendar_filmes(login)
                        if(recomendados):
                            print('Filmes Recomendados:')
                            for filme in recomendados:
                                print(filme['filme'])
                        else:
                            print(f'{MAGENTA}Não há filmes recomendados no momento.\n{RESET}')
                    elif(menu_usuario == '5'):
                        print(f'{MAGENTA}Voltando ao Menu principal\n{RESET}')
                        break
                    # menu_usuario
                    else:
                        print(f'{RED}Opção não existe\n{RESET}')

            elif(login in adm['adm'] and senha == adm['adm'][login]['pin']):
                print(f'{GREEN}Login efetuado com sucesso{RESET}')
                while (True):
                    print(f'{GREEN}MENU DO ADMINISTRADOR\n{RESET}')
                    print(f'{GREEN}[1] Cadastrar Filme\n[2] Atualizar Dados do Filme\n[3] Buscar Filme\n[4] Remover Filme\n[5] Verificar Pedidos\n[6] Sair \n{RESET}')
                    gerenciar_filme = input(f'{GREEN}Digite a opção desejada:\n{RESET}')
                    if(gerenciar_filme == '1'):
                        cadastrar_filme()
                    elif(gerenciar_filme == '2'):
                        mudar_filme()
                    elif(gerenciar_filme == '3'):
                        buscar_filme()
                    elif(gerenciar_filme == '4'):
                        remover = input(f'{GREEN}Digite o Nome do filme que o senhor(a) deseja remover do catálogo:{RESET}')
                        for chave, filme_valor in list(filmes['filmes'].items()):
                            if(filme_valor['filme'] == remover):
                                filme_removido = filmes['filmes'].pop(chave)
                                mostrar_filmes()
                    elif(gerenciar_filme == '5'):
                        verificar_pedidos()
                    
                    elif(gerenciar_filme == '6'):
                        print(f'{GREEN}Saindo do MENU DO ADMINISTRADOR{RESET}')
                        break
                    else:
                        print(f'{RED}Opção não existe{RESET}')
            else:
                print(f'{RED}\nConta não existe!!!\n{RESET}')
        else:
            print(f'{RED}Caracteres não atendem aos requisitos.\n{RESET}')

    elif(menu_principal == '2'):
        print(f'CADASTRAR CONTA\n')
        print(f'{BLUE}[1]Cadastrar Cliente\n[2]Cadastrar Administrador\n[3]Sair\n{RESET}')
        cadastrar_conta = input(f'Digite a opção desejada:')
        if(cadastrar_conta == '1'):
            nome, login, senha = criar_login()
            if('@gmail.com' in login and len(senha) == 6):
                usuarios['usuarios'][login] = {'nome': nome, 'pin': senha}
                print(f'{BLUE}\n------CLIENTE CADASTRADO------\n')
                print(f'{BLUE}Nome do Cliente: {nome}{RESET}')
                print(f'{BLUE}Login do Cliente: {login}{RESET}')
                print(f'{BLUE}Senha do Cliente: {senha}\n{RESET}')
                break
            else:
                print(f'{RED}\nLogin ou senha não atendem aos critérios de cadastro{RESET}')

        elif(cadastrar_conta == '2'):
            nome, login, senha = criar_login()
            if('@gmail.com' in login and len(senha) == 6):
                adm['adm'][login] = {'nome': nome, 'pin': senha}
                print(f'{BLUE}\n------ADMINISTRADOR CADASTRADO------\n')
                print(f'{BLUE}Nome do Administrador: {nome}{RESET}')
                print(f'{BLUE}Login do Administrador: {login}{RESET}')
                print(f'{BLUE}Senha do Administrador: {senha}\n{RESET}')
                break
            else:
                print(f'{RED}\nLogin ou senha não atendem aos critérios de cadastro{RESET}')

        elif(cadastrar_conta == '3'):
            print(f'{BLUE}Voltando para Menu Principal\n{RESET}')
        # cadastrar conta
        else:
            print(f'{RED}Opção não existe\n{RESET}')
    # Menu principal
    else:
        print(f'{RED}Opção não existe{RESET}')

