from mysound import Sound
import math


class SoundSin(Sound):
    def __init__(self, duration, frequency, amplitude):
        super().__init__(duration)          # Herencia de Sound
        self.frequency = frequency          # Inicialización de las variables
        self.amplitude = amplitude
        self.sin(frequency, amplitude)      # Creación de una onda senoidal
