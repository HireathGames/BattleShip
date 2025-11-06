# python libraries
import time
import copy

# our functions
import ship_placement
import draw_boards

import core_functions
import gameloop_input


short_break = 0
long_break = 0



keep_playing = (input("Would you like to play battleship? (y/n)").lower().startswith("y"))

while keep_playing:

    ship_dictionary = ship_placement.get_available_ships()


    player_grid = ship_placement.generate_random_board() # ship_placement.run_ship_placement()
    original_player_grid = copy.deepcopy(player_grid) 


    ai_grid = ship_placement.generate_random_board()
    original_ai_grid = copy.deepcopy(ai_grid)



    winner = 0 # 1 for player, 2 for ai, 0 for in-progress

    while winner == 0:

        # player turn
        draw_boards.print_ai_board(original_ai_grid,ai_grid)


        ai_grid,status = gameloop_input.get_ai_shot(ai_grid)
        
        draw_boards.print_ai_board(original_ai_grid,ai_grid)


        if status == -1:
            print("\nYou missed...")
        elif status == 1: 
            print("\nYou hit a ship!")
            if core_functions.check_for_win(ai_grid,ship_dictionary):
                winner = 1
                break


        draw_boards.print_player_board(original_player_grid,player_grid)

            

        # ai turn
        print("Ai is making its shot",end="",flush=True)

        for i in range(4):
            time.sleep(long_break/4)
            print(".",end="",flush=True)
        print()


        player_grid, ai_status = gameloop_input.get_ai_shot(player_grid)
        draw_boards.print_player_board(original_player_grid,player_grid)


        if ai_status == -1:
            print("\nThe AI missed!")
        elif ai_status == 1: 
            print("\nThe AI hit a ship...")
            if core_functions.check_for_win(player_grid,ship_dictionary):
                winner = 2
                break


        time.sleep(long_break)



    time.sleep(short_break/2)

    if winner == 1: #player win
        print("\n\nYou won!")
    elif winner == 2:
        print("\n\nThe AI won...")

    time.sleep(short_break)

    keep_playing = (input("Would you like to play again? (y/n)").lower().startswith("y"))

    

