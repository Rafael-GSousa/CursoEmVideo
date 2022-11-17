# Melhore o Desafio 061, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerra quando ele disser
# que quer mostrar 0 termos.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('1º termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
