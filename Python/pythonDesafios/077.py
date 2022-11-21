# Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis',
         'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')
for i in tupla:
    print(f'Na palavra {i.upper()} temos ', end='')
    for j in i:
        if j in "AEIOUaeiou":
            print(j.lower(), end=' ')
    print('')
