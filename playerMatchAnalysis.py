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
Cryp_data = []
for filename in os.listdir("datadumps/playerData/CrypticSl0th_98Y2CVV8"):
    with open('datadumps/playerData/CrypticSl0th_98Y2CVV8/{:}'.format(filename), 'r') as f:
        Cryp_data.append(json.load(f)) # This is all of the data in the folder

Jin_data = []
for filename in os.listdir("datadumps/playerData/Jinakaks_8020JC98P"):
    with open('datadumps/playerData/Jinakaks_8020JC98P/{:}'.format(filename), 'r') as f:
        Jin_data.append(json.load(f)) # This is all of the data in the folder

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

Cryp_data[0]
def ladder_summary(data):
    ladder_games = list(filter_games(data,'Ladder'))

    wins = list(extract_wins(data))
    win_loss_ratio = wins.count(1)/len(wins)

    # No longer have 'trophyChange' data for each match
    # trophy_change = []
    # for match in ladder_games:
    #     trophy_change.append(match['team'][0]['trophyChange'])
    # avg_trophy_movement = np.mean(np.abs(trophy_change))
    # avg_trophy_gain = np.mean(trophy_change)

    print("For the last {:} ladder games:".format(len(list(ladder_games))))
    print("You have a {:.4f}% win rate.".format(win_loss_ratio))
    # print("You have gained an average of {:.4f} trophies per game.".format(avg_trophy_gain))

ladder_summary(Cryp_data)
ladder_summary(Jin_data)

ladder = list(filter_games(Cryp_data,'Ladder'))
ladder[0]

# Strategy for organizing the data I want
from collections import defaultdict

def clean_data(data):
    matches = []
    for match in data:
        d = defaultdict(list)
        for card in match['team'][0]['deck']:
            d['team_cards'].append(card['name'])

        for card in match['opponent'][0]['deck']:
            d['opponent_cards'].append(card['name'])

        d['win'] = match['winner']

        matches.append(d)
    return matches

def card_winloss(clean_matches,card_search):
    d = defaultdict(list)
    for match in clean_matches:
        if match['win'] > 0:
            win = 1
        if match['win'] < 0:
            win = -1
        if match['win'] == 0:
            win = 0
        for card in match['opponent_cards']:
            d[card].append(win)
    card_winrate = np.mean([0 if i < 0 else i for i in d[card_search]])
    return card_winrate

ladder_clean = clean_data(ladder)
card_winloss(ladder_clean,'P.E.K.K.A')
card_winloss(ladder_clean,'Fireball')
