import random
from typing import List
from BattleShip.src import game_config, ship, orientation, move
from BattleShip.src.players.ais.ai_player import AIPlayer

class RandomAi(AIPlayer):

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)


    def init_name(self, player_num: int) -> None:
            self.name = f'Random AI {player_num}'