# A Confederação Nacional de Natação precisa de um
# programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date
anoAtual = date.today().year

anoNasc = int(input('Digite o ano de nascimento do atleta: '))

idade = anoAtual - anoNasc
categoria = ''

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JÚNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f"""Idade do atleta ==> {idade} anos
Categoria do atleta ==> {categoria}""")
