import numpy as np


# arr is 3x1478 matrix
arr = np.loadtxt("formatData.txt", delimiter = ",", unpack = False)
# creates 1x1478 time data matrix
arrTime = arr[:,1:2] 
# creates 1x1478 funding data matrix
arrFunding = arr[:,2:]

arrFinal = []
arrOnes = []
arrTimeFinal = []
arrFundingFinal = []

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
    arrFunding[i] = (arrFunding[i] - muFunding) / (maxFunding - minFunding)
    arrTime[i] = (arrTime[i] - muTime) / (maxTime - minTime)

# updates time matrix with normalized values 
for i in range(len(arrTime)):
    x = arrTime[i]
    arrTimeFinal.append(x[0])
    
# updates funding matrix with normalized values    
for i in range(len(arrFunding)):
    y = arrFunding[i]
    arrFundingFinal.append(y[0])
    
# creates 1x1478 ones matrix    
for i in range(len(arrTimeFinal)):
    arrOnes.append(1.0)

# creates 3X1478 matrix with the updated normalized values for time and funding data    
for i in range(len(arrOnes)):
    arrFinal.append([arrOnes[i], arrTimeFinal[i], arrFundingFinal[i]])

# saves final normalized matrix to be ran through gradient decent    
np.savetxt("normalData.txt", arrFinal, delimiter = ",")
