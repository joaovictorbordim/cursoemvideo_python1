# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.
n1 = float(input('Cálculadora de metros para CEMTIMETROS e MILÍMETROS. Digite uma medida em METROS: '))
cm = n1 * 100
mm = n1 * 1000

print('A medida em METROS é {} e sua conversão para {:.0f}cm e {:.0f}mm.'.format(n1, cm, mm))