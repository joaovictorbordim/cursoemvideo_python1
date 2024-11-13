#Crie um programa que leia quanto dinheiro tem na carteira e mostre quantos Dólares podemos comprar. Considere US$1,00 =R$3,27
real = float(input('Vamos comprar dólares? Digite o valor que possui em sua carteira e veja quantos Dólares você pode comprar: '))
dol = real / 3.27

print('Considerando o valor em Real que você tem {}, você pode comprar {:.2f} Dólares'.format(real, dol))
