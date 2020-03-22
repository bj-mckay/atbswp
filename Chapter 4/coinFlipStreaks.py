import random

numberOfStreaks = 0
flipResults = []
streakNumber = 0

for experimentNumber in range(10000):
    for flips in range(100):
        flip = random.randint(0,1)
        if flip == 0:
            flipResults.append('H')
        else:
            flipResults.append('T')
    for i in range(len(flipResults)):
        if flipResults[i] == flipResults[i - 1]:
            streakNumber += 1
            if streakNumber >= 6:
                numberOfStreaks += 1
                streakNumber = 0
        else:
            streakNumber = 0

    flipResults = []

print('Chance of streak: %s%%' % (numberOfStreaks / 100))


print(experimentNumber)