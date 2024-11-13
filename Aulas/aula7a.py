#Operações aritméticas.

#nome = input('Digite seu nome: ')
#print('Prazer meu nome é {}!'.format(nome))

#print('Prazer meu nome é {:20}!'.format(nome))
#utiliza um tamanho de 20 caractéris.

#print('Prazer meu nome é {:>20}!'.format(nome))
#Centralizado a direita, dentro do espaço.

#print('Prazer meu nome é {:<20}!'.format(nome))
#Centralizado a esquerda, dentro do espaço.

#print('Prazer meu nome é {:^20}!'.format(nome))
#Centralizado, dentro do espaço.

#print('Prazer meu nome é {:=^20}!'.format(nome))
#Centralizado entre 20 caractéris de = , dentro do espaço.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

#print('A soma vale {}.'.format(n1+n2))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

#print('A somoa é {}, o produto é {} e a divisão é {}'.format(s, m, d))
#print('A divisão inteira é {} e a potência é {}'.format(di, e))

#Utilizando formatação de casas futuantes.
#print('A somoa é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d))
#print('A divisão inteira é {} e a potência é {}'.format(di, e))

#Utilizando formatação para NÃO quebra de linha.
print('A somoa é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potência é {}'.format(di, e))