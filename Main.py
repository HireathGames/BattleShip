#Imports the Point class from Classes
from Classes import Point
import ship_placement
import board_generator
import core_functions
import draw_boards
import ai_logic
import helper_functions

import time
import copy


# moved the functions to core functions (because you can't import a file that imports your file, so main wouldn't be able to access any files that import main) -Trevor





player_grid = board_generator.generate_board_point()#ship_placement.run_ship_placement()
original_player_grid = copy.deepcopy(player_grid)

ai_grid = board_generator.generate_board_point()
original_ai_grid = copy.deepcopy(ai_grid)


lose = False
coords_shot = []

while lose == False:

    # player turn

    draw_boards.print_ai_board(original_ai_grid,ai_grid)

    valid_coord = False

    while not valid_coord:
        coord = input(f"Enter coordinate to shoot at. (Ex. C6)").strip().upper()
        letter_coord = coord[0]
        try:
            number_coord = int(coord[1:])
        except ValueError:
            number_coord = 0

        if (len(coord) in [2,3]) and (letter_coord in "ABCDEFGHIJK") and (1 <= number_coord <= 11) and (coord not in coords_shot):
            valid_coord = True
            coords_shot.append(coord)
        else:
            print("Invalid coordinate! (Must be A through K for the first coordinate and 1-11 for the second) (No repeats!)")

    #print(coord)
    
    status,ai_grid = core_functions.check_coordinate(ai_grid,coord)

    #print(status)


    draw_boards.print_ai_board(original_ai_grid,ai_grid)

    if status == -1:
        print("\nYou missed...")
    elif status == 1: 
        print("\nYou hit a ship!")

    

    time.sleep(2)

    draw_boards.print_player_board(original_player_grid,player_grid)


    print("Ai is making its shot")

    time.sleep(2)

    ai_coords = ai_logic.call_ai(helper_functions.translate_point_to_grid(player_grid))
    print(ai_coords)

    status,player_grid = core_functions.check_ai_coordinate(player_grid,ai_coords)



    draw_boards.print_player_board(original_player_grid,player_grid)

    if status == -1:
        print("\nThe AI missed!")
    elif status == 1: 
        print("\nThe AI hit a ship...")

    time.sleep(3)






    



