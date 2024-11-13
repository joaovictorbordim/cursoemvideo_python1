#Escreva um programa que pergunte a quantidade de Km percorridos
#por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodados.

km = float(input('Calculo de custo de aluguel automotivo.\n\nDigite a quantidade de Km percorridos: '))
dia = int(input('Digite a quantidade de dias locados: '))
total = (dia * 60)+(km * 0.15)

print('O tatal é de R${:.2f}'.format(total))
