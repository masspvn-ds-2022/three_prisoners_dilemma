from typing import Tuple

from package.player import Player, C


class KhanhPlayer(Player):
    def __init__(self):
        """
        the player who always plays nice to others
        """
        super().__init__()

    def new_match(self, opponent: Tuple[int, int]):
        return

    def record_action(self, prev_action: Tuple[int, int]):
        return

    def choose_action(self) -> int:
        return C
