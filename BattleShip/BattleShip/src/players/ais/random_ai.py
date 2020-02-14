import random
from typing import List
from BattleShip.src import game_config, ship, orientation, move
from BattleShip.src.players.ais.ai_player import AIPlayer

class RandomAi(AIPlayer):

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)


    def init_name(self, player_num: int) -> None:
            self.name = f'Random AI {player_num}'


    def get_move(self) -> move.Move:
        firing_location = self.make_list()
        return random.choice(firing_location)

    def make_list(self, config: game_config.GameConfig):
        fire_location_possibilities = []
        for i in range(config._num_rows):
            for j in range(config._num_cols):
                fire_location_possibilities.append([i,j])
        return fire_location_possibilities


