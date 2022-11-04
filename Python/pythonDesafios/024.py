# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome "SANTO"

cidade = str(input('Digite o nome da cidade: ')).strip()
print(f'Começa com "SANTO"? ==> {cidade.upper().startswith("SANTO")}')
print(f'Começa com "SANTO"? ==> {cidade[0:5].upper() == "SANTO"}')
