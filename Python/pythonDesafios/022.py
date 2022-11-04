# Crie um programa que leia o nome completo de uma pessoa e mostre:
# ==> O nome com todas as letras maiúsculas
# ==> O nome com todas as letras minúsculas
# ==> Quantas letras no total (sem considerar os espaços)
# ==> Quantas letras tem o primeiro nome

# Entrada de dados pelo teclado
# Utilizando o método strip() para eliminar os espaços antes e depois da string logo na entrada
# por isso o input deve ser explicitado como string
nome = str(input('Digite um nome completo: ')).strip()

# # Variável alternativa para juntar um nome com ou outro que serão quebrados no método split()
# juntaNome = ""
#
# # estrutura de repetição para quebrar o nome no split e depois concatenar suas posições
# for i in range(0, len(nome.split())):
#     juntaNome = juntaNome + (nome.split()[i])

# mostrando na tela os resultados
# utilizando um único print com 3 aspas duplas sem necessidade de usar quebra de linha
print(f"""Nome digitado ==> {nome}
Todas as letras maiúsculas ==> {nome.upper()}
Todas as letras minúsculas ==> {nome.lower()}
Quantas letras no total (sem os espaços) ==> {len(nome) - nome.count(" ")}
Quantas letras têm no primeiro nome ==> {len(nome.split()[0])}""")


# Abaixo seria usado na linha 25
# Quantas letras têm no primeiro nome ==> {nome.find(" ")}
# O método find encontraria a posição do 1º espaço que também seria o total de letras do 1º nome

# Abaixo seria usado na linha 24
# Quantas letras no total (sem os espaços) ==> {len(juntaNome)}
# Obs.: na linha 24 foi utilizado o tamanho da string menos a quantidade
# de espaços que foram contados com o método count()
