##imports da lib para setar o path do arquivo .in de maneira dinamica
from pathlib import Path

##setando o path do .in
script_location = Path(__file__).absolute().parent
file_location = script_location / 'day1.in'

#passando os dados para uma variavel e tratando o resultado
file = file_location.open()
data = [i for i in file.read().strip().split("\n")]

#declarando auxiliares
aux = 0
max = 0

#percorrendo array e fazendo as somas e comparações
for i in data :
    if(i != ''):
        aux += int(i)
    else:
        aux = 0
    if(aux > max):
        max = aux

print(max)
