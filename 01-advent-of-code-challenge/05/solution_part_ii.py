from pathlib import Path

##setando o path do .in
script_location = Path(__file__).absolute().parent
file_location = script_location / 'day4.in'

#passando os dados para uma variavel e tratando o resultado
file = file_location.open()
data = [i for i in file.read().strip().split("\n")]
##IDK how i can solve this