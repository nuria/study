#!/usr/local/bin/python
import matplotlib.pyplot as pl

# avg 51
x = [10,10,20,20,20,20,20, 30,30, 30, 30, 40, 40, 60,70, 70, 70, 70, 80, 80, 80, 80, 80, 90, 90, 100]

bins = [10,20,30,40,50,60,70,80,90,100]
pl.subplot(2, 1, 1)
pl.title("Test Scores")
pl.hist(x, bins,  color=('pink'))
pl.ylim(ymax=6)

pl.subplot(2, 1, 2)

#avg 52
x2 = [45,45,46,46,47,47,48,48,49,49,50,50,51, 51,51,51, 52,52,53, 53, 54,54, 55,55,56,56,57,57]
pl.hist(x2, bins,  color=('pink'))
pl.title("Test Scores")
pl.ylim(ymax=20)
pl.show()

