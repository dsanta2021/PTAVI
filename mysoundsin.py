from mysound import Sound
import math

class SoundSin(Sound):
    def __init__(self, duration, frequency, amplitude):
        super().__init__(duration)          # herencia de Sound
        self.frequency = frequency          # inicialización de las variables
        self.amplitude = amplitude

        self.sin(frequency, amplitude)      # creación de la onda senoidal
        # for nsample in range(self.nsamples):
        #     t = nsample / self.samples_second
        #     self.buffer[nsample] = int(amplitude *
        #                                math.sin(2 * math.pi * frequency * t))