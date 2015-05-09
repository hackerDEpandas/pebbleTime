import numpy as np
import pandas as pd

# loads funding data into 1x1483 array
x = np.genfromtxt('OGFD.txt', delimiter = ',', unpack = False)

# creates 1x1483 boolean valued array from x: floats = False; nan = True
boolArr = pd.isnull(x)

# creates empty timeArr
timeArr = []

# creates empty arr
arr = []

# intitalize time to zero
time = 0.0

for i in range(len(x)):

    # update value for time
    time += 30.0

    # store value in timeArr
    timeArr.append(time)
    
    if boolArr[i] == False:
        # stores desired floats from x and timeArr 
        arr.append([1.0, timeArr[i], x[i]])

# saves final 3x1478 arr as a text file
np.savetxt("formatData.txt", arr, delimiter = ",")       
