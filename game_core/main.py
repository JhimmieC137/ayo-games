from utils.player_utils import *
from utils.board_utils import *


[player_one, player_two] = assign_players()     # Getting the two player objects
current_player = player_one    # Player to start game

while player_one.get_seeds() + player_two.get_seeds() > 3:  # Play game as long as 4 or more seeds in total are still in game
    player_one.board_holes, player_two.board_holes = play_board(player_one, player_two, current_player)

    current_player = player_one if player_two == current_player else player_two

    # Check possibility of end of game
    if (player_one.get_seeds() == 0 or player_two.get_seeds() == 0) and not validate_end_of_play([*player_one.board_holes, *player_two.board_holes], current_player.side):
        break


print(get_scores(player_one, player_two))    # Print scores and winner
