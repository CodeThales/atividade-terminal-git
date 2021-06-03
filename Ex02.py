#Utilizando estruturas de repetição com variável de controle,
#faça um programa que receba uma string com uma frase informada
#pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u 
#e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.
frase = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
print(frase)
print(f'A letra "a" aparece {frase.count("a")} vezes na frase.')
print(f'A letra "e" aparece {frase.count("e")} vezes na frase.')
print(f'A letra "i" aparece {frase.count("i")} vezes na frase.')
print(f'A letra "o" aparece {frase.count("o")} vezes na frase.')
print(f'A letra "u" aparece {frase.count("u")} vezes na frase.')
for vogais in frase:
    if 'a' in frase:
        frase = frase.replace('a', '')
    if 'e' in frase:
        frase = frase.replace('e', '')
    if 'i' in frase:
        frase = frase.replace('i', '')
    if 'o' in frase:
        frase = frase.replace('o', '')
    if 'u' in frase:
        frase = frase.replace('u', '')
print(f'A frase sem as vogais é: {frase}')
