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
for filename in os.listdir("datadumps/playerData"):
    with open('datadumps/playerData/{:}'.format(filename), 'r') as f:
        data = json.load(f) # This is all of the data in the folder

def ladder_summary():
    ladder_games = []
    for match in data:
        if match['mode']['name'] == 'Ladder':
            ladder_games.append(match)

    wins = []
    for match in ladder_games:
        wins.append(match['winner'])
    win_loss_ratio = wins.count(1)/len(wins)

    trophy_change = []
    for match in ladder_games:
        trophy_change.append(match['team'][0]['trophyChange'])
    avg_trophy_movement = np.mean(np.abs(trophy_change))
    avg_trophy_gain = np.mean(trophy_change)

    print("For the last {:} ladder games:".format(len(ladder_games)))
    print("You have a {:.4f}% win rate.".format(win_loss_ratio))
    print("You have gained an average of {:.4f} trophies per game.".format(avg_trophy_gain))

ladder_summary()
