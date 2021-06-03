#Utilizando estruturas de repetição com teste lógico,
#faça um programa que peça uma senha para iniciar seu
#processamento, só deixe o usuário continuar se a senha
#estiver correta, após entrar dê boas vindas a seu usuário
#e apresente a ele o jogo da advinhação, onde o computador
#vai “pensar” em um número entre 0 e 10. O jogador vai tentar
#adivinhar qual número foi escolhido até acertar, 
#a cada palpite do usuário diga a ele se o número escolhido
#pelo computador é maior ou menor ao que ele palpitou,
#no final mostre quantos palpites foram necessários para vencer.
from random import randint
token = 666
validacao = False
while not validacao:
    senha = int(input('Digite sua senha para iniciar o jogo: '))
    if senha == token:
        validacao = True        
pc = randint(0, 10)
print('''Olá, meu nome é Stark. Sou uma inteligência artificial. 
Seja bem vind@. Eu acabei de pensar em um número entre 0 e 10.
Consegue adivinhar qual foi? ''')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Foi mais... Tente novamente:')
        elif jogador > pc:
            print('Foi menos... Tente novamente: ')
print(f'Você acertou com {palpites} tentativas. Parabéns!')
