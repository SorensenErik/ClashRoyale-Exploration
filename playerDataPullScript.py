import json
import os
os.chdir("C:/GitHub/ClashRoyale-Exploration") # For Hydrogen Atom
from apiaccess import make_request

data = make_request("https://api.royaleapi.com/player/98Y2CVV8/battles")

def save_data(data):
    for match in data:
        game_mode = match['mode']['name']
        utcTime = match['utcTime']
        with open('datadumps/playerData/{:}-{:}.json'.format(utcTime,game_mode),'w') as outfile:
            json.dump(data, outfile)

save_data(data)
