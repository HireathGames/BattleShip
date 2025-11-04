"""
5 ships

Carrier: length 5, id: 5
battleship: length 4, id: 6
submarine: length 3, id: 7
cruiser: length 3, id: 8
destroyer: length 2, id: 9

  
"""
from Classes import Point
 

# To print player's board, just use print_my_board(old_grid,new_grid)


import helper_functions

import copy 
import sprites
import board_generator

# vertical id = "v", horiz id = "h"
# top/left id = 0, middle id = 1, bottom/right id = 2



# Carrier, type 5, length 5, "c"

# Battleship, type 6, length 4, "b"

# Submarine, type 7, length 3, "s"

# Cruiser, type 8, length 3, "r"

# Destroyer, type 9, length 2, "d"


def safe_index(grid,y,x):
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        return grid[y][x]
    return 0


def print_player_board(grid,new_grid):
    ui_grid = get_ui_grid(grid,new_grid)
    my_board(ui_grid)




def print_unplayed_board(grid):
    grid = helper_functions.translate_point_to_grid(grid)
    ui_grid = get_ui_grid(grid,grid)
    my_board(ui_grid)


def print_ai_board(grid,new_grid):
    grid = helper_functions.translate_point_to_grid(grid)
    new_grid = helper_functions.translate_point_to_grid(new_grid)

    ui_grid = get_hidden_ui_grid(grid,new_grid)
    my_board(ui_grid)




def get_ui_grid(grid,new_grid):
    # check for beginnings of horiz ships
    type_ids = "01234cbsrd" #0-4 are dummy characters as padding to index the others

    edit_grid = copy.deepcopy(grid)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            center = safe_index(grid,y,x)
            top = safe_index(grid,y-1,x)
            bottom = safe_index(grid,y+1,x)
            left = safe_index(grid,y,x-1)
            right = safe_index(grid,y,x+1)
            if not center == 0:
                if center == bottom == top: edit_grid[y][x]=f"{type_ids[grid[y][x]]}v1"
                elif center == bottom: edit_grid[y][x]=f"{type_ids[grid[y][x]]}v0"
                elif center == top: edit_grid[y][x]=f"{type_ids[grid[y][x]]}v2"
                else:
                    if center == left == right: edit_grid[y][x]=f"{type_ids[grid[y][x]]}h1"
                    elif center == left: edit_grid[y][x]=f"{type_ids[grid[y][x]]}h0"
                    elif center == right: edit_grid[y][x]=f"{type_ids[grid[y][x]]}h2"
            else:
                edit_grid[y][x]="   "


            
            if new_grid[y][x] == 1:
                edit_grid[y][x] = "mv0"
            elif new_grid[y][x]!=abs(new_grid[y][x]):
                if sum(board_generator.count_values(new_grid,[abs(new_grid[y][x])]))==0:
                    edit_grid[y][x] = "gv0"
                else:
                    edit_grid[y][x]="hv0"

    return edit_grid
            


def get_hidden_ui_grid(grid,new_grid):
    # check for beginnings of horiz ships
    type_ids = "01234cbsrd" #0-4 are dummy characters as padding to index the others

    edit_grid = copy.deepcopy(grid)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            center = safe_index(grid,y,x)
            top = safe_index(grid,y-1,x)
            bottom = safe_index(grid,y+1,x)
            left = safe_index(grid,y,x-1)
            right = safe_index(grid,y,x+1)
            if not center == 0:
                if center == bottom == top: edit_grid[y][x]=f"{type_ids[grid[y][x]]}v1"
                elif center == bottom: edit_grid[y][x]=f"{type_ids[grid[y][x]]}v0"
                elif center == top: edit_grid[y][x]=f"{type_ids[grid[y][x]]}v2"
                else:
                    if center == left == right: edit_grid[y][x]=f"{type_ids[grid[y][x]]}h1"
                    elif center == left: edit_grid[y][x]=f"{type_ids[grid[y][x]]}h0"
                    elif center == right: edit_grid[y][x]=f"{type_ids[grid[y][x]]}h2"
            else:
                edit_grid[y][x]="   "


            
            if new_grid[y][x] == 1:
                edit_grid[y][x] = "mv0"
            elif new_grid[y][x]!=abs(new_grid[y][x]):
                if sum(board_generator.count_values(new_grid,[abs(new_grid[y][x])]))==0:
                    edit_grid[y][x] = "gv0"
                else:
                    edit_grid[y][x]="hv0"
                    
            if not edit_grid[y][x][0] in ["m","g","h"]:
                edit_grid[y][x] = "   "

    return edit_grid
            



def my_board(ui_grid):
    """
    all pipe characters:
    ═  ║  ╔  ╗  ╚  ╝  ╠  ╣  ╦  ╩  ╬
    """

    print_nr = lambda i: print(i,end="") #print no return, aka print_nr

    alpha = "ABCDEFGHIJK"

    cols = 11
    rows = 11
    sprite_height = 3 
    sprite_width = 7



    print_nr("   ")
    for i in range(cols):
        print_nr(f"    {i+1}  ")
        if len(str(i+1))<2: print_nr(" ")


    print()


    print_nr("   ╔")
    for i in range(rows-1):
        print_nr("═"*sprite_width+"╦")
    print("═"*sprite_width+"╗")

    for y in range(cols):
        for sprite_y in range(sprite_height):
            if sprite_y==1:
                print_nr(alpha[y]+"  ")
            else:
                print_nr("   ")
            for x in range(rows):
                
                center = str(safe_index(ui_grid,y,x))
                left = str(safe_index(ui_grid,y,x-1))

                if left[:1]==center[:1] and center!="   " and (center[0] not in ["m","g","h"]):
                    print_nr(sprites.get_connector((ui_grid[y][x])[:1]+"h",sprite_y=sprite_y))
                else:
                    print_nr("║")

                    

                if center == "   ": 
                    print_nr(" "*sprite_width)
                else:
                    print_nr(sprites.get_sprite(ui_grid[y][x]+str(sprite_y)))
            print("║")

        
        if y<10:
            print_nr("   ╠")
            for x in range(cols):
                center = str(safe_index(ui_grid,y,x))
                bottom = str(safe_index(ui_grid,y+1,x))

                if bottom[:1]==center[:1] and center!="   " and (center[0] not in ["m","g","h"]):
                    print_nr(sprites.get_connector((ui_grid[y][x])[:1]+"v"))
                else: print_nr("═"*sprite_width)

                if x<10: print_nr("╬")
            print("╣")
        else:

            print_nr("   ╚")
            for i in range(rows-1):
                print_nr("═"*sprite_width+"╩")
            print("═"*sprite_width+"╝")


