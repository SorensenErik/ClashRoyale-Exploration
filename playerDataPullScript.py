import json
import os
#os.chdir("C:/GitHub/ClashRoyale-Exploration") # For Hydrogen Atom
from apiaccess import make_request

path = 'D:/DataSets/ClashRoyale/playerData/'
data_98Y2CVV8 = make_request("https://api.royaleapi.com/player/98Y2CVV8/battles")
data_8020JC98P = make_request("https://api.royaleapi.com/player/8020JC98P/battles")

def save_player_data(path,data,dirname):
    # Make dir if not exists
    if not os.path.exists('{:}{:}'.format(path,dirname)):
        os.makedirs('{:}{:}'.format(path,dirname))
    # Write the data in that directory
    for match in data:
        game_mode = match['mode']['name']
        utcTime = match['utcTime']
        with open('{:}{:}/{:}-{:}.json'.format(path,dirname,utcTime,game_mode),'w') as outfile:
            json.dump(match, outfile)

save_player_data(path,data_98Y2CVV8,"CrypticSl0th_98Y2CVV8")
save_player_data(path,data_8020JC98P,"Jinakaks_8020JC98P")
