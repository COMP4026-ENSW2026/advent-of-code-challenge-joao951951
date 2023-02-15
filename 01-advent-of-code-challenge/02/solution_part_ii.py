from pathlib import Path

##setando o path do .in
script_location = Path(__file__).absolute().parent
file_location = script_location / 'day2.in'

#passando os dados para uma variavel e tratando o resultado
file = file_location.open()
data = [i for i in file.read().strip().split("\n")]

#Possibilidades
# PT 2 
# X = LOSE 0pts , Y DRAW 3pts , Z WIN 6pts
#A v X = LOSE = 0 + 3 = 3 pts
#A v Y = DRAW = 3 + 1 = 4 pts
#A v Z = WIN = 2 + 6 = 8 pts
#B v X = LOSE = 1 + 0 = 1 pts
#B v Y = DRAW = 2 + 3 = 5 pts
#B v Z = WIN = 3 + 6 = 9 pts
#C v X = LOSE = 2 + 0 = 2 pts
#C v Y = DRAW = 3 + 3 = 6 pts
#C v Z = WIN = 6+1 = 7 pts


pts = {"A X":3, "A Y":4, "A Z": 8, "B X":1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
sumPts = 0
for round in data:
    sumPts += pts[round]

print("Result of sum pt2:",sumPts)