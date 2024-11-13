#Faça um programa que leia a largura e a altura de uma parede em metros e cálcule a sua área e a quantidade de tintas
#necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

val1 = float(input('Cálculadora para saber a quantidade que será necessário de tintas para pintar uma área. \n\nDigite o valor da parte VERTICAL: '))
val2 = float(input('Digite o valor ORIZONTAL:'))
som = val1 * val2
tin = som / 2

print("O tatal da sua área é de {:.2f}m² e serão necessários {:.3f}L de tintas, para uma pintura completa da área.".format(som, tin))
