import copy
from Classes import Point

def count_values(matrix, vals):
    return [sum(row.count(val) for row in matrix) for val in vals]


def translate_board(grid):
    #Trevor: I'll use this to translate the way y'all implement board into a more UI generation friendly method
    print("nah")    



def fetch_ship_id_list(points_grid):

    normal_grid = copy.deepcopy(points_grid)

    for y in range(len(points_grid)):
        for x in range(len(points_grid[0])):
            normal_grid[y][x]=Point.get_ID(points_grid[y][x])
    
    return normal_grid

       
