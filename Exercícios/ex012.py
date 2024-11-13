# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
# valor_porcentagem = valor * (percentual / 100)

val1 = float(input('CONSULTA DE DESCONTOS - HIPER MERCADO CURSO EM VÍDEO. \n\nDigite o valor do produto: '))
des = val1 * (5 / 100)
tot = val1 - des
print('O produto com o valor R${} terá um desconto de 5% ficando R${}'.format(val1, tot))
