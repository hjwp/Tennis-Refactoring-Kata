from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TennisGame8:
    player1_name: str
    player2_name: str
    player1_score: int = 0
    player2_score: int = 0

    def won_point(self, player_name) -> TennisGame8:
        if player_name == "player1":
            return TennisGame8(
                player1_name=self.player1_name,
                player2_name=self.player2_name,
                player1_score=self.player1_score + 1,
                player2_score=self.player2_score,
            )
        else:
            return TennisGame8(
                player1_name=self.player1_name,
                player2_name=self.player2_name,
                player1_score=self.player1_score,
                player2_score=self.player2_score + 1,
            )

    def _point_name(self, point: int) -> str:
        match point:
            case 0:
                return "Love"
            case 1:
                return "Fifteen"
            case 2:
                return "Thirty"
            case 3:
                return "Forty"
            case _:
                raise Exception("Invalid point value")

    def _score(self) -> str:
        if self.player1_score == self.player2_score:
            if self.player1_score > 2:
                return "Deuce"
            return f"{self._point_name(self.player1_score)}-All"

        if self.player1_score < 4 and self.player2_score < 4:
            return f"{self._point_name(self.player1_score)}-{self._point_name(self.player2_score)}"

        return self._end_game_score()

    def _end_game_score(self) -> str:
        if self.player1_score - self.player2_score == 1:
            return "Advantage " + self.player1_name
        elif self.player1_score - self.player2_score == -1:
            return "Advantage " + self.player2_name
        elif self.player1_score - self.player2_score >= 2:
            return "Win for " + self.player1_name
        else:
            return "Win for " + self.player2_name

    def score(self):
        return f"Current score: {self._score()}, enjoy your game!"
