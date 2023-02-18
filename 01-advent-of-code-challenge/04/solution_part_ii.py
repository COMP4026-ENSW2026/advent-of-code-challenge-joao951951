from pathlib import Path
import string 

##setando o path do .in
script_location = Path(__file__).absolute().parent
file_location = script_location / 'day4.in'

#passando os dados para uma variavel e tratando o resultado
file = file_location.open()
data = [i for i in file.read().strip().split("\n")]

sumPairs = 0

for i in data:
    i, j = i.split(",")
    i = [int(x) for x in i.split("-")]
    j = [int(x) for x in j.split("-")]   
    # print(i,j)
    for char in range(i[0],i[1]+1):
        if char in range(j[0],j[1]+1):
            sumPairs +=1
            break
print(sumPairs)