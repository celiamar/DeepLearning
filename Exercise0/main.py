import numpy as np
import matplotlib.pyplot as plt
import Exercise0.checkers as ch
import Exercise0.spectrum as sp


def main():
    # checkboard = ch.Checkers(2, 16)
    # checkboard.draw()
    # checkboard.show()

    spectrum = sp.Spectrum(900)
    spectrum.draw()
    spectrum.show()
if __name__== "__main__":
    main()


