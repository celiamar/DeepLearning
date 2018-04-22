import numpy as np
import matplotlib.pyplot as plt

class Circle:


    def __init__(self, resolution, radius, position):
        self.resolution = resolution
        self.radius = radius
        self.position = position
        self.output = None


    def draw(self):
        x_indicies = np.arange(self.resolution)
        x_indicies = np.tile(x_indicies, (self.resolution, 1))

        y_indicies = x_indicies.T

        pos_y = (int) (self.position / self.resolution)
        pos_x = self.position - (pos_y * self.resolution)

        x_indicies = np.power((x_indicies - pos_x),2)
        y_indicies = np.power((y_indicies - pos_y),2)

        self.output = x_indicies + y_indicies
        self.output = self.output <= self.radius ** 2

    def show(self):
        plt.axis('off')
        plt.imshow(self.output, cmap='gray')
        plt.show()
