import json
import os
import glob
import numpy as np
os.chdir("C:/Github/ClashRoyale-Exploration") # For Atom Hydrogen

# with open('datadumps/playerData/1554943658-MirrorDeck.json', 'r') as f:
#      data = json.load(f)
#
# for filename in os.listdir("datadumps/playerData"):
#     print(filename)

# ladder_games = glob.glob("datadumps/playerData/*Ladder.json")
# ladder_games = [x.replace("\\","/") for x in ladder_games]
# ladder_games
for filename in os.listdir("datadumps/playerData/CrypticSl0th_98Y2CVV8"):
    with open('datadumps/playerData/CrypticSl0th_98Y2CVV8/{:}'.format(filename), 'r') as f:
        Cryp_data = json.load(f) # This is all of the data in the folder

for filename in os.listdir("datadumps/playerData/Jinakaks_8020JC98P"):
    with open('datadumps/playerData/Jinakaks_8020JC98P/{:}'.format(filename), 'r') as f:
        Jin_data = json.load(f) # This is all of the data in the folder

def ladder_summary(data):
    ladder_games = []
    for match in data:
        if match['mode']['name'] == 'Ladder':
            ladder_games.append(match)

    wins = []
    for match in ladder_games:
        win = match['winner']
        if win == -1: # Correct for match['winner'] saying either 2 or 3 instead of 1 for wins
            wins.append(win)
        else:
            wins.append(1)
    print(wins)
    win_loss_ratio = wins.count(1)/len(wins)

    trophy_change = []
    for match in ladder_games:
        trophy_change.append(match['team'][0]['trophyChange'])
    avg_trophy_movement = np.mean(np.abs(trophy_change))
    avg_trophy_gain = np.mean(trophy_change)

    print("For the last {:} ladder games:".format(len(ladder_games)))
    print("You have a {:.4f}% win rate.".format(win_loss_ratio))
    print("You have gained an average of {:.4f} trophies per game.".format(avg_trophy_gain))
    print(wins)
    print(trophy_change)

ladder_summary(Cryp_data)
ladder_summary(Jin_data)
