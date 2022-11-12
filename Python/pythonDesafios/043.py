# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida
from math import pow
peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / pow(altura, 2)
resultado = ''
if imc < 18.5:
    resultado = 'Abaixo do peso'
elif 18.5 <= imc <= 25:
    resultado = 'Peso ideal'
elif 25 <= imc <= 30:
    resultado = 'Sobrepeso'
elif 30 <= imc <= 40:
    resultado = 'Obesidade'
else:
    resultado = 'Obesidade mórbida'

print(f"""Peso ==> {peso:.2f}
Altura ==> {altura:.2f}
IMC ==> {imc:.2f}
Resultado ==> {resultado}""")
