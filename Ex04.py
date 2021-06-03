#Utilizando funções e listas faça um programa
#que receba uma data no formato DD/MM/AAAA e 
#devolva uma string no formato DD de mesPorExtenso
#de AAAA. Opcional: valide a data e retorne 'data 
#inválida' caso a data seja inválida.

def extmes(dia, mes, ano):
    meses = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril',
    5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro',
    10: 'outubro', 11: 'novembro', 12: 'dezembro'}
    
    if dia not in range(0, 32) or mes not in range(1, 13) or ano < 0:
        print('Data inválida!')
    else:
        print(f'{dia} de {meses[mes]} de {ano}')


dia = int(input('Digite o dia: '))  
mes = int(input('Digite o mês: '))  
ano = int(input('Digite o ano: '))
print('*'*15)
extmes(dia, mes, ano)
