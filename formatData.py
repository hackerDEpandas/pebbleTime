import numpy as np

# loads 1x1478 funding data matrix
x = np.loadtxt('fundingData.txt', delimiter = ",", unpack = False)
arr = [26,27,28,29,990]
onesArr = []
timeArr = []
finalArr = []

time = 0.0

y = len(x) + len(arr)

# creates 1x1478 matrix of all ones
for i in range(len(x)):
    onesArr.append(1.0)

# creates 1x1483 time matrix 
for i in range(y):
    time += 30.0
    timeArr.append(time)

# removes broken data points from timeArr. timeArr becomes 1x1478   
for i in range(len(timeArr)):
    if i == arr[0]:
        timeArr.remove(timeArr[i])
        
    elif i == arr[1]:
        timeArr.remove(timeArr[i])
        
    elif i == arr[2]:
        timeArr.remove(timeArr[i])
        
    elif i == arr[3]:
        timeArr.remove(timeArr[i])
        
    elif i == arr[4]:
        timeArr.remove(timeArr[i])
# creates 3x1478 matrix to be ran through gradient decent       
for i in range(len(x)):
    finalArr.append([onesArr[i], timeArr[i], x[i]])

# saves finalArr matrix as a txt file
np.savetxt("formatData.txt", finalArr, delimiter = ",")
