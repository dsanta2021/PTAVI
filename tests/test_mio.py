from mysound import Sound
import unittest


class TestMio(unittest.TestCase):

    def test_sound(self):
        sound = Sound(1)
        sen = Sound(2)
        frec = 250
        maxAmplitud = sound.max_amplitude
        period1 = sound.samples_second / frec
        period2 = sen.samples_second / (frec*2)
        sound.sin(frec, maxAmplitud)
        sen.sin(frec*2, maxAmplitud/2)

        # Comprueba el número de muestras
        self.assertEqual(44100, len(sound.buffer))

        # Comprueba los valores de la onda senoidal 1 (amplitud)
        self.assertEqual(0, sound.buffer[0])
        self.assertNotEqual(maxAmplitud, sound.buffer[int(period1/2)])
        self.assertGreater(sound.buffer[int(period1 * 0.1)], sound.buffer[int(period1/2)])
        self.assertRegex('32766', str(sound.buffer[int(period1 * 0.25)]), msg='Error')

        # Comprueba los valores de la onda senoidal 2
        self.assertEqual(0, sen.buffer[int(period2 * 0)])
        self.assertEqual(sen.buffer[int(period2 * 0.25)], sen.buffer[int(period2/4)])
        self.assertAlmostEqual(16383, sen.buffer[int(period2 * 1.25)], delta=8)
        self.assertLess(0, sen.buffer[int(period2/4)])

        # Compara los valores de las dos ondas senoidales
        self.assertEqual(sound.buffer[int(period1/2)], -sen.buffer[int(period2)])
        self.assertNotEqual(sound.buffer[int(period1 * 0.25)], -sen.buffer[int(period2 * 0.25)])
        self.assertGreater(sound.buffer[2], -sen.buffer[2])
        self.assertLess(sound.buffer[466], sen.buffer[int(period2 * 2)])


if __name__ == '__main__':
    unittest.main()
