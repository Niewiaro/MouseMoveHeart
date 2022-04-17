import math as m
import numpy as np

outputRound = 2 # how many digits after dot
step = 0.1 # step in for loop and "x" step 

# this loop creates points that are used to check the accuracy of the compaction (ex. in Geogebra)
# https://www.geogebra.org/calculator/evakcq4n

for x in np.arange(-2, 2 + step, step):
    x = round(x, outputRound)
    y = round(m.sqrt(1 - (abs(x) - 1) ** 2), outputRound) # function whose points are searched for
  
    print('({},{}),'.format(x, y), end = "")