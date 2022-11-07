# nome = str(input('Qual é o seu nome? '))
# if nome == 'Gustavo':
#     print('Que lindo nome você tem!')
# else:
#     print('Seu nome é tão normal!')
# print(f'Bom dia, {nome}!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua média foi {media:.2f}')
# condição simplificada (igual operador ternário do Java)
print('PARABÉNS!' if media >= 6 else 'ESTUDE MAIS!')
# condição normal composta
if media >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')
