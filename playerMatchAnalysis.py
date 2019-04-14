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

def filter_games(data,game_type):
    # games = []
    for match in data:
        if match['mode']['name'] == game_type:
            # games.append(match)
            yield match
    # return games

def extract_wins(data):
    # wins = []
    for match in data:
        win = match['winner']
        if win == -1:
            yield win
        else:
            yield 1
    # return wins

def ladder_summary(data):
    ladder_games = list(filter_games(data,'Ladder'))

    wins = list(extract_wins(data))
    win_loss_ratio = wins.count(1)/len(wins)

    trophy_change = []
    for match in ladder_games:
        trophy_change.append(match['team'][0]['trophyChange'])
    avg_trophy_movement = np.mean(np.abs(trophy_change))
    avg_trophy_gain = np.mean(trophy_change)

    print("For the last {:} ladder games:".format(len(list(ladder_games))))
    print("You have a {:.4f}% win rate.".format(win_loss_ratio))
    print("You have gained an average of {:.4f} trophies per game.".format(avg_trophy_gain))

ladder_summary(Cryp_data)
ladder_summary(Jin_data)

ladder = list(filter_games(Cryp_data,'Ladder'))
ladder[0]

# Strategy for organizing the data I want
from collections import defaultdict
matches = []
for match in ladder:
    d = defaultdict(list)
    for card in match['team'][0]['deck']:
        d['team_cards'].append(card['name'])

    for card in match['opponent'][0]['deck']:
        d['opponent_cards'].append(card['name'])

    d['win'] = match['winner']

    matches.append(d)
matches
