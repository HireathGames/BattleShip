player_grid = [
    [[2, 1], [2, 1], [2, 1], [2, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [5, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [5, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [5, 1], [0, 0], [0, 0], [6, 1], [6, 1], [6, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [5, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [5, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
]
#This is the code for checking the grid to find fully destroyed ships.
def destruction_check(grid):
    updated_grid = grid
    points = {}
    for rows in updated_grid:
        for pos in rows:
            if pos[0] in points.keys():
                points[pos[0]][0] += 1
                if (pos[1]>0):
                    points[pos[0]][1] += 1
            else:
                if (pos[1]>0):
                    points[pos[0]] = [1, 1]
                else:
                    points[pos[0]] = [1, 0]
    for key in points:
        if points[key][0] == points[key][1]:
            for row_ind in range(0, len(updated_grid)):
                for pos_ind in range(0, len(updated_grid[row_ind])):
                    if updated_grid[row_ind][pos_ind][0] == key:
                        updated_grid[row_ind][pos_ind][1] = -2
    return(updated_grid)
#This is the code for firing at a point.
def select_target(cord, grid):
    alphabet = "ABCDEFGHIJK"
    row = alphabet.index(cord[0 : 1])
    colum = int(cord[1 : len(cord)]) - 1
    updated_grid = grid
    if updated_grid[row][colum][0] != 0:
        if updated_grid[row][colum][1] == 0:
            updated_grid[row][colum][1] = 1
            return(updated_grid)
        else:
            return(updated_grid)
    else:
        return(updated_grid)
player_grid = select_target("H10", player_grid)
player_grid = destruction_check(player_grid)
for row in player_grid:
    print(row)

                