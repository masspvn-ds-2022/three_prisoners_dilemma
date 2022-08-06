from typing import Tuple, Optional, Dict, Any

from khanh_nguyen_code.player import KhanhPlayer
from package.player import NicePlayer, RandomPlayer, FreakyPlayer, NastyPlayer, Tit4TatPlayer, Player

C = 0
D = 1

NUM_ROUNDS = 100

PAYOFF = {
    (C, C): {C: 6, D: 8},
    (C, D): {C: 3, D: 5},
    (D, C): {C: 3, D: 5},
    (D, D): {C: 0, D: 2},
}


def _other_t(i: int, t: Optional[Tuple[Any, Any, Any]]) -> Optional[Tuple[Any, Any]]:
    if t is None:
        return None
    return t[(i + 1) % 3], t[(i + 2) % 3]


def _add_score(canvas: Tuple[int, int, int], addon: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return canvas[0] + addon[0], canvas[1] + addon[1], canvas[2] + addon[2]


def run_match(player_pool: Dict[int, Player], player_id: Tuple[int, int, int]) -> Tuple[int, int, int]:
    player = [player_pool[name] for name in player_id]
    for i in range(3):
        player[i].new_match(opponent=_other_t(i, player_id))

    total_score = (0, 0, 0)
    for _ in range(NUM_ROUNDS):
        action = tuple(
            player[i].choose_action() for i in range(3)
        )

        for i in range(3):
            player[i].record_action(_other_t(i, action))

        score = tuple(
            PAYOFF[_other_t(i, action)][action[i]] for i in range(3)
        )
        total_score = _add_score(total_score, score)
    return total_score


if __name__ == "__main__":
    pool = {
        0: NicePlayer(),
        1: NastyPlayer(),
        2: RandomPlayer(),
        3: FreakyPlayer(),
        4: Tit4TatPlayer(),
        5: KhanhPlayer(),
    }
    score = run_match(player_pool=pool, player_id=(3, 4, 5))
    print(score)
