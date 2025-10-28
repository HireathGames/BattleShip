import random
import copy


def count_values(matrix, vals):
    return [sum(row.count(val) for row in matrix) for val in vals]


def place_ship(board, ship_id, length):
    grid = copy.deepcopy(board)
    grid_size = len(grid)


    if random.randint(0,1)==0: #horizontal
        row = random.randint(0, grid_size-1) 
        start_col = random.randint(0, grid_size-length) 
            
        for i in range(length):
            grid[row][start_col+i] = ship_id
            
        return grid
    
    else: #vertical
        col = random.randint(0, grid_size-1)  
        start_row = random.randint(0, grid_size-length) 

        for i in range(length):
            grid[start_row+i][col] = ship_id

        return grid





def generate_board():
    board = [[0]*11 for _ in range(11)]


    ships = {5: 5, 6: 4, 7: 3, 8: 3, 9: 2}

    ship_items = list(ships.items())
    random.shuffle(ship_items)


    ships_placed_id = []
    ships_placed_len = []

    fails = 0


    for ship_id, length in ships.items():

        valid_placement = False

        ships_placed_id.append(ship_id)
        ships_placed_len.append(length)

        while not valid_placement:
            test_board = place_ship(board, ship_id, length)

            if count_values(test_board,ships_placed_id)==ships_placed_len:
                board = test_board
                valid_placement = True
    return board
