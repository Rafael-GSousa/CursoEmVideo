# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

entrada = input('Digite algo ==> ')
print(f'Tipo ==> {type(entrada)}\nMaiúscula ==> {entrada.isupper()}\nMinúscula ==> {entrada.islower()}'
      f'\nAlfanumérico ==> {entrada.isalnum()}\nAlfabético ==> {entrada.isalpha()}\nASCII ==> {entrada.isascii()}'
      f'\nDecimal ==> {entrada.isdecimal()}\nDígito ==> {entrada.isdigit()}\nIdentificador ==> {entrada.isidentifier()}'
      f'\nNumérico ==> {entrada.isnumeric()}\nImprimível ==> {entrada.isprintable()}\nEspaço ==> {entrada.isspace()}'
      f'\n1ª letra maiúscula ==> {entrada.istitle()}')
