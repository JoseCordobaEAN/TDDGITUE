from unittest import TestCase
from funciones import *

class TestContar_vocales(TestCase):

    def test_contar_vocales(self):

        dado = 'hola mundo'
        espero = 4
        real = contar_vocales(dado)
        self.assertEquals(espero, real)


        dado = 'UniEMPREsaRIAL'
        espero = 7
        real = contar_vocales(dado)
        self.assertEquals(espero, real)

        # Casos Extremos

        # Casos Excepcionales