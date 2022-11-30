from random import randint
# from time import sleep
dados = dict()
jogadores = list()
p = s = t = q = 0
cont = 1
for i in range(1, 5):
    dados['jogador', cont] = i
    dados['dado', cont] = randint(1, 6)
    # jogadores.append(dados.copy())
    print(f'O jogador {dados["jogador", cont]} tirou {dados["dado", cont]}')
    if cont == 1:
        p = s = t = q = dados['dado', cont]
    else:
        if dados['dado', cont] > p > s > t > q:
            p = dados['dado', cont]
        elif dados['dado', cont] < p > s > t > q:
            s = dados['dado', cont]
        elif dados['dado', cont] < p < s > t > q:
            t = dados['dado', cont]
        elif dados['dado', cont] < p < s < t > q:
            q = dados['dado', cont]
    cont += 1

    # print(dados)
    # print(jogadores)
    # for i in range(1, 5):
    # if i == 1:
    #     p = s = t = dados['dado', i]
    # else:
    #     if dados['dado', i] > p:
    #         p = dados['dado', i]
    #     elif dados['dado', i] > s:
    #         s = dados['dado', i]
    #     elif dados['dado', i] > t:
    #         t = dados['dado', i]
    #     else:
    #         q = dados['dado', i]
print(f'1 = {p}')
print(f'2 = {s}')
print(f'3 = {t}')
print(f'4 = {q}')
