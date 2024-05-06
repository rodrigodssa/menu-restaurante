#nome = input("Digite seu nome: ")
#print("ola" , nome + "! Bem vindo ao jogo")


nome = input('Digite seu nome:')
sobrenome = input('Digite seu sobrenome:')

print('ola' ,nome,sobrenome, '! + Bem vindo ao jopgo')


# Imagine que você está desenvolvendo em Python para a Meteora, uma loja de roupas e-commerce. Você está no processo de adicionar descrições de produtos ao site e precisa usar a função print em python para exibir as descrições na página. As descrições dos produtos incluem várias linhas e parágrafos.


print("Camiseta Unisex",
"Tamanho: p , m , g , gg",
"Material: 100% algodão",
"Cores disponiveis: Preto, Branco, Vermelho", sep="\n" )


# Imagine que você está trabalhando na Organo, uma plataforma de organogramas para empresas. Você foi designado para criar um simples script em Python que coleta o nome de um departamento e o nome da pessoa responsável por ele, para depois imprimir uma mensagem personalizada.

departamento = input("Digite o nome do departamento: ")
responsavel = input("Digite o nome da pessoa responsável: ")
print("O departamento de " + departamento + " é liderado por " + responsavel + ".")

# Imagine que você está desenvolvendo um projeto para um serviço de streaming de música. Sua tarefa é melhorar o algoritmo de recomendação de músicas, garantindo que os usuários recebam sugestões mais precisas com base em seus gêneros favoritos. Para isso, você precisa criar uma função em Python que classifique as sugestões de músicas utilizando estruturas condicionais if, else e elif.

# No processo de desenvolvimento, você escreveu a seguinte função para classificar uma música como 'recomendada', 'neutra' ou 'não recomendada' com base na preferência do gênero musical do usuário:



def classificar_musica(genero_favorito, genero_musica):
    if genero_favorito == genero_musica:
        return 'recomendada'
    elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
        return 'neutra'
    else:
        return 'não recomendada'

resultado = classificar_musica('Rock', 'Pop')
print(resultado)



# Imagine que você está desenvolvendo um aplicativo chamado Fokus, inspirado na técnica Pomodoro de gerenciamento de tempo. O objetivo do Fokus é ajudar as pessoas a se concentrarem em suas tarefas usando períodos de trabalho focados intercalados com breves intervalos. Uma característica importante do seu aplicativo é permitir que o usuário escolha o tempo de foco e o tempo de pausa.

# Você precisa escrever uma função que pergunte ao usuário quanto tempo deseja configurar para o período de foco e, em seguida, use condicionais para verificar se o tempo inserido está dentro de um intervalo aceitável (por exemplo, entre 25 e 45 minutos).

def configurar_tempo_foco():
    tempo = int(input("Digite o tempo de foco (25-45 min): "))
    if tempo < 25:
        print("Valor muito baixo. Configure um tempo maior ou igual a 25 minutos.")
    elif tempo > 45:
        print("Valor muito alto. Configure um tempo menor ou igual a 45 minutos.")
    else:
        print("Tempo configurado para", tempo, "minutos.")

        