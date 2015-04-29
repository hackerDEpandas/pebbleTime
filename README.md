# Linear Regression (Machine Learning)  for Pebble Time

### Introduction
For this project I used machine learning to try and perdict a final **TotalFundingRaised** for the popular Kickstarter project **Pebble Time**. The *Linear Regression* method, along with the *Gradient Decent* alogrithm, was learnt from Stanfords Machine Learning class taught by Andrew Ng on [Coursera](https://www.coursera.org/course/ml). In specific, the following documantation provides insight on collecting and organizing data to later be ran through the *Linear Regression* machine learning method. 

### Data Source
My data came from a service that was modified, and can be found [here](http://104.236.89.73:8888/project/pebble?snapshot=3). This service took a snapshot every 30 minutes of multiple data points from the pebble project page. I had to parse through the data set, and retrive only the *TotalFundingRaised* data point. Since I was trying to map the data to a function with respect to time, I wrote a script that made a one to one mapping of a time input to a total funding output.

**Example**

Time (minutes)| Total Funding ($)
--- | --- 
30 | $ 7,409,488.01
60 | $ 7,474,673.01
90 | $ 7,559,766.01
.  | .
.  | .


### About Linear Regression
Linear Regression is used to find a line that best fits any given data set. In this example I use the single variable case, as I was only interested in predicting the **TotalFundingRaised** data point as a function of tme. That is to say, put in . 

![alt tag](http://imgur.com/huAcDlZ.png)
