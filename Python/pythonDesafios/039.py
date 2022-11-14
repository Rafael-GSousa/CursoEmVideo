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
    msg = f'''Quem nasceu em {anoNasc} tem {idade} anos em {anoAtual}.
Você já deveria ter se alistado há {tempo} ano(s).
Seu alistamento foi em {anoAtual - tempo}.'''
elif idade == 17:
    msg = f'''Quem nasceu em {anoNasc} tem {idade} anos.
Você tem que se alistar IMEDIATAMENTE!'''
else:
    msg = f'''Quem nasceu em {anoNasc} tem {idade} anos.
Ainda faltam {tempo * (-1)} anos para o alistamento.
Seu alistamento será em {anoAtual + tempo}.'''
print(msg)
