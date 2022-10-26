larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
qtdNec = ((area / 20) * 10)
print(f'Altura = {alt:.2f} m \nLargura = {larg:.2f} m \nÁrea = {area:.2f} m²\nTinta necessária = {qtdNec:.2f} litro(s)')
