# Crie um programa que leia o nome completo de uma pessoa e mostre:
# ==> O nome com todas as letras maiúsculas
# ==> O nome com todas as letras minúsculas
# ==> Quantas letras no total (sem considerar os espaços)
# ==> Quantas letras tem o primeiro nome

# Entrada de dados pelo teclado
nome = input('Digite um nome completo: ')

# Variável alternativa para juntar um nome com ou outro que serão quebrados no método split()
juntaNome = ""

# estrutura de repetição para quebrar o nome no split e depois concatenar suas posições
for i in range(0, len(nome.split())):
    juntaNome = juntaNome + (nome.split()[i])

# mostrando na tela os resultados
# utilizando um único print com 3 aspas duplas sem necessidade de usar quebra de linha
print(f"""Nome digitado ==> {nome}
Todas as letras maiúsculas ==> {nome.upper()}
Todas as letras minúsculas ==> {nome.lower()}
Quantas letras no total (sem os espaços) ==> {len(juntaNome)}
Quantas letras têm no primeiro nome ==> {len(nome.split()[0])}""")
