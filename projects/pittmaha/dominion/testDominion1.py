# -*- coding: utf-8 -*-
"""
Created on January 13th, 2020

@author: Hannah Pittman
"""

import Dominion
import testUtility

# Get player names
player_names = ["Annie", "*Ben", "*Carla"]

# number of curses and victory cards
nV = testUtility.GetVictoryCards(player_names)
nC = testUtility.GetCurses(player_names)

# Define box
box = testUtility.TheBox(nV - nC)

# Pick 10 cards from box to be in the supply.
# The supply always has these cards
supply = testUtility.TheSupply(box, nV, nC, player_names)
supply_order = testUtility.PrintSupplyOrder()

for value in supply_order:
    print(value)
    for stack in supply_order[value]:
        if stack in supply:
            print(stack, len(supply[stack]))

# initialize the trash
trash = []

# Costruct the Player objects
players = testUtility.ThePlayers()

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    testUtility.PrintSupplyOrder()
    testUtility.PrintPlayers(players, supply, trash, turn)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = testUtility.TheWinners(vp, vpmax)
print(dcs)
