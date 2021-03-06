# Gradient Decent (Machine Learning)  for PebbleTime

### Introduction
For this project I used machine learning to try and predict a final **TotalFundingRaised** for the popular Kickstarter project **Pebble Time**. The *Gradient Descent* alogrithm was learnt from Stanfords Machine Learning class taught by Andrew Ng on [Coursera](https://www.coursera.org/course/ml). In specific, the following documentation provides insight on collecting and organizing data to later be ran through the *Linear Regression* model. 

### Data Source (*getData.py*)
My data came from a service that was built by [Jared Halpert](https://github.com/internetsadboy/kickstarter-crawler) which took a snapshot every 30 minutes of multiple data points of the [pebble project](https://www.kickstarter.com/projects/597507018/pebble-time-awesome-smartwatch-no-compromises). It was up to me to parse through the data set and retrieve only the *TotalFundingRaised* data point. Since I was trying to map the data to a function with respect to time, I wrote a script (*formatData.py*) that made a one to one mapping of a time input to a total funding output.

**Example**

Time (minutes)| Total Funding ($)
--- | --- 
30 | $ 7,409,488.01
60 | $ 7,474,673.01
90 | $ 7,559,766.01
.  | .
.  | .


### Plot of Pebble Time Data (*scatter.py*)

The following plot was done on the 17th day of the live Pebble Time project. At about the 24,000 minute (or the 17th day) Pebble Time had raised $ 18,235,853.27, which can be seen on the plot. **NOTE** the x-axis is in minutes, and the y-axis is in millions of dollars.

![alt tag](http://i.imgur.com/L2vNY6t.png)

### About Gradient Decent
Gradient Decent is an optimization algorithm that minimizes a cost function to find a line that best fits any given data set. In this example, I use the single variable case, as I was only interested in predicting the **TotalFundingRaised** data point as a function of time. The goal of this method was to find a simple linear function that would generate output as close as possible to the actual total funding values.

### Parameters, Training Examples, and The Hypothesis Function

![alt tag](http://i.imgur.com/a1GEb0H.png)

The hypothesis function will be the line we obtain that best fits the given data set. We parameterize the hypothesis function by ![alt tag](http://i.imgur.com/MeSkGMw.png) and ![alt tag](http://i.imgur.com/j5ko1yL.png), where ![alt tag](http://i.imgur.com/MeSkGMw.png) and ![alt tag](http://i.imgur.com/j5ko1yL.png) will be the coefficients that when given any input, the output is as close as possible to the true value. The value *m* is just the number of training examples, or the size of our data set.

### Mean Normalizer (*normalizer.py*)
![alt tag](http://i.imgur.com/itblwaX.png)

When using gradient decent one must be careful that the data is weighted correctly, otherwise the alogrithm will blow up. For this particualr example, when I first ran gradient decent, it didn't work. Since I was dealing with a data set that had *dollars* in the millions, and *minutes* in the few thousands,  the algorithm wasn't running properly. **Mean Normalizer** helps to weight the data set so that gradient decent will work. It simply takes an element in an array subtracts the mean of said array, and divides by the *max* minus the *min* of the array. It does this for every element in the array until the entire array is *Normalized*. **Note** When you have obatined the **Hypothesis Fucntion** and start using it to produce output, you must scale back to get the output to make sense.

### The Cost Function (*gradDec.py*)

![alt tag](http://i.imgur.com/BSAyRse.png)

The purpose of the cost function is to compute the sum of the squared errors. Note the difference in the sumation is actually seeing how far off the particular values of ![alt tag](http://i.imgur.com/MeSkGMw.png) and ![alt tag](http://i.imgur.com/j5ko1yL.png) are from the true value in any given iteration. Basically if the gradient decent algorithm is working properly the value for the cost function will be constantly decreasing.

### Computing ![alt tag](http://i.imgur.com/MeSkGMw.png) and ![alt tag](http://i.imgur.com/j5ko1yL.png); the learning rate.

![alt tag](http://i.imgur.com/XGyYemD.png)

For the purposes of this project in particular I intalized ![alt tag](http://i.imgur.com/MeSkGMw.png) and ![alt tag](http://i.imgur.com/j5ko1yL.png) to zero. From the formulas given for the theta values we can see that ![alt tag](http://i.imgur.com/MeSkGMw.png) and ![alt tag](http://i.imgur.com/j5ko1yL.png) will update after each iteration. The greek letter alpha is considered the learnig rate or step size. It is important that the learning rate isn't too large otherwise the gradient decent algorithm will blow up. Conversely if the learning rate is too small the algorithm will require a large number of iterations, and thus would be considered an ineffiecent use of time.


### Conclusion
Overall this was a good learning experience and by the end of the project I was able to predict a final **TotalFundingRaised** for the project. Even though the prediction was off by a few million dollars, it was a success. In fact it was expected to be off because we were using a line to predict a non-linear data set. All in all it was cool to see trends, growth rates, etc of an extremely successful live kickstarter project. With further practice I could see this style of real time analysis to be quite crucial for future kickstarter projects. If you wish to have further information about *Gradient Decent* please see the following [pdf](http://cs229.stanford.edu/notes/cs229-notes1.pdf). I hope you find this readme useful and please let me know if you have any questions.
