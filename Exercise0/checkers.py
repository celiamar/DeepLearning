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
        evenrow= np.concatenate( (np.ones(self.tilesize),np.zeros(self.tilesize)), axis = 0)
        oddtemp= np.tile(oddrow, steps)
        eventemp= np.tile(evenrow, steps)

        tworows= np.concatenate((oddtemp, eventemp),axis = 0)
        temp2=np.tile(tworows, steps)
        self.output= np.reshape(temp2,[self.resolution,self.resolution])


    def show(self):
        print(self.output)
        plt.imshow(self.output)
        plt.show()