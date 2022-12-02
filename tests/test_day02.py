from day02 import *

guide = """A Y
B X
C Z"""


def test_shapes():
    assert get_shape("A") == HandShape.ROCK
    assert get_shape("A").value == 1
    assert get_shape("B") == HandShape.PAPER
    assert get_shape("B").value == 2
    assert get_shape("C") == HandShape.SCISSORS
    assert get_shape("C").value == 3
    assert get_shape("X") == HandShape.ROCK
    assert get_shape("X").value == 1
    assert get_shape("Y") == HandShape.PAPER
    assert get_shape("Y").value == 2
    assert get_shape("Z") == HandShape.SCISSORS
    assert get_shape("Z").value == 3


def test_game_scores():
    assert get_game_score(me=HandShape.ROCK, opponent=HandShape.ROCK) == 3
    assert get_game_score(me=HandShape.PAPER, opponent=HandShape.PAPER) == 3
    assert get_game_score(me=HandShape.SCISSORS, opponent=HandShape.SCISSORS) == 3
    assert get_game_score(me=HandShape.SCISSORS, opponent=HandShape.ROCK) == 0
    assert get_game_score(me=HandShape.PAPER, opponent=HandShape.ROCK) == 6


def test_scores():
    # score is actually based on shape value as well as game score.
    assert get_score(me=HandShape.ROCK, opponent=HandShape.ROCK) == 4
    assert get_score(me=HandShape.PAPER, opponent=HandShape.PAPER) == 5
    assert get_score(me=HandShape.SCISSORS, opponent=HandShape.SCISSORS) == 6


def test_sum_scores():
    rounds = guide.splitlines()
    assert get_scores(rounds) == 15


def test_targets():
    assert get_target("X") == Target.LOOSE
    assert get_target("Y") == Target.DRAW
    assert get_target("Z") == Target.WIN


def test_target_shape():
    assert get_target_shape(opponent=HandShape.ROCK, target=Target.DRAW) == HandShape.ROCK
    assert get_target_shape(opponent=HandShape.ROCK, target=Target.WIN) == HandShape.PAPER
    assert get_target_shape(opponent=HandShape.ROCK, target=Target.LOOSE) == HandShape.SCISSORS


def test_sum_scores_ultra():
    rounds = guide.splitlines()
    assert get_scores_part2(rounds) == 12
