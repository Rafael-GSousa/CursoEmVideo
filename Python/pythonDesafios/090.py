aluno = {}
nome = str(input('Nome: ')).strip()
aluno['nome'] = nome
media = float(input(f'Média de {nome}: '))
aluno['media'] = media
if media >= 6:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
aluno['situacao'] = situacao
print(f'''Nome é igual a {aluno["nome"]}
Média é igual a {aluno["media"]:.1f}
Situação é igual a {aluno["situacao"]}''')
