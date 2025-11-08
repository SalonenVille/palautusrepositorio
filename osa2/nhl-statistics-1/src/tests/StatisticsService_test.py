import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Kurri")
        self.assertAlmostEqual(player.name, "Kurri")
    
    def test_search_pelaajaa_ei_loydy(self):
        player = self.stats.search("Jake")
        self.assertIsNone(player)

    def test_team(self):
        team = self.stats.team("EDM")
        for player in team:
            self.assertEqual(player.team, "EDM")

    def test_top(self):
        top_players = self.stats.top(3)
        expected_names = ["Gretzky", "Lemieux", "Yzerman"]
        correct_names = [player.name for player in top_players]
        self.assertEqual(correct_names, expected_names)
