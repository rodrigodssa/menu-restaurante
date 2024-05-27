import os

restaurantes = [{'nome':'Praca', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():

    print("""⟆Ꭿᑲᗝᖇ ∈ⲭᕈᖇ∈⟆⟆
""")          

def exibir_opcoes():
    print(' 1. Cadastrar restaurante ')
    print(' 2. Listar restaurantes ')
    print(' 3. Alternar estado do restaurante ')
    print(' 4. Sair\n')

def finalizar_app():
    exibir_subtitulo('finalizando app')   

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu: ')
    main()


def opcao_invalida():
    print('opcao invalida!\n')
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurantes
    - Catregoria

    Output:
    - Adiciona um novo restaiurante a lista de restaurantes
    
    
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurantes que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante{nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado'if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()  


def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante{nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado.')        

    voltar_ao_menu_principal()

def escolher_opcao(): 
    try:
        opcao_escolhida = int(input('escolha uma opcão: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()    
        else:
            opcao_invalida()
    except:
        opcao_invalida()        

    finalizar_app() 
    os.system("clear") # funcao para limpar o terminal no mac
    print("Finalizando o app\n")


def main ():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__' :
    main()

