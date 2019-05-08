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

def get_match_data(path):
    data = []
    for filename in os.listdir(path):
        with open('{:}/{:}'.format(path,filename), 'r') as f:
            data.append(json.load(f)) # This is all of the data in the folder
    return data

Cryp_data = get_match_data("E:/DataSets/ClashRoyale/playerData/CrypticSl0th_98Y2CVV8")
Jin_data = get_match_data("E:/DataSets/ClashRoyale/playerData/Jinakaks_8020JC98P")

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

ladder_clean = clean_data(list(filter_games(Jin_data,'Ladder')))
card_winloss(ladder_clean,'Bowler')

def find_played_decks(data):
    l = []
    for game in data:
        deck = []
        for card in game['team'][0]['deck']:
            deck.append(card['name'])
        tf = []
        for d in l:
            tf.append(set(deck) == set(d))
        if True not in tf:
            l.append(deck)
    return l

played_decks = find_played_decks(filter_games(Cryp_data,'Ladder'))
played_decks

['1','2','3'] == ['1','3','2']


played_decks


ladder[0]['team'][0]['deck']
