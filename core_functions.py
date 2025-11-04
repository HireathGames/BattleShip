from Classes import Point

def intialize_grid(Height = 11, Width = 11):
    out_grid = []
    for row_ind in range(Height):
        row = []
        for ind in range(Width):
            row.append(Point())
        out_grid.append(row)
    return(out_grid)


#This is the code for checking the grid to find fully destroyed ships.
def destruction_check(grid):
    updated_grid = grid 
    points = {}
    for rows in updated_grid:
        for pos in rows:
            if pos.get_ID() in points.keys():
                points[pos.get_ID()][0] += 1
                if (pos.get_State() > 0):
                    points[pos.get_ID()][1] += 1
            else:
                if (pos.get_State() > 0):
                    points[pos.get_ID()] = [1, 1]
                else:
                    points[pos.get_ID()] = [1, 0]
    for key in points:
        if points[key][0] == points[key][1]:
            for row_ind in range(0, len(updated_grid)):
                for pos_ind in range(0, len(updated_grid[row_ind])):
                    if updated_grid[row_ind][pos_ind].get_ID() == key:
                        updated_grid[row_ind][pos_ind].set_State(-2)
    return(updated_grid)

#This is the code for firing at a point.
def select_target(cord, grid):
    alphabet = "ABCDEFGHIJK"
    row = alphabet.index(cord[0 : 1])
    colum = int(cord[1 : len(cord)]) - 1
    updated_grid = grid
    return_message = updated_grid[row][colum].chosen_target()
    return (updated_grid, return_message)


def check_coordinate(grid,coord): #idk how your thinks worked so i made a more dynamic one
    alphabet = "ABCDEFGHIJK"
    row = alphabet.index(coord[0])
    column = int(coord[1 : len(coord)]) - 1
    status = 0
    if grid[row][column].get_ID() != 0:
        status = 1

    else:
        status = -1

    grid[row][column] = Point(grid[row][column].get_ID(),status)

    return status,grid