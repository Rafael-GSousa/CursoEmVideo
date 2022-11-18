# # Crie um programa que leia vários números inteiros pela teclado.
# No final da execução, mostre a média entre todos os valores e qual
# foi o maior e o menor valores lidos. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.

opcao = 'S'
soma = maior = menor = media = cont = n = 0
while opcao in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Quer continuar? S/N: ')).strip().upper()[0]
media = soma / cont
print(f'Valores = {cont} | Soma = {soma} | Média = {media:.2f} | Maior = {maior} | Menor = {menor}')
