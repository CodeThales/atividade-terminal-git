#Refatore o exercício 2, para que uma função receba a frase,
#faça todo o tratamento necessário e retorne o resultado. 
#Depois mostre na tela o resultado e a quantidade de letras
#que foram retiradas da frase original.
def tiravogal(frase):
    print(frase)
    print(f'A letra "a" aparece {frase.count("a")} vezes na frase.')
    print(f'A letra "e" aparece {frase.count("e")} vezes na frase.')
    print(f'A letra "i" aparece {frase.count("i")} vezes na frase.')
    print(f'A letra "o" aparece {frase.count("o")} vezes na frase.')
    print(f'A letra "u" aparece {frase.count("u")} vezes na frase.')
    letras = frase.count('a') + frase.count("e") + frase.count("i") + frase.count("o") + frase.count("u")
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
    print(f'Foram retiradas {letras} letras da frase original.')


frase = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
tiravogal(frase)
