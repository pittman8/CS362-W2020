# -*- coding: utf-8 -*-
"""
Created on January 13th, 2020

@author: Hannah Pittman
"""

import Dominion
import random
from collections import defaultdict
import testUtility

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

#Define box
box = testUtility.TheBox(nV)

#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:10]
supply = defaultdict(list,[(k,box[k]) for k in random10])


#The supply always has these cards
supply = testUtility.TheSupply(supply, nV, nC, player_names)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.ThePlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1
    testUtility.PrintSupplyOrder(supply)
    testUtility.PrintPlayers(players, supply, trash, turn)

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners = testUtility.TheWinners(vp, vpmax)
print(dcs)