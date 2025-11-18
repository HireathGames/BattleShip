from Classes import Point
from Classes import Ship
import core_functions
import helper_functions
from draw_boards import print_unplayed_board

import copy
import random

# establishes ships and corresponding length
def get_available_ships():
    return {
            "carrier": Ship("Carrier", 5, 5, "c"),
            "battleship": Ship("Battleship", 4, 6, "b"),
            "submarine": Ship("Submarine", 3, 7, "s"),
            "cruiser": Ship("Cruiser", 3, 8, "r"),
            "destroyer": Ship("Destroyer", 2, 9, "d")
    }

player_grid = core_functions.intialize_grid()
reserve_ships = get_available_ships()
# defines how our coordinates function
def coord_to_index(coord):
    letters = "ABCDEFGHIJK"
    row = letters.index(coord[0].upper())
    col = int(coord[1:]) - 1 
    return row, col # sections off two parts of coordinate

# Boolean verifies placement is valid
def place_ship(grid, coord, direction, length, ship_id):
    row, col = coord_to_index(coord)
    max_index = len(grid) - 1

    # Check if placement is valid and doesn't overlap
    if direction == "up":
        if row - length + 1 < 0:
            print("\nNot enough space upward from that position.")
            return False
    elif direction == "down":
        if row + length - 1 > max_index:
            print("\nNot enough space downward from that position.")
            return False
    elif direction == "left":
        if col - length + 1 < 0:
            print("\nNot enough space to the left from that position.")
            return False
    elif direction == "right":
        if col + length - 1 > max_index:
            print("\nNot enough space to the right from that position.")
            return False
    else:
        print("\nInvalid direction. Choose up, down, left, or right.")
        return False

    # Check for overlap
    # Orion: I changed it from letters to actual names!
    for step in range(length): # step = each section of the ship through it's length
        vert, hori = row, col
        if direction == "up":
            vert -= step
        elif direction == "down":
            vert += step
        elif direction == "left":
            hori -= step
        elif direction == "right":
            hori += step

        temp = grid[vert][hori].get_ID()
        if grid[vert][hori].get_ID() != 0: # Will replace ≈ with whatever 
                                  # symbolizes open space
            print("\nOverlap detected — there's already a ship at that location.\n")
            return False 

    # Place the ship
    for step in range(length):
        vert, hori = row, col
        if direction == "up":
            vert -= step
        elif direction == "down":
            vert += step
        elif direction == "left":
            hori -= step
        elif direction == "right":
            hori += step

        grid[vert][hori].set_ID(ship_id)  # Will replace with whatever symbolizes
                         # occupying ship

    return True # If all verification passes, clear to place!
    
# Scaffolding for updating menu after every choice
def print_ship_menu(ships):
    print("+------------+--------+")
    print("| Ship Name  | Length |")
    print("+------------+--------+")
    for i, (name, ship_object) in enumerate(ships.items(), start=1):
        print(f"| {name.ljust(10)} | {str(ship_object.get_length()).center(6)} |")
    print("+------------+--------+")

# Prompts user to choose a ship
def get_ship_choice(ships):
    while True:
        ship_name = input("Choose a ship to place by name: ").strip().lower()
        if ship_name in ships.keys():
            return ships[ship_name]
        print("\nInvalid ship name. Try again.\n")

# Prompts user to choose a coordinate
def get_placement_details(ship):
    valid_coord = False
    valid_direction = False

    while not valid_coord:
        coord = input(f"Enter starting coordinate for {ship.get_name()} (e.g., B5): ").strip().upper()
        try:
            letter_coord = coord[0]
            number_coord = int(coord[1:])
        except:
            letter_coord = "p"
            number_coord = 0



        if (len(coord) in [2,3]) and (letter_coord in "ABCDEFGHIJK") and (1 <= number_coord <= 11):
            valid_coord = True
        else:
            print("Invalid coordinate! (Must be A through K for the first coordinate and 1-11 for the second)")
    while not valid_direction:
        direction = input("Enter direction (up, down, left, right): ").strip().lower()
        if direction in ["up","down","left","right"]:
            valid_direction = True
        else:
            print("Invalid direction!")

    return coord, direction

def run_ship_placement():
    # Simplifies our known information
    ships = get_available_ships()
    grid = core_functions.intialize_grid()

    print_grid(grid)
    # Loops updating menu and user choices
    while ships: 

        print_ship_menu(ships)
        ship = get_ship_choice(ships)

        ship_id = ship.get_ID()
        coord, direction = get_placement_details(ship)

        # Continues verifying as we receive prompts
        success = place_ship(grid, coord, direction, ship.get_length(), ship_id)
        if success: # STORE COORDINATE INFO ON EACH SHIP IN CLASS SOMEWHERE 
            del ships[ship.get_name().lower()] 
            print(f"{ship.get_name} placed.")
            print_grid(grid)
        else:
            print("\nInvalid placement. Try again.\n")

    return grid

# Enters info into updated grid
#Orion: I couldn't figure out how to make this part function so I kinda remade it, Sorry.
"""
def print_grid(grid):
    letters = "ABCDEFGHIJK"
    ship_grid = []
    for row in grid:
        temp = []
        for point in row:
            temp.append(point.get_ID())
        ship_grid.append(temp)
    for ind in range(len(ship_grid)):
        print (letters[ind] + " " + str(ship_grid[ind]))
"""

def print_grid(grid):

    print_unplayed_board(grid)



def generate_random_board(): # My random board generator I use for the AI
    board = [[0]*11 for _ in range(11)]
    ships = {5: 5, 6: 4, 7: 3, 8: 3, 9: 2}

    ships_placed_id = []
    ships_placed_len = []

    for ship_id, length in ships.items():
        valid_placement = False
        ships_placed_id.append(ship_id)
        ships_placed_len.append(length)

        while not valid_placement:
            grid = copy.deepcopy(board)
            grid_size = len(grid)

            if random.randint(0, 1) == 0:  # horizontal
                row = random.randint(0, grid_size-1)
                start_col = random.randint(0, grid_size-length)
                for i in range(length):
                    grid[row][start_col+i] = ship_id
            else:  # vertical
                col = random.randint(0, grid_size-1)
                start_row = random.randint(0, grid_size-length)
                for i in range(length):
                    grid[start_row+i][col] = ship_id

            if helper_functions.count_values(grid, ships_placed_id) == ships_placed_len:
                board = grid
                valid_placement = True

    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x] = Point(board[y][x], 0)

    return board


def do_demo():
    # Final output after all ships chosen, all choices made 
    # Orion: made a little thing just for debug.       
    player_grid = run_ship_placement()

    clean_grid = helper_functions.translate_point_to_grid(player_grid)
    print(clean_grid)

    print("Game Start!")
    while True:
        print_grid(player_grid)
        target = input("Please select a target: ")
        result = core_functions.select_target(target, player_grid)
        print(result[1])
        player_grid = result[0]
