import unittest
from mysoundsin import SoundSin
import math


class TestSoundSin(unittest.TestCase):
    def test_init(self):
        duration = 10
        frequency = 1000
        amplitude = 0.02
        sen = SoundSin(duration, frequency, amplitude)

        self.assertEqual(sen.duration, duration)
        self.assertEqual(sen.frequency, frequency)
        self.assertEqual(sen.amplitude, amplitude)

    def test_sin(self):
        duration = 6
        frequency = 225
        amplitude = 0.5
        sen = SoundSin(duration, frequency, amplitude)

        period = SoundSin.samples_second / frequency
        expected_value = amplitude * math.sin(2 * math.pi * frequency * 0 / sen.samples_second)

        # Compruba si la amplitud con lo esperado
        self.assertEqual(0, sen.buffer[int(period)])

        # Verifica si el valor del primer elemento del sonido senoidal es correcto
        self.assertEqual(sen.buffer[0], expected_value)

    def test_bars(self):
        duration = 2
        frequency = 440
        amplitude = 0.001
        sen = SoundSin(duration, frequency, amplitude)

        bars = sen.bars(bar_period=0.0001)

        self.assertAlmostEqual(22060, len(bars.split('\n')), delta=10)      # Comprueba el número de lineas
        self.assertAlmostEqual(41, len(bars.split('\n')[0]), delta=1)       # Verifica la longitud de bar


if __name__ == '__main__':
    unittest.main()
