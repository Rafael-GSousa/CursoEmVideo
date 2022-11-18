# cont = 1
# # Loop com condição de parada
# while cont <= 10:
#     print(cont, '->', end='')
#     cont += 1
# print('Acabou')

# # Loop infinito
# while True:
#     print(cont, '->', end='')
#     cont += 1
# print('Acabou')

# Loop infinito, com comando de interrupção 'break'
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s:=^20}')
print(f'{"A soma vale":=^20}')

