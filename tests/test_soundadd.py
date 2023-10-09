import unittest
from mysound import Sound
import soundops


class TestSoundAdd(unittest.TestCase):
    def test_different_lenght(self):
        s1 = Sound(5)
        s2 = Sound(10)
        s3 = soundops.soundadd(s1, s2)
        durationMax = max(s1.duration, s2.duration)
        durationMin = min(s1.duration, s2.duration)

        self.assertEqual(durationMax, s3.duration)
        self.assertGreater(s3.duration, durationMin)

    def test_equal_lenght(self):
        sameDuration = 8
        s1 = Sound(sameDuration)
        s2 = Sound(sameDuration)
        s3 = soundops.soundadd(s1, s2)

        self.assertEqual(sameDuration, s3.duration)
        self.assertListEqual(s1.buffer, s2.buffer)

    def test_s1_longer(self):
        s1 = Sound(1)
        s2 = Sound(0.5)
        s3 = soundops.soundadd(s1, s2)

        self.assertEqual(len(s3.buffer), max(len(s1.buffer), len(s2.buffer)))
        self.assertEqual(s3.duration, max(s1.duration, s2.duration))

    def test_s2_longer(self):
        s1 = Sound(1.6)
        s2 = Sound(4.4)
        s3 = soundops.soundadd(s1, s2)

        self.assertEqual(s3.buffer, s2.buffer)
        self.assertLess(s1.duration, s2.duration)
        self.assertGreater(s2.buffer, s1.buffer)
        self.assertEqual(s3.duration, max(s1.duration, s2.duration))

    def test_non_lenght(self):
        duration = 0
        s1 = Sound(duration)
        s2 = Sound(duration)
        s3 = soundops.soundadd(s1, s2)

        self.assertEqual(len(s1.buffer), s1.duration)
        self.assertEqual(s1.duration, s2.duration)
        self.assertEqual(s3.duration, s1.duration + s2.duration)


if __name__ == '__main__':
    unittest.main()
