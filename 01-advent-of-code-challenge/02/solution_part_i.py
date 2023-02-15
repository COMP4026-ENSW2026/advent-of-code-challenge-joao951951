from pathlib import Path

##setando o path do .in
script_location = Path(__file__).absolute().parent
file_location = script_location / 'day2.in'

#passando os dados para uma variavel e tratando o resultado
file = file_location.open()
data = [i for i in file.read().strip().split("\n")]

#Possibilidades
#A v X = 1+3 = 4 pts
#A v Y = 2+6 = 8 pts
#A v Z = 3+0 = 3 pts
#B v X = 1+0 = 1 pts
#B v Y = 2+3 = 5 pts
#B v Z = 3+6 = 9 pts
#C v X = 1+6 = 7 pts
#C v Y = 2+0 = 2 pts
#C v Z = 3+3 = 6 pts

pts = {"A X":4, "A Y":8, "A Z": 3, "B X":1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
sumPts = 0
for round in data:
    sumPts += pts[round]

print("Result of sum:",sumPts)