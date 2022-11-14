# Refaça o desafio 035 dos triângulos, acrescentando
# o recurso de mostrar que tipo de triângulo será formado
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes
r1 = float(input('Comprimento da 1ª reta ==> '))
r2 = float(input('Comprimento da 2ª reta ==> '))
r3 = float(input('Comprimento da 3ª reta ==> '))

tipo = ''
msg = f'Será formado um triângulo do tipo {tipo}'

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    if r2 == r1 == r3:
        tipo = 'Equilátero, pois, todos os lados são iguais'
    elif r2 == r1 != r3 or r2 != r1 == r3 or r1 != r2 == r3:
        tipo = 'Isósceles, pois, apenas dois lados são iguais'
    else:
        tipo = 'Escaleno, pois, todos os lados são diferentes'
else:
    msg = 'Não se pode formar um triângulo com esses segmentos de reta'
print(msg + tipo)
