from Classes import Point
import Main

from draw_boards import print_unplayed_board

# establishes ships and corresponding length
def get_available_ships():
    return {
        "Destroyer": 2,
        "Submarine": 3,
        "Cruiser": 3,
        "Battleship": 4,
        "Carrier": 5
    }

player_grid = Main.intialize_grid()

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
    for i, (name, length) in enumerate(ships.items(), start=1):
        print(f"| {name.ljust(10)} | {str(length).center(6)} |")
    print("+------------+--------+")

# Prompts user to choose a ship
def get_ship_choice(ships):
    while True:
        ship_name = input("Choose a ship to place by name: ").strip().title()
        if ship_name in ships:
            return ship_name
        print("\nInvalid ship name. Try again.\n")

# Prompts user to choose a coordinate
def get_placement_details(ship_name):
    coord = input(f"Enter starting coordinate for {ship_name} (e.g., B5): ").strip().upper()
    # Prompts user for direction of ship FROM coordinate
    direction = input("Enter direction (up, down, left, right): ").strip().lower()
    return coord, direction

def run_ship_placement():
    # Simplifies our known information
    ships = get_available_ships()
    grid = Main.intialize_grid()
    ship_ids = {
        "destroyer": 9,
        "submarine": 7,
        "cruiser": 8,
        "battleship": 6,
        "carrier": 5
    }

    print_grid(grid)
    # Loops updating menu and user choices
    while ships:
        print_ship_menu(ships)
        ship = get_ship_choice(ships)
        ship_id = ship_ids[ship.lower()]
        coord, direction = get_placement_details(ship)

        # Continues verifying as we receive prompts
        success = place_ship(grid, coord, direction, ships[ship], ship_id)
        if success: # STORE COORDINATE INFO ON EACH SHIP IN CLASS SOMEWHERE 
            del ships[ship] 
            print(f"{ship} placed.")
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

# Final output after all ships chosen, all choices made 
# Orion: made a little thing just for debug.       
player_grid = run_ship_placement()
print("Game Start!")
while True:
    print_grid(player_grid)
    target = input("Please select a target: ")
    result = Main.select_target(target, player_grid)
    print(result[1])
    player_grid = result[0]
