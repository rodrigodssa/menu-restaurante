# Para imprimir a frase, basta utilizar a função print() com aspas simples ou duplas entre a sentença:
print('python na Escols de programação. ')

# Para imprimir a frase utilizando variáveis, temos algumas abordagens possíveis:

# criação de variáveis
nome = 'Rodrigo'
idade = 41

# Abordagem mais simples
print('Meu nome é' ,nome, 'etenho' ,idade, 'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos. ')

# Abordagem do .format ()
print('Meu nome é {} e tenho {} anos. ' .format(nome,idade))

#Abordagem da % (Formatação de Sting Antiga - python 2 )
print('Meu nome é %s e tenho %i anos. '%(nome,idade))

# Para imprimir a palavra ‘ESCOLA’ com cada letra em cada linha com a função print utilizando o parâmetro sep para especificar o separador entre os argumentos da seguinte forma:
print('E','S','C','O','L','A',sep='\n')
# O separador sep é definido como \n, que representa uma quebra de linha.

# Para imprimir o valor de pi arredondado, temos algumas possíveis abordagens:
pi = 3.14159

# Abordagem de f-string
print(f'O valor arrendodado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}' .format(pi))

#Utilizando a função round()
print('O valor arrendodado de pi é:', round(pi, 2))



















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




