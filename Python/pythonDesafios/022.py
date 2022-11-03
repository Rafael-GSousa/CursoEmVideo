# Crie um programa que leia o nome completo de uma pessoa e mostre:
# ==> O nome com todas as letras maiúsculas
# ==> O nome com todas as letras minúsculas
# ==> Quantas letras no total (sem considerar os espaços)
# ==> Quantas letras tem o primeiro nome
nome = input('Digite um nome completo: ')
juntaNome = ""
for i in range(0, len(nome.split())):
    juntaNome = juntaNome + (nome.split()[i])
print(f"""Nome digitado ==> {nome}
Todas as letras maiúsculas ==> {nome.upper()}
Todas as letras minúsculas ==> {nome.lower()}
Quantas letras no total (sem os espaços) ==> {len(juntaNome)}
Quantas letras têm no primeiro nome ==> {len(nome.split()[0])}""")
