import unittest
from atividade01.classes.q1 import Bola


class TestQuestion1(unittest.TestCase):

    def test_ball_get_method(self):
        ball = Bola('red')

        expected = 'red'

        self.assertEqual(ball.get(), expected)

    def test_ball_set_method(self):
        ball = Bola('blue')

        ball.set('red')

        self.assertEqual(ball.get(), 'red')


if __name__ == '__main__':
    unittest.main()
