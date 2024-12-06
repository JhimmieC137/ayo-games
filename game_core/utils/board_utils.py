from random import choice

from .player_utils import Player, validate_input
from .text_colors import *


def display_board(current_player: Player, other_player: Player) -> None:    # Prints the state of the board
    print(f"\n\n    {'Player 1' if other_player.side == 0 else 'Player 2'}:  { YELLOW + other_player.name + ENDC } ({GREEN + str(other_player.captured) + ENDC if other_player.captured > current_player.captured else FAIL + str(other_player.captured) + ENDC})")

    print('  -----------------------------------------------------')

    # for number in range(6, 0, -1):
    #     if number == 1:
    #         print(f"{number}\t|")
    #     elif number == 6 :
    #         print(f" |\t{number}", end='\t')
    #     else:
    #         print(f"{number}", end='\t')

    for hole in range((len(other_player.board_holes) - 1), -1, -1):
        if hole == 0:
            print(f"{other_player.board_holes[hole]}{ENDC}\t|")
        elif hole == 5:
            print(f" |\t{BOLD}{BLUE}{other_player.board_holes[hole]}", end='\t')
        else:
            print(f"{BOLD}{BLUE}{other_player.board_holes[hole]}", end='\t')

    print('  |----------------------------------------------------| ')

    for hole in range(len(current_player.board_holes)):
        if hole == len(current_player.board_holes) - 1:
            print(f"{current_player.board_holes[hole]}{ENDC}\t|")
        elif hole == 0:
            print(f" |\t{BOLD}{BLUE}{current_player.board_holes[hole]}", end='\t')
        else:
            print(f"{BOLD}{BLUE}{current_player.board_holes[hole]}", end='\t')

    # for number in range(1, 7):
    #     if number == 6:
    #         print(f"{number}\t|")
    #     elif number == 1 :
    #         print(f" |\t{number}", end='\t')
    #     else:
    #         print(f"{number}", end='\t')

    print('  ----------------------------------------------------- ')
    print(f"    {'Player 1' if current_player.side == 0 else 'Player 2'}: {YELLOW + current_player.name + ENDC} ({GREEN + str(current_player.captured) + ENDC if current_player.captured > other_player.captured else FAIL + str(current_player.captured) + ENDC})\n\n")

    # print([*board_one, *board_two], "\n")


def get_boards(board: list = None) -> tuple[list[int], list[int]]:   # Split the board into two sides for each player
    board_one = [seed for seed in board[0:6]]
    board_two = [seed for seed in board[6:12]]

    return board_one, board_two


def get_playable_holes(holes: list) -> list[int]:     # Retrieve holes with seeds
    holes = [hole+1 for hole in range(6) if holes[hole] != 0]

    return holes


def validate_end_of_play(board_state: list[int], next_side: int) -> bool|int:    # Check for chance no further play
    side_board_state = board_state[(next_side * 6): 6 + (next_side * 6)]   # Calculate the side of the current player on the board
    holes = get_playable_holes(side_board_state)
    compulsory_hole = None
    for hole in holes:
        if side_board_state[(hole - 1)] > (6 - hole):    # Check for the hole at the extreme  has enough seeds to reach the other side
            compulsory_hole = hole

    if compulsory_hole:
        return compulsory_hole
    else:
        return False



def validate_selection(current_side: Player, other_side: Player) -> tuple[list[int], int, int]:   # Aid selection of board holes
    current_board = [*current_side.board_holes, *other_side.board_holes] if current_side.side == 0 else [*other_side.board_holes, *current_side.board_holes]
    seed_count = 0

    while seed_count == 0:
        if current_side.is_comp:
            if sum(current_board[other_side.side * 6: 6 + (other_side.side * 6)]) == 0:
                selected_hole = validate_end_of_play(current_board, next_side=1 if other_side.side == 0 else 0)
            else:
                selected_hole = choice(get_playable_holes(current_side.board_holes))
        else:
            display_board(current_side, other_side)
            selected_hole = validate_input(1, f"{current_side.name}, Select a hole from 1 to 6: ")

            if (sum(current_board[other_side.side * 6: 6 + (other_side.side * 6)]) == 0) and (selected_hole != validate_end_of_play(current_board, next_side=1 if other_side.side == 0 else 0)):
                while selected_hole != validate_end_of_play(current_board, next_side=1 if other_side.side == 0 else 0):
                    selected_hole = validate_input(1, f"{current_side.name}, Please select hole {validate_end_of_play(current_board, next_side=1 if other_side.side == 0 else 0)} to continue the game: ")

        print(f"{current_side.name} picked hole {selected_hole}")

        if 0 < selected_hole < 7:
            board_index = (selected_hole - 1) + (current_side.side * 6)
            seed_count = current_board[board_index]

            if seed_count == 0:
                print("Hole has no seeds. Choose another!")

            else:
                current_board[board_index] = 0
                return current_board, board_index, seed_count

        else:
            print("Invalid hole!")



def move_and_capture(current_board: list[int], board_index: int, seed_count: int, current_side: Player) -> tuple[list[int], list[int]]:   # To move from hole to hole and capture
    while seed_count > 0:
        board_index += 1
        if board_index > 11:
            board_index = 0
        current_board[board_index] += 1
        seed_count -= 1


    if current_board[board_index] == 4:
        current_side.captured += current_board[board_index]
        print(f"{current_side.name} captured seeds in hole {board_index + 1}. {current_side.name} now has {current_side.captured} captured seeds\n")

        current_board[board_index] = 0


    return get_boards(current_board)



def play_board(player_one: Player, player_two: Player, current_side: Player) -> tuple[list[int], list[int]]:    # Comprises each iteration of a players move
    updated_board, board_index, seed_count = validate_selection(current_side, other_side=player_two if current_side == player_one else player_one)

    return move_and_capture(updated_board, board_index, seed_count, current_side)



