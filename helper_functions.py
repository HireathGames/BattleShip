import copy
from Classes import Point

def count_values(matrix, vals):
    return [sum(row.count(val) for row in matrix) for val in vals]


def translate_board(grid):
    #Trevor: I'll use this to translate the way y'all implement board into a more UI generation friendly method
    print("nah")    



def translate_point_to_grid(points_grid):

    # states:
    # 0 baseline
    # 1 hit
    # -1 miss

    normal_grid = copy.deepcopy(points_grid)

    for y in range(len(points_grid)):
        for x in range(len(points_grid[0])):

            if Point.get_State(points_grid[y][x]) == 0: # no modification
                normal_grid[y][x]=Point.get_ID(points_grid[y][x])

            if Point.get_State(points_grid[y][x]) in [1,-2]: # hit/sunk
                normal_grid[y][x] = 0 - Point.get_ID(points_grid[y][x])

            if Point.get_State(points_grid[y][x]) < -1: # miss
                normal_grid[y][x] = 1

    
    return normal_grid

       
