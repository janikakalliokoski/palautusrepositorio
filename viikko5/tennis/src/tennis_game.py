class TennisGame:
    def __init__(self, player1: str, player2: str):
        self.player1 = player1
        self.player2 = player2
        self._score1 = 0
        self._score2 = 0

    def won_point(self, player: str):
        if player == self.player1:
            self._score1 += 1
        else:
            self._score2 += 1

    def get_score(self):
        scores = ["Love", "Fifteen", "Thirty", "Forty"]
        best_score = max(self._score1, self._score2)

        if self._score1 == self._score2:
            if best_score < 4:
                return f"{scores[self._score1]}-All"
            else:
                return "Deuce"
        else:
            if best_score < 4:
                return f"{scores[self._score1]}-{scores[self._score2]}"
            else:
                score_difference = self._score1 - self._score2

                if score_difference == 1:
                    return f"Advantage {self.player1}"
                if score_difference == -1:
                    return f"Advantage {self.player2}"
                if score_difference >= 2:
                    return f"Win for {self.player1}"
                else:
                    return f"Win for {self.player2}"
