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

j = 3
for i in range(0, len(data), 3):
    sacks = data[i:j]
    j += 3
    for i in sacks:
        for char in i:
            if char in sacks[0] and char in sacks [1] and char in sacks [2]:
                sumPts += pts.index(char) +1
                break
        if char in sacks[0] and char in sacks [1] and char in sacks [2]:
            break
print(sumPts)