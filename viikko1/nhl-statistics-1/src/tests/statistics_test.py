import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12), #16
            Player("Lemieux", "PIT", 45, 54), #99
            Player("Kurri",   "EDM", 37, 53), #90
            Player("Yzerman", "DET", 42, 56), #98
            Player("Gretzky", "EDM", 35, 89) #124
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_find_player(self):
        name = self.statistics.search("Semenko")
        self.assertAlmostEqual(str(name), "Semenko EDM 4 + 12 = 16")

    def test_player_not_found(self):
        name = self.statistics.search("not_found")
        self.assertAlmostEqual(name, None)

    def test_number_of_players_in_team(self):
        player_list = self.statistics.team("EDM")
        self.assertAlmostEqual(len(player_list), 3)

    def test_no_players_in_team(self):
        player_list = self.statistics.team("NHL")
        self.assertAlmostEqual(len(player_list), 0)

    def test_find_top_scorer(self):
        top_scorer = self.statistics.top(1,1)
        self.assertAlmostEqual(str(top_scorer[0]), "Gretzky EDM 35 + 89 = 124")

    def test_find_top_goalers(self):
        top_goaler = self.statistics.top(1,2)
        self.assertAlmostEqual(str(top_goaler[0]), "Lemieux PIT 45 + 54 = 99")

    def test_find_top_assist(self):
        top_assist = self.statistics.top(1,3)
        self.assertAlmostEqual(str(top_assist[0]), "Gretzky EDM 35 + 89 = 124")

