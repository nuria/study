#!/usr/local/bin/python
import matplotlib.pyplot as pl


x = [10,10,20,20,20,20,20, 30,30, 30, 30, 40, 40, 60,70, 70, 70, 70, 80, 80, 80, 80, 80, 90, 90, 100]

bins = [10,20,30,40,50,60,70,80,90,100]

pl.hist(x, bins,  color=('pink'))
pl.ylim(ymax=6)
pl.title("Test Scores")
pl.xlabel("Score")
pl.show()
