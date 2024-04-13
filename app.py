import os

def exibir_nome_do_programa():

    print("""⟆Ꭿᑲᗝᖇ ∈ⲭᕈᖇ∈⟆⟆
""")          

def exibir_opcoes():
    print(" 1. cadastrar restaurante ")
    print(" 2. listar restaurantes ")
    print(" 3. ativar restaurante ")
    print(" 4. sair\n ")

def finalizar_app():
    os.system("clear")
    # os.system("clear") para o mac
    print("finalizando o app\n")    

def escolher_opcao():
    opcao_escolhida = int(input("escolha uma opcão: "))
    # opcao_escolhida = int(opcao_escolhida)

    if opcao_escolhida == 1:
        print("cadastrar restaurante")
    elif opcao_escolhida == 2: 
        print("listar restaurantes")
    elif opcao_escolhida == 3:
        print("ativar restaurante")
    else:
        finalizar_app() 

def main ():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__" :
    main()
