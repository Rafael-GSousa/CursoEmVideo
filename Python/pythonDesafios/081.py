lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if continua in 'N':
        break
print(f'Você digitou os valores: {lista}')
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'Lista ordenada de forma decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado!')
else:
    print(f'O valor 5 não foi digitado!')
