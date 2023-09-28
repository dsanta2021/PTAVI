#! /usr/bin/env python3

import math


class Sound:
    samples_second = 44100
    max_amplitude = 2 ** 15 - 1

    def __init__(self, duration):
        """
        Initializes a new instance of the class with the specified duration.

        @param duration: The duration of the sound in seconds
        @returns: None
        """
        self.duration = duration
        self.nsamples = int(self.samples_second * self.duration)
        self.buffer = [0] * self.nsamples

    def sin(self, frequency, amplitude):
        """
        Creates a sine wave with the specified frequency and amplitude.

        :param frequency: The frequency of the sine wave in Hz
        :param amplitude: The amplitude of the sine wave
        :return: None
        """

        for nsample in range(self.nsamples):
            t = nsample / self.samples_second
            self.buffer[nsample] = int(amplitude *
                                       math.sin(2 * math.pi * frequency * t))

    @staticmethod
    def _bar(value):
        """
        Return string of stars corresponding to a horizontal bar

        :param value: value of the mean sound for that bar
        :return: string with chars for the bar
        """
        stars = int(abs(value) // 1000 * 4)
        if value > 0:
            chars = (' ' * 40) + ':' + ('*' * stars)
        else:
            chars = (' ' * (40 - stars)) + ('*' * stars) + ':'
        return chars

    def bars(self, bar_period=0.01):
        """
        Generates a bar visualization of the sound, as a string

        :param bar_period: period (in seconds) of each bar
        :return: string with bar visualization
        """

        samples_period = int(bar_period * self.samples_second)
        chars = ""
        for nsample in range(0, len(self.buffer), samples_period):
            fraction = self.buffer[nsample: nsample + samples_period]
            mean = sum(fraction) / len(fraction)
            chars = chars + self._bar(mean) + '\n'
        return chars
