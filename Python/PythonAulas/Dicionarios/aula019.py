pessoas = {'nome': 'Rafael', 'sexo': 'M', 'idade': 33}
print(pessoas)
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(f'O {pessoas["nome"]} é do sexo {pessoas["sexo"]} e tem {pessoas["idade"]} anos.')
for key in pessoas.keys():
    print(key)
for key, value in pessoas.items():
    print(f'{key} = {value}')
del pessoas['idade']
print(pessoas)
pessoas['nome'] = 'Leandro'
print(pessoas)
pessoas['peso'] = 98.5
print(pessoas)
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
print(estado1)
print(estado2)
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
estado = dict()
brasil1 = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip()
    estado['sigla'] = str(input('Sigla: ')).strip().upper()
    brasil1.append(estado.copy())
print(brasil1)
for e in brasil1:
    print(e)
for e in brasil1:
    for key, value in e.items():
        print(f'{key} ==> {value}', end=' ')
    print()
for e in brasil1:
    for valor in e.values():
        print(valor, end=' ')
    print()
