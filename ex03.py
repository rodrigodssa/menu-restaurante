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