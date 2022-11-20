# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
tabela1 = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro')
tabela2 = ('Flamengo', 'Vasco', 'Chapecoense', 'Atlético - MG', 'Botafogo')
tabela3 = ('Atlético - PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport')
tabela4 = ('Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético - GO')
tabela5 = tabela1 + tabela2 + tabela3 + tabela4
print('-=' * 20)
print(f'Lista de times do Brasileirão 2018: {tabela5}')
print('-=' * 20)
print(f'Os 5 primeiros são: {tabela5[:5]}')
print('-=' * 20)
print(f'Os 4 útlimos são: {tabela5[16:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(tabela5)}')
print('-=' * 20)
print(f'A Chapecoense está na {tabela5.index("Chapecoense") + 1}ª posição')
