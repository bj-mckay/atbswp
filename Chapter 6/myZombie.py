import zombiedice, random

class RandomRoller:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() 
        while diceRollResults is not None:
            if random.randint(1,2) == 1:
                diceRollResults = zombiedice.roll()
            else:
                break

class TwoBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() 
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() 
            else:
                break

class TwoGuns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() 
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun < 2:
                diceRollResults = zombiedice.roll() 
            else:
                break

class StopAtTwoGuns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() 
        shotgun = 0
        for i in range(random.randint(1,4)):
            shotgun += diceRollResults['shotgun']
            if shotgun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class MoreGunsThanBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() 
        shotgun = 0
        brains = 0        
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if brains < shotgun:
                break
            else:
                diceRollResults = zombiedice.roll()
zombies = (
    RandomRoller(name='Ranom Roller'),
    TwoBrains(name='Two Brains'),
    TwoGuns(name='Two Guns'),
    StopAtTwoGuns(name='Stop at two guns'),
    MoreGunsThanBrains(name='More guns than brains'),
    
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=10000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
