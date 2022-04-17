import math as m
import numpy as np

outputRound = 2 # how many digits after dot
step = 0.1 # step in for loop and "x" step 

# articule about heart function
# https://towardsdatascience.com/plot-the-shape-of-my-heart-698d4776c51a

# function which return value of upper part of heart function
def upperHeartFunction(num):
    return m.sqrt(1 - (abs(num) - 1) ** 2)

def main():
    # this loop creates points that are used to check the accuracy of the compaction (ex. in Geogebra)
    # https://www.geogebra.org/calculator/evakcq4n

    for x in np.arange(-2, 2 + step, step):
        x = round(x, outputRound)
        y = round(upperHeartFunction(x), outputRound) # function whose points are searched for
    
        print('({},{}),'.format(x, y), end = "")

    print("\n\n")
    # due to fact that "x" step is constant, only difference between consecutive y is needed

    tmp = 0
    for x in np.arange(-2, 2 + step, step):
        x = round(x, outputRound)
        y = round(m.sqrt(1 - (abs(x) - 1) ** 2), outputRound)
        print(round(y-tmp, outputRound), ", ", end = "")
        tmp = y

if __name__ == '__main__':
    main()