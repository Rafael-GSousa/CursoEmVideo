lista = list()
while True:
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continua in 'N':
        break
    print('-' * 30)
print('-=' * 40)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>5}')
print('-' * 20)
for posicao, aluno in enumerate(lista):
    print(f'{posicao:<5}{lista[posicao][0]:<10}{lista[posicao][2]:>5}')
print('-' * 20)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        print('FINALIZANDO...')
        break
    if mostrar <= len(lista) - 1:
        print(f'Notas de {lista[mostrar][0]} são {lista[mostrar][1]}')
    else:
        print('Aluno(a) não encontrado! Tente novamente...')
    print('-' * 30)
