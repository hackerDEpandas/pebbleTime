import numpy as np

# The goal is to compute the cost fucntion which is as follows:
# J(theta_zero, theta_one) = 1/2m * sum((theta_zero + theta_one*x - y)**2)


arr = np.loadtxt("normalData.txt", delimiter=",", unpack=False)
xArr = arr[:, 0:2]
yArr = arr[:, 2]
XArr = xArr.transpose()


# creates 2xc matrix
x = np.matrix( XArr )
# creates 1xc matrix
y = np.matrix( yArr )

# intialize guess for theta 1x2 matrix
theta = np.matrix( (0.0, 0.0) )

m,n = x.shape

# take the square of each element in a matrix
def squareMat(A):
    
    # r = rows, c = columns of difference matrix
    r, c = A.shape
    
    for i in range(c):
        A[:, i] = (A[:, i]) ** 2
    return A
    

def costFunction(x, y, theta):
    # returns 1xc hypothesis matrix
    hypothesis = np.dot(theta, x)

    #return the 1xc difference matrix
    difference = hypothesis - y
    
    # r = rows, c = columns of difference matrix
    r, c = difference.shape

    # compute the cost function
    return (1.0/(2.0 * c)) * np.sum(squareMat(difference))
    

def gradientDecent(x, y, theta, alpha, m, numIter):    
    
    for i in range(0, numIter):
        
        J = costFunction(x, y, theta)
        X = x[1, 0:].transpose() 
        # returns 1xc hypothesis matrix
        hypothesis = np.dot(theta, x)
    
        # returns 1xc difference matrix
        difference = hypothesis - y
        
        # returns 1xc dot matrix
        dot = difference * X
        
        # r = rows, c = columns of difference matrix
        r, c = difference.shape
        
        print ("Iteration: %r | Cost: %r") % (i, J)
        
        gradientZero = np.sum(difference)
        gradientOne = np.sum(dot)
        thetaZero = theta[:, 0] - ((alpha/m) * gradientZero)
        thetaOne = theta[:, 1] - ((alpha/m) * gradientOne)
        newTheta = np.concatenate((thetaZero, thetaOne), axis=0)
        theta = newTheta.transpose()
        
    return theta
    
    
    
print gradientDecent(x, y, theta, 0.01, n, 1500)
