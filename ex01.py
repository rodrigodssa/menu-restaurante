# Para imprimir a frase, basta utilizar a função print() com aspas simples ou duplas entre a sentença:
print('python na Escols de programação. ')

#















# para verificar se o número é impar ou par, você pode fazer essa estrutura condicional:

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('0 número é par. ')
else:
    print('o número é ímpar.')    

# Para fazer as condicionais que informará a idade em categorias, você pode usar essa estrutura:

idade = int(input('Digite sua idade: '))
if 0 < idade <= 12:
    print('criança')
elif 12 < idade <= 18:
    print('adolescente')
elif idade > 18:
    print('adulto')        
else: 
    print('valor inválido!')

# Para fazer uma condicional que poderá verificar os valores de usuário e senha, você pode utilizar o seguinte código:

usuario_correto = 'Rodrigo'
senha_correta = 'Rodrigo123'

usuario = input('Digite o nome do usuario: ')
senha = input('Digite a senha: ')

if usuario == usuario_correto and senha == senha_correta:
    print('login bem sucedido! ')
print('credencias invalidas. tente novamente.')    


# Para verificar onde o ponto está localizado no plano cartesiano, você pode utilizar a seguinte estrutura:

x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordenada y: '))

if x > 0 and y > 0:
    print('O ponto está no primeiro quadrante. ')
elif x < 0 and y > 0:
    print('O ponto está no segundo quadrante. ')
elif x < 0 and y < 0:
    print('O ponto está no terceiro quadrante. ')
elif x > 0 and y < 0:
    print('O ponto está no quarto quadrante. ')
else:
    print('O ponto está sobre um eixo ou na origem. ')




