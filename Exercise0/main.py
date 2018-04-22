import numpy as np
import matplotlib.pyplot as plt
import Exercise0.checkers as ch
import Exercise0.spectrum as sp
import Exercise0.circle as cr

def main():
    # checkboard = ch.Checkers(2, 16)
    # checkboard.draw()
    # checkboard.show()

    # spectrum = sp.Spectrum(900)
    # spectrum.draw()
    # spectrum.show()

    circle = cr.Circle(1000,100,555500)
    circle.draw()
    circle.show()

if __name__== "__main__":
    main()


