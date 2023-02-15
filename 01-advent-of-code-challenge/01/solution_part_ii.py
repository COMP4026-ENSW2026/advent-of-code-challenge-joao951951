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
elv1 = 0
elv2 = 0
elv3 = 0

#percorrendo array e fazendo as somas e comparações
for i in data :
    if(i != ''):
        num = int(i)
        aux += num
    else:
        if(aux > elv1):
            elv1 = aux
        elif(aux > elv2):
            elv2 = aux
        elif(aux > elv3):
            elv3 = aux
        aux = 0

print('First elv: ', elv1)
print("total calories of 3: ", elv1+elv2+elv3)