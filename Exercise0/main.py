import numpy as np
import matplotlib.pyplot as plt
import Exercise0.checkers as ch


def main():
    checkboard = ch.Checkers(2, 16)
    checkboard.draw()
    checkboard.show()


if __name__== "__main__":
    main()


