# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos dígitos separados
# Ex.:
# Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = int(input('Digite um número de 0 a 9999: '))

# Para funcionar, o número precisa ser quebrado em unidade, dezena, centena e milhar da seguinte forma
# numero (variável) // (divisão inteira, duas barras) 1 (unidade... para dezena, centena e milhar é só
# acrescentar os zeros correspondentes após o 1) % 10 (resto da divisão por 10... é igual para as demais unidades)
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

# Mesmo que sejam apenas 2 números, onde não tem valor será mostrado zero
print(f"""Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {m}""")
