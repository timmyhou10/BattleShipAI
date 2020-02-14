import random
from typing import List
from BattleShip.BattleShip.src import game_config, ship, orientation, move
from BattleShip.BattleShip.src.players.player import Player

class AIPlayer(Player):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)


    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        ...

    def get_orientation(self, ship_: ship.Ship) -> orientation.Orientation:
        return random.choice([orientation.Orientation.HORIZONTAL, orientation.Orientation.VERTICAL])

    def get_start_coords(self, ship_: ship.Ship):
        if orientation == orientation.Orientation.HORIZONTAL:
            row = random.randint(0, self.board.num_rows - 1)
            col = random.randint(0, self.board.num_cols - ship_.length)

        else:
            row = random.randint(0, self.board.num_rows - ship_.length)
            col = random.randint(0, self.board.num_cols - 1)
        return row, col
    def get_move(self) -> move.Move:
        ...