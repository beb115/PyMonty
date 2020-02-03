import random

runs = 10000
change = True
totalWins = 0

def game(change):
    rand = random.randint(0, 2)
    pickRand = random.randint(0, 2)
    door = [0, 0, 0]
    door[rand] = 1
    global totalWins

    pick = door[pickRand]

    if pick == 0:
        door.remove(0)
        if change == True:
            totalWins += 1
        elif change == False:
            pass

    if pick == 1:
        door.remove(0)
        if change == False:
            totalWins += 1
        elif change == True:
            pass

for i in range(runs):
    game(change)

loss = runs - totalWins
if change == True:
    print("You won " + str(totalWins) + " games and lost " + str(loss) + " changing")
else:
    print("You won " + str(totalWins) + " games and lost " + str(loss) + " not changing")
