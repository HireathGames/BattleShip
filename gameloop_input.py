import core_functions
import ai_logic

coords_shot = []

# These are meant to be suer interchangable for debug purposes, they both input and output exactly the same format.

def get_player_shot(grid): # get input.

    valid_coord = False

    while not valid_coord:
        coord = input(f"Enter coordinate to shoot at. (Ex. C6)").strip().upper()
        try:
            letter_coord = coord[0]
            number_coord = int(coord[1:])
        except:
            continue

        if (len(coord) in [2,3]) and (letter_coord in "ABCDEFGHIJK") and (1 <= number_coord <= 11) and (coord not in coords_shot):
            valid_coord = True
            coords_shot.append(coord)
        else:
            print("Invalid coordinate! (Must be A through K for the first coordinate and 1-11 for the second) (No repeats!)")


    return core_functions.shoot_coordinate(grid,coord)


def get_ai_shot(grid): # performs the shot. 
    coord = ai_logic.call_ai(grid)

    return core_functions.shoot_coordinate(grid,coord)