# Crie um programa que leia duas notas de um aluno
# e calcule a sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
aluno = str(input('Nome do(a) aluno(a) ==> '))
n1 = float(input(f'1ª nota do(a) aluno(a) {aluno} ==> '))
n2 = float(input(f'2ª nota do(a) aluno(a) {aluno}  ==> '))

media = (n1 + n2) / 2
msg = ''

if media < 5.0:
    msg = f"""Aluno(a) ==> {aluno}
1ª e 2ª nota ==> {n1:.1f} e {n2:.1f}
Média ==> {media:.1f}
Situação ==> REPROVADO(A)"""
elif 5.0 <= media <= 6.9:
    msg = f"""Aluno(a) ==> {aluno}
1ª e 2ª nota ==> {n1:.1f} e {n2:.1f}
Média ==> {media:.1f}
Situação ==> RECUPERAÇÃO"""
else:
    msg = f"""Aluno(a) ==> {aluno}
1ª e 2ª nota ==> {n1:.1f} e {n2:.1f}
Média ==> {media:.1f}
Situação ==> APROVADO(A)"""
print(msg)
