#FAZENDO UMA ALTERAÇÃO DE TESTE!
#Utilizando estruturas condicionais faça um programa
#que pergunte ao usuário dois números e mostre:
# A soma deles;
# A multiplicação entre eles;
# A divisão inteira deles;
# Mostre na tela qual é o maior;
# Verifique se o resultado da soma é par ou impar
# e mostre na tela;
# Se a multiplicação entre eles for maior que 40, 
# divida pelo resultado da divisão inteira e mostre o 
# resultado na tela. Se não, mostre que a multiplicação
#não foi maior que 40.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
mult = n1 * n2
div = n1 // n2
print(f'A soma entre {n1} e {n2} é: {soma}')
print(f'O resultado da multiplicação entre {n1} e {n2} é: {mult}')
print(f'O resultado da divisão inteira entre {n1} e {n2} é: {div}')
if n1 > n2:
    maior = n1
    print(f'{n1} é MAIOR que {n2}')
elif n2 > n1:
    maior = n2
    print(f'{n2} é MAIOR que {n1}')
else:
    print('Os valores são IGUAIS, por isso não há maior.')
if soma % 2 == 0:
    print(f'A soma entre {n1} e {n2} é: {soma}. {soma} é um número PAR.')
else:
    print(f'A soma entre {n1} e {n2} é: {soma}. {soma} é um número ÍMPAR.')
if mult > 40:
    try:
        resmd = mult / div
    except ZeroDivisionError:
        resmd = 0
        print(f'O resultado da multiplicação foi {mult}. O resultado da divisão inteira foi {div}. Por isso, o resultado da divisão entre estes resultados é {resmd}')
else:
    print(f'O resultado da multiplicação entre {n1} e {n2} foi menor que 40.')
