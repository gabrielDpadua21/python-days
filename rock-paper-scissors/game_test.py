import unittest
from rules import rock, paper, scissors


class MyTestCase(unittest.TestCase):
    def test_rock_win(self):
        self.assertEqual(rock("scissors"), "You Win")

    def test_rock_lose(self):
        self.assertEqual(rock("paper"), "You Lose")

    def test_rock_tie(self):
        self.assertEqual(rock("rock"), "a tie")

    def test_paper_lose(self):
        self.assertEqual(paper("scissors"), "You Lose")

    def test_paper_tie(self):
        self.assertEqual(paper("paper"), "a tie")

    def test_paper_win(self):
        self.assertEqual(paper("rock"), "You Win")

    def test_scissors_lose(self):
        self.assertEqual(scissors("rock"), "You Lose")

    def test_scissors_tie(self):
        self.assertEqual(scissors("scissors"), "a tie")

    def test_scissors_win(self):
        self.assertEqual(scissors("paper"), "You Win")


if __name__ == '__main__':
    unittest.main()
