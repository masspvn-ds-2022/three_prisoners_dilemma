import random
from typing import Tuple

C = 0
D = 1


class Player(object):
    def __init__(self):
        """
        called once at the start of the tournament
        """
        super().__init__()

    def new_match(self, opponent: Tuple[int, int]):
        """
        called at the start of every match
        :param opponent: id of the two opponents
        :return:
        """
        raise RuntimeError("implement me")

    def record_action(self, prev_action: Tuple[int, int]):
        """
        record action from opponent
        :param prev_action: previous action of opponent
        :return:
        """
        raise RuntimeError("implement me")

    def choose_action(self) -> int:
        """
        called to get action from agent
        :return:
        """
        raise RuntimeError("implement me")


class NicePlayer(Player):
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


class NastyPlayer(Player):
    def __init__(self):
        """
        the player who always plays nasty to others
        """
        super().__init__()

    def new_match(self, opponent: Tuple[int, int]):
        return

    def record_action(self, prev_action: Tuple[int, int]):
        return

    def choose_action(self) -> int:
        return D


class RandomPlayer(Player):
    def __init__(self):
        """
        the player who plays randomly at every round
        """
        super().__init__()

    def new_match(self, opponent: Tuple[int, int]):
        return

    def record_action(self, prev_action: Tuple[int, int]):
        return

    def choose_action(self) -> int:
        return D if random.random() > 0.5 else C


class FreakyPlayer(Player):
    def __init__(self):
        """
        the player who chooses a random action at the beginning of a match and commit to it
        """
        super().__init__()
        self.my_action = None

    def new_match(self, opponent: Tuple[int, int]):
        self.my_action = D if random.random() > 0.5 else C

    def record_action(self, prev_action: Tuple[int, int]):
        return

    def choose_action(self) -> int:
        return self.my_action


class Tit4TatPlayer(Player):
    def __init__(self):
        """
        the player who repeats the last action of either one of the opponent
        """
        super().__init__()
        self.next_action = None

    def new_match(self, opponent: Tuple[int, int]):
        self.next_action = C
        return

    def record_action(self, prev_action: Tuple[int, int]):
        player_to_tit4tat = 1 if random.random() > 0.5 else 0
        self.next_action = prev_action[player_to_tit4tat]

    def choose_action(self) -> int:
        return self.next_action
