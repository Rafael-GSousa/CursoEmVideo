# # Crie um programa que leia vários números inteiros pela teclado.
# No final da execução, mostre a média entre todos os valores e qual
# foi o maior e o menor valores lidos. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.

opcao = 'S'
soma = maior = menor = media = cont = 0
while opcao != 'N':
    n = int(input('Digite um número: '))
    opcao = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print(f'Valores = {cont} | Soma = {soma} | Média = {media:.2f} | Maior = {maior} | Menor = {menor}')
