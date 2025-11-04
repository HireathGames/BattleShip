#Imports the Point class from Classes
from Classes import Point
import ship_placement
import board_generator
import core_functions
import draw_boards

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

        if (len(coord) in [2,3]) and (letter_coord in "ABCDEFGHIJK") and (1 <= number_coord <= 11):
            valid_coord = True
            coords_shot.append(coord)
        else:
            print("Invalid coordinate! (Must be A through K for the first coordinate and 1-11 for the second)")

    print(coord)
    
    status,ai_grid = core_functions.check_coordinate(ai_grid,coord)

    print(status)

    draw_boards.print_ai_board(original_ai_grid,ai_grid)