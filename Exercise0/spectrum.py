import numpy as np
import matplotlib.pyplot as plt

class Spectrum:

    def __init__(self, resolution):
        self.resolution  = resolution
        self.output = None

    def draw(self):


        range = np.linspace(0,self.resolution,self.resolution)/self.resolution
        range = np.tile(range, (self.resolution,1))

        r = range
        g = range.T
        b = np.flip(range, axis = 1)

        r = np.expand_dims(r, axis=2)
        g = np.expand_dims(g, axis=2)
        b = np.expand_dims(b, axis=2)

        self.output = np.concatenate([r, g, b], axis=2)

    def show(self):
        print(self.output)
        img = self.output
        plt.imshow(img)
        plt.show()