#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

#n1 = int(input('Digite um número inteiro para descobrir o seu ANTECESSOR e eu SUCESSOR: '))
#su = n1 + 1
#an = n1 - 1

#print("O numero digitado é {} e seu ANTECESSOR é o número {} e seu SUCESSOR é {}.".format(n1, an, su))

#CORREÇÃO NÃO UTILIZANDO VARIÁVEL

n1 = int(input('Digite um número inteiro para descobrir o seu ANTECESSOR e eu SUCESSOR: '))

print("O numero digitado é {} e seu ANTECESSOR é o número {} e seu SUCESSOR é {}.".format(n1, (n1-1),(n1+1)))