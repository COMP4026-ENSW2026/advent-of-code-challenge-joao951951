from pathlib import Path

##setando o path do .in
script_location = Path(__file__).absolute().parent
file_location = script_location / 'day5.in'

#passando os dados para uma variavel e tratando o resultado
file = file_location.open()
data, moves = (i.splitlines() for i in file.read().strip('\n').split('\n\n'))
print(data, moves)

# for i in data:
#     for char in i:
#         print(char)
    # print(i)
    # moves = i.split(" ")

# print(moves)
