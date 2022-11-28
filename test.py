import unittest
import gato


class Test(unittest.TestCase):

    # def test_CPU_dificil (self):
    #  self.assertTrue(gato.Gato().jugador_vs_cpu(gato.Gato().nivel) )

    def test_jugador_jugador(self):
        self.assertTrue(gato.Gato().jugador_vs_jugador())

    '''def test_movim_restantes(self):
       self.assertTrue(gato.Gato().movimientos_restantes(gato.Gato().tablero))
'''


if __name__ == "_main_":
    unittest.main()
