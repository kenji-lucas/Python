#if, elif, else, while

#Exemplo 1: Encontre o maior entre 2 números.

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
if int(primeiro_numero) > int(segundo_numero):
    print('O primeiro número é maior!')
else:
    print('O segundo número é maior!')

#Exemplo 2: Gere um número aleatório de 1 a 20 e permita que o usuário chute até acertá-lo, informando se o chute foi maior, menor ou igual.

import random
numero_aleatorio = random.randint(1,20)
acertou = False
while acertou == False:
    chute = int(input('Chute um número de 1 a 20: '))
    if chute < numero_aleatorio:
        print('O chute foi muito baixo!')
    elif chute > numero_aleatorio:
        print('O chute foi muito alto!')
    elif chute == numero_aleatorio:
        acertou = True
        print('Você acertou!!!')