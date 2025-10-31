def count_values(matrix, vals):
    return [sum(row.count(val) for row in matrix) for val in vals]


def translate_board(grid):
    #Trevor: I'll use this to translate the way y'all implement board into a more UI generation friendly method
    print("nah")  