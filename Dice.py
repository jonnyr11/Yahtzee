import random


def dice_roll(NumDice):
    count = 0
    a = []
    while (count < NumDice):
        a.append(random.randint(1, 6))
        count = count + 1
    return (a)


roll = input('Would you like to roll the dice ? yes/no ')

NumDice = 5 #int(input('How many dice would you like to roll? '))

rollcount = 0

dicehand = []

while roll == 'yes' and rollcount < 5:
    newdice = list(dice_roll(NumDice))
    print(newdice)

    for dice in newdice:
        dicehand.append(dice)

    print (dicehand)

    reroll = list(input('Which dice would you like to re-roll?')) #this is not comming in a lsit nicely

    print(reroll)

    print(dicehand)

    for x in reroll:
        while True:
            try:
                dicehand.remove(int(x))
            except:
                break


    print(dicehand)

    roll = input('Would you like to roll again? yes/no ')

    NumDice = len(reroll) # sum is wrong as its lenght is how many we are getting rid of

    rollcount += 1


print('Game over')
