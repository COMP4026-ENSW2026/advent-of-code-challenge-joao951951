from pathlib import Path

##setando o path do .in
script_location = Path(__file__).absolute().parent
file_location = script_location / 'day6.in'

#passando os dados para uma variavel e tratando o resultado
file = file_location.open()
data = file.read()

for char in range(14, len(data)):
    aux = {i for i in data[char-14:char]}
    if(len(aux) == 14):
        print("message will processed in char:",char)
        break