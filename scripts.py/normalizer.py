import numpy as np


# arr is 3x1478 matrix
arr = np.loadtxt("formatData.txt", delimiter = ",", unpack = False)
# creates 1x1478 time data matrix
arrTime = arr[:,1:2] 
# creates 1x1478 funding data matrix
arrFunding = arr[:,2:]

arrFinal = []


# computes mean of funding matrix
muFunding = np.mean(arrFunding)
# finds the min
minFunding = min(arrFunding)
# finds the max
maxFunding = max(arrFunding)

# computes mean of time matrix
muTime = np.mean(arrTime)
# finds the min
minTime = min(arrTime)
# finds the max
maxTime = max(arrTime)

n = len(arrTime)

# normalizes the data
for i in range(n):
    
    # normalize all of arrFunding
    arrFunding[i] = (arrFunding[i] - muFunding) / (maxFunding - minFunding)
    
    # normalize all of arrTime
    arrTime[i] = (arrTime[i] - muTime) / (maxTime - minTime)
    
    # appends 1.0, ith value, ith value to arrFinal
    arrFinal.append([1.0, arrTime[i], arrFunding[i]])

# saves 3x1478 matrix as text file to be ran through gradient decent   
np.savetxt("normalData.txt", arrFinal, delimiter = ",")
