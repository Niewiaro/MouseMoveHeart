import math as m
import numpy as np
import matplotlib.pyplot as plt



outputRound = 2 # how many digits after dot
step = 0.01 # step in for loop and "x" step 
enlarge = 100 # define how big heart will be



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

    map = []
    tmp = 0
    point_x = []
    point_y = []

    for x in np.arange(-2, 2 + step, step):
        x = round(x, outputRound)
        y = round(function(x), outputRound) # function whose points are searched for
    
        point_x.append(x)
        point_y.append(y)
        # due to fact that "x" step is constant, only difference between consecutive y is needed
        map.append(round(y-tmp, outputRound))
        tmp = y
    
    return point_x, point_y, map



def plotter(x, y, label: str = "", show: bool = True):
    plt.plot(x, y)
    
    if show:
        # naming the x axis
        plt.xlabel('x - axis')
        # naming the y axis
        plt.ylabel('y - axis')
        # giving a title to my graph
        plt.title('Map graph')
        # function to show the plot
        plt.show()



def main():
    upper_x, upper_y, upperMap = pointCounter(upperHeartFunction)
    bottom_x, bottom_y, bottomMap = pointCounter(bottomHeartFunction)

    plotter(upper_x, upper_y, label = "sqrt", show = False)
    plotter(bottom_x, bottom_y, label = "arccos")

    print("\nUpper map = ", upperMap, "\n\nBottom map = ", bottomMap)

    finalMap = [int(element * enlarge) for element in upperMap]

    bottomMap.reverse() # reverse because bottom part must start where upper finish
    finalMap.extend(int(element * enlarge) for element in bottomMap)
    finalMap.pop(0) # delate first and last element, because there are 0 movment what is just dalay for map
    finalMap.pop()
    print("\nupper size = ", len(upperMap) - 1, "\nbottom size = ", len(bottomMap) - 1)
    print("\nMap to copy = ", finalMap)
    print("\nMap size = ", len(finalMap))

    

if __name__ == '__main__':
    main()