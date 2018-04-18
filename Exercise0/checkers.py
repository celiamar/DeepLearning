import numpy as np
import matplotlib.pyplot as plt



class Checkers:


    def __init__(self, tilesize, resolution):

        self.tilesize= tilesize
        self.resolution=resolution
        self.output = None

    def draw(self):

        steps= (int)((self.resolution/self.tilesize)/2)

        oddrow= np.concatenate( (np.zeros(self.tilesize),np.ones(self.tilesize)), axis = 0)
        oddrow= np.tile(oddrow, (steps))
        oddrow= np.tile(oddrow, (self.tilesize,1))
        evenrow= np.concatenate( (np.ones(self.tilesize),np.zeros(self.tilesize)), axis = 0)
        evenrow = np.tile(evenrow, (steps))
        evenrow = np.tile(evenrow, (self.tilesize,1))

        tworows = np.vstack((oddrow, evenrow))

        self.output = np.tile(tworows, (steps,1))

    def show(self):
        print(self.output)
        plt.imshow(self.output)
        plt.gray()
        plt.show()