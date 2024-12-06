from .text_colors import *

class Player:
    def __init__(self) -> None:
        self.board_holes = None
        self.captured = None
        self.name = None
        self.side = None
        self.is_comp = None


    def create_player(self, name: str, side: int, is_comp: bool = False):
        self.name = name
        self.board_holes = [4, 4, 4, 4, 4, 4]
        self.captured = 0
        self.side = side
        self.is_comp = is_comp

        return self

    def get_seeds(self) -> int:
        seed_number = 0
        for seed in self.board_holes:
            seed_number += seed

        return seed_number

def validate_input(sample_type, prompt: str, nullable: bool = False):
    while True:
        try:
            value = type(sample_type)(input(prompt))
            return value
        except:
            if nullable and prompt is None:
                pass

            print("Invalid input!\n")

        # finally:



def assign_players() -> list[Player]:
    player_one_obj = Player()
    player_one_name = validate_input("string", "Input a name for Player_1\nPress <Enter> to select computer as player: ", True)
    if player_one_name is None or player_one_name == '':
        print("Computer_1 selected as player 1\n")
        player_one_obj.create_player(name="Comp_1", side=0, is_comp=True)
    else:
        player_one_obj.create_player(name=player_one_name, side=0)

    player_two_obj = Player()
    player_two_name = validate_input("string", "Input a name for Player_2\nPress <Enter> to select computer as player: ", True)
    if player_two_name is None or player_two_name == '':
        print("Computer_2 selected as player 2\n")
        player_two_obj.create_player(name="Comp_2", side=1, is_comp=True)
    else:
        player_two_obj.create_player(name=player_two_name, side=1)



    return [player_one_obj, player_two_obj]



def get_scores(player_one: Player, player_two: Player) -> str:
    print(f"\n\n{YELLOW} {player_one.name} {ENDC} total score:")
    print("   ---------------------------------")
    print(f"     {player_one.name} captured seeds: {player_one.captured}")
    print(f"     {player_one.name} remaining seeds: {player_one.get_seeds()}")
    print(f"     {player_one.name} total seeds: {player_one.get_seeds() + player_one.captured}")
    print("   ---------------------------------\n\n")

    print(f"\n\n{YELLOW} {player_two.name} {ENDC} total score:")
    print("   ---------------------------------")
    print(f"     {player_two.name} captured seeds: {player_two.captured}")
    print(f"     {player_two.name} remaining seeds: {player_two.get_seeds()}")
    print(f"     {player_two.name} total seeds: {player_two.get_seeds() + player_two.captured}")
    print("   ---------------------------------\n\n")

    if (player_two.get_seeds() + player_two.captured) == player_one.get_seeds() + player_one.captured:
        return  f" ***** {YELLOW} It's a draw! {ENDC}  *****\n\n"

    return  f" {GREEN}***** $$ {player_one.name if (player_one.get_seeds() + player_one.captured) > (player_two.get_seeds() + player_two.captured) else player_two.name} wins $$  *****{ENDC}\n\n"
