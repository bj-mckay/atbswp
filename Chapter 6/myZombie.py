from . import ICON, SHOTGUN, COLOR, BRAINS, roll, rollDie
import BRAINS
import zombiedice
import random


class MyZombie:
    def __init__(self, name, minBrains=2) :
        # All zombies must have a name:
        self.name = name
        self.minBrains = minBrains

    def turn(self, gameState):
        # A bot that, after the first roll, randomly decides if it will continue or stop
        diceRollResults = zombiedice.roll()
        while diceRollResults and random.randint(0, 1) == 0:
            diceRollResults = zombiedice.roll()
        # A bot that stops rolling after it has rolled two brains
        brains = 0 # number of brains rolled this turn
        while brains < self.minBrains:
            diceRollResults = zombiedice.roll()

            if diceRollResults is None:
                return

            brains += diceRollResults[BRAIN] # increase brains by the number of brains die rolls.
        



zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=100)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
