import unittest
from main import avaliar_humor


class TestAvaliarHumor(unittest.TestCase):
    def test_humor_agressivo(self):
        humor = avaliar_humor("Estou muito irritado com isso!")
        self.assertEqual(humor, 3)

    def test_humor_neutro(self):
        humor = avaliar_humor("A temperatura está amena hoje.")
        self.assertEqual(humor, 5)

    def test_humor_reconfortante(self):
        humor = avaliar_humor("Adoro passar tempo com minha família.")
        self.assertEqual(humor, 7)

    def test_humor_misto(self):
        humor = avaliar_humor("Estou um pouco triste, mas ainda esperançoso.")
        self.assertEqual(humor, 3)


if __name__ == '__main__':
    unittest.main()
