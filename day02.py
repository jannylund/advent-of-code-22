from enum import Enum

from utils.timer import get_time, start_timer


class HandShape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Target(Enum):
    WIN = 6
    DRAW = 3
    LOOSE = 0


def get_shape(selection):
    if selection in ["A", "X"]:
        return HandShape.ROCK
    if selection in ["B", "Y"]:
        return HandShape.PAPER
    if selection in ["C", "Z"]:
        return HandShape.SCISSORS


def get_game_score(me, opponent):
    score = 0
    if me == opponent:
        score = Target.DRAW.value
    elif (
        (me == HandShape.ROCK and opponent == HandShape.SCISSORS)
        or (me == HandShape.SCISSORS and opponent == HandShape.PAPER)
        or (me == HandShape.PAPER and opponent == HandShape.ROCK)
    ):
        score = Target.WIN.value
    return score


def get_score(me, opponent):
    return me.value + get_game_score(me, opponent)


def get_scores(rounds):
    scores = []
    for round in rounds:
        o, m = round.split(" ")
        o = get_shape(o)
        m = get_shape(m)
        scores.append(get_score(m, o))
    return sum(scores)


def get_target(selection):
    if selection in ["X"]:
        return Target.LOOSE
    if selection in ["Y"]:
        return Target.DRAW
    if selection in ["Z"]:
        return Target.WIN


def get_target_shape(opponent, target):
    if target == Target.DRAW:
        return opponent

    if opponent == HandShape.ROCK:
        if target == Target.WIN:
            return HandShape.PAPER
        return HandShape.SCISSORS

    if opponent == HandShape.PAPER:
        if target == Target.WIN:
            return HandShape.SCISSORS
        return HandShape.ROCK

    if opponent == HandShape.SCISSORS:
        if target == Target.WIN:
            return HandShape.ROCK
        return HandShape.PAPER


def get_scores_part2(rounds):
    scores = []
    for round in rounds:
        o, m = round.split(" ")
        o = get_shape(o)
        m = get_target_shape(o, get_target(m))
        scores.append(get_score(m, o))
    return sum(scores)


if __name__ == "__main__":
    with open("input/day02.txt") as f:
        rounds = f.read().splitlines()

    start = start_timer()
    total_score = get_scores(rounds)
    print("day 02 part 1: total scores {} in {} ms".format(total_score, get_time(start)))
    assert total_score == 15632

    start = start_timer()
    total_score = get_scores_part2(rounds)
    print("day 02 part 2: total scores {} in {} ms".format(total_score, get_time(start)))
    assert total_score == 14416
