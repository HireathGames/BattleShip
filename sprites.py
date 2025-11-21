import json
import os


_json_path = os.path.join(os.path.dirname(__file__), "sprites.json")

with open(_json_path, "r") as f: # open the sprites folder 
    ships = json.load(f)


def get_sprite(id): #gets the sprite from a string ID format
    ship = id[0]
    orient = id[1]
    part = id[2]
    sprite_line = id[3]

    return ships[ship][orient][part][sprite_line]


 
connectors = { #the connectors for each type of ship
    "c":{"v": " ||+|| ", "h": ["=","+","="]},
    "b":{"v": " |[¤]| ", "h": ["‾","¤","_"]},
    "s":{"v": " | ~ | ", "h": ["‾","=","_"]},
    "r":{"v": " | ^ | ", "h": ["‾","<","_"]},
    "d":{"v": " |= =| ", "h": ["‾","║","_"]}    
}


 
def get_connector(id,sprite_y=0):
    ship = id[0] 
    orient = id[1]

    if orient == "h": return connectors[ship][orient][sprite_y]
    else: return connectors[ship][orient]

