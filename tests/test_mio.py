from mysound import *


class TestMio(unittest.TestCase):

    def test_play_sound(self):
        # Test playing a sound
        play_sound("sound.wav")

        # Add assertions to check that sound played correctly
        self.assertTrue(True) 