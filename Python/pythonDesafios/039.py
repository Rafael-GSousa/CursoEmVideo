# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora dele se alistar.
# - Se ele já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.

from datetime import date
anoAtual = date.today().year

anoNasc = int(input('Digite seu ano de nascimento: '))
idade = anoAtual - anoNasc

msg = ''
tempo = idade - 17

if idade > 17:
    msg = f'Você já passou em {tempo} ano(s) do prazo de alistamento.'
elif idade == 17:
    msg = f'Você está com {idade} anos e já está na hora de se alistar.'
else:
    msg = f'Não chegou sua hora de se alistar, ainda falta(m) {tempo * (-1)} ano(s).'
print(msg)
