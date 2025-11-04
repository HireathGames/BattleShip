#Imports the Point class from Classes
from Classes import Point
import ship_placement
import board_generator
import core_functions
# moved the functions to core functions (because you can't import a file that imports your file, so main wouldn't be able to access any files that import main) -Trevor





player_grid = ship_placement.run_ship_placement()
ai_grid = board_generator.generate_board_point()


print(ai_grid)
print(player_grid)

