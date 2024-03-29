#!/usr/bin/env python3

from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):
            self.dice.append(randint(1,6))

    def get_dice(self):
        return self.dice

class Cheat_Swapper(Player):
    def cheat(self):
        self.dice[-1] = 6

class Cheat_Loaded_Dice(Player):
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1   

from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

cheater1 = Cheat_Swapper()
cheater2 = Cheat_Loaded_Dice()

cheater1.roll()
cheater2.roll()

cheater1.cheat()
cheater2.cheat()

print("Cheater 1 rolled" + str(cheater1.get_dice()))
print("Cheater 2 rolled" + str(cheater2.get_dice()))

if sum(cheater1.get_ice()) == sum(cheater2.get_dice()):
    print("Draw!")

elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
    print("Cheater 1 wins!")

else:
    print("Cheater 2 wins!")

