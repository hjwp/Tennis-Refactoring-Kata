import pytest

from tennis1 import TennisGame1
from tennis2 import TennisGame2
from tennis3 import TennisGame3
from tennis4 import TennisGame4
from tennis5 import TennisGame5
from tennis6 import TennisGame6
from tennis7 import TennisGame7
from tennis8 import TennisGame8
from tennis_unittest import play_game, test_cases


@pytest.mark.parametrize(
    "TennisGameClass",
    [
        TennisGame1,
        TennisGame2,
        TennisGame3,
        TennisGame4,
        TennisGame5,
        TennisGame6,
    ],
)
@pytest.mark.parametrize(
    "p1_points p2_points score p1_name p2_name".split(), test_cases
)
def test_get_score_most_games(
    TennisGameClass, p1_points, p2_points, score, p1_name, p2_name
):
    game = play_game(TennisGameClass, p1_points, p2_points, p1_name, p2_name)
    assert score == game.score()


@pytest.mark.parametrize(
    "p1_points p2_points score p1_name p2_name".split(), test_cases
)
def test_get_score_game7(p1_points, p2_points, score, p1_name, p2_name):
    game = play_game(TennisGame7, p1_points, p2_points, p1_name, p2_name)
    assert "Current score: " + score + ", enjoy your game!" == game.score()


def play_game8(TennisGame, p1_points, p2_points, p1_name, p2_name):
    game = TennisGame(p1_name, p2_name)
    for i in range(max(p1_points, p2_points)):
        if i < p1_points:
            game = game.won_point(p1_name)
        if i < p2_points:
            game = game.won_point(p2_name)
    return game


@pytest.mark.parametrize(
    "p1_points p2_points score p1_name p2_name".split(), test_cases
)
def test_get_score_game8(p1_points, p2_points, score, p1_name, p2_name):
    game = play_game8(TennisGame8, p1_points, p2_points, p1_name, p2_name)
    assert "Current score: " + score + ", enjoy your game!" == game.score()
