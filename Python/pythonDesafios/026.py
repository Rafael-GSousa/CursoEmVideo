# Faça um programa que leia uma frase pelo teclado e mostre:
# ==> Quantas vezes aparece a letra "A"
# ==> Em que posição ela aparece a primeira vez
# ==> Em que posição ela aparece a última vez
frase = input('Digite uma frase: ')
print(f"""Quantas vezes aparece a letra "A" ==> {frase.count('A')} 
Em que posição ela aparece a primeira vez ==> {frase.find('A')} 
Em que posição ela aparece a última vez ==> {frase.rfind('A')}""")
