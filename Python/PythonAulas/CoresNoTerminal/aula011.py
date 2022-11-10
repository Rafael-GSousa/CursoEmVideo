# ANSI cores no terminal do python
# style = {'reset': '\033[0m',
#          'bold': '\033[01m',
#          'disable': '\033[02m',
#          'underline': '\033[04m',
#          'reverse': '\033[07m',
#          'invisible': '\033[08m',
#          'strikethrough': '\033[09m'}
# fontcolor = {'black': '\033[30m',
#              'red': '\033[31m',
#              'green': '\033[32m',
#              'orange': '\033[33m',
#              'blue': '\033[34m',
#              'purple': '\033[35m',
#              'cyan': '\033[36m',
#              'lightgrey': '\033[37m',
#              'darkgrey': '\033[90m',
#              'lightred': '\033[91m',
#              'lightgreen': '\033[92m',
#              'yellow': '\033[93m',
#              'lightblue': '\033[94m',
#              'pink': '\033[95m',
#              'lightcyan': '\033[96m'}
# background = {'black': '\033[40m',
#               'red': '\033[41m',
#               'green': '\033[42m',
#               'orange': '\033[43m',
#               'blue': '\033[44m',
#               'purple': '\033[45m',
#               'cyan': '\033[46m',
#               'lightgrey': '\033[47m'}
texto = str(input('Digite qualquer coisa: '))
estilo = int(input('Estilo do texto: '))
estilo = f'\033[{estilo}m'
cor = int(input('Cor do texto: '))
cor = f'\033[{cor}m'
fundo = int(input('Cor de fundo: '))
fundo = f'\033[{fundo}m'
print(f"""Normal ==> {texto}
Formatado ==> {estilo + cor + fundo + texto}\033[m""")
