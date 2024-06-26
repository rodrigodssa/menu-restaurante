# 1 - Imprima a frase: Python na Escola de Programação .
#  Para imprimir a frase, basta utilizar a função print() com aspas simples ou duplas entre a sentença:
print('python na Escols de programação. ')



# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
# Para imprimir a frase utilizando variáveis, temos algumas abordagens possíveis:
# criação de variáveis
nome = 'Rodrigo'
idade = 41
# Abordagem mais simples
print('Meu nome é' ,nome, 'e tenho' ,idade, 'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos. ')

# Abordagem do .format ()
print('Meu nome é {} e tenho {} anos. ' .format(nome,idade))

#Abordagem da % (Formatação de Sting Antiga - python 2 )
print('Meu nome é %s e tenho %i anos. '%(nome,idade))



# 3 - Imprima a palavra: ‘ESCOLA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
# Para imprimir a palavra ‘ESCOLA’ com cada letra em cada linha com a função print utilizando o parâmetro sep para especificar o separador entre os argumentos da seguinte forma:
print('E','S','C','O','L','A',sep='\n')
# O separador sep é definido como \n, que representa uma quebra de linha.



# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
# Para imprimir o valor de pi arredondado, temos algumas possíveis abordagens:
pi = 3.14159
# Abordagem de f-string
print(f'O valor arrendodado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}' .format(pi))

#Utilizando a função round()
print('O valor arrendodado de pi é:', round(pi, 2))




