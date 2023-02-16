from pathlib import Path
import string 

##setando o path do .in
script_location = Path(__file__).absolute().parent
file_location = script_location / 'day3.in'

#passando os dados para uma variavel e tratando o resultado
file = file_location.open()
data = [i for i in file.read().strip().split("\n")]

pts = list(string.ascii_lowercase)
auxPts = list(string.ascii_uppercase)
for i in auxPts:
    pts.append(i)
sumPts = 0

#Percorrendo o array e cada elemento no array para realizar  a comparação
for item in data:
    auxA = item[:int(len(item)/2)]
    auxB = item[int(len(item)/2):int(len(item))]
    for index,charA in enumerate(auxA):
        for indexB, charB in enumerate(auxB):
            if(charA == charB):
                sumPts += pts.index(charA) +1
                break
        if(charA == charB):
            break

print(sumPts)