import math as m
import numpy as np

outputRound = 2 # how many digits after dot
step = 0.1 # step in for loop and "x" step 

# articule about heart function
# https://towardsdatascience.com/plot-the-shape-of-my-heart-698d4776c51a

# function which return value of upper part of heart
def upperHeartFunction(num):
    return m.sqrt(1 - (abs(num) - 1) ** 2)

# return value of bottom part of heart
def bottomHeartFunction(num):
    return np.arccos(1 - abs(num)) - m.pi

def pointCounter(function):
    # this loop creates points that are used to check the accuracy of the compaction (ex. in Geogebra)
    # https://www.geogebra.org/calculator/evakcq4n

    points = ""
    map = []
    tmp = 0
    for x in np.arange(-2, 2 + step, step):
        x = round(x, outputRound)
        y = round(function(x), outputRound) # function whose points are searched for
    
        points = points + ('({},{}),'.format(x, y))
        # due to fact that "x" step is constant, only difference between consecutive y is needed
        map.append(round(y-tmp, outputRound))
        tmp = y
    
    return points, map

def main():
    upperPoints, upperMap = pointCounter(upperHeartFunction)
    bottomPoints, bottomMap = pointCounter(bottomHeartFunction)
    print("\nUpper points = ", upperPoints, "\n\nBottom points = ", bottomPoints,)
    print("\nUpper map = ", upperMap, "\n\nBottom map = ", bottomMap)

if __name__ == '__main__':
    main()