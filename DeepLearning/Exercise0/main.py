import numpy as np
import matplotlib.pyplot as plt
import Exercise0.checkers as ch


def main():

    checkboard= ch(1,8)
    checkboard.draw()
    checkboard.show()



if __name__== "__main__":
    checkboard= ch.Checkers(1,8)
    checkboard.draw()
    checkboard.show()


