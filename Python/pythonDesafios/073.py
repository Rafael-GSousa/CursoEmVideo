# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
tabela = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
          'Flamengo', 'Vasco', 'Chapecoense', 'Atlético - MG', 'Botafogo',
          'Atlético - PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
          'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético - GO')
print('-=' * 20)
print(f'Lista de times do Brasileirão 2018: {tabela}')
print('-=' * 20)
print(f'Os 5 primeiros são: {tabela[:5]}')
print('-=' * 20)
print(f'Os 4 útlimos são: {tabela[16:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 20)
print(f'A Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição')
