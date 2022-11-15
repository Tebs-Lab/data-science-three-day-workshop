# Exercise: Applied Metrics for Regression

In this exercise you'll be broken into small teams and asked to discuss the application of different metrics for a few classification tasks. After each topic, we'll discuss the results as a class.

## Discussion Topics:

In your discussion, attempt to answer these questions:

1. How would you use/interpret the R^2 value?
2. How would you use/interpret the MAE value?
3. How would you use/interpret the MSE value?
4. Could you define a threshold for any of these values that you'd be willing to interpret as "good enough" to go to market?
    * What about the opposite, could you define a threshold for any of these values that you'd interpret as a sure sign that your system isn't working well?
5. Consider the average vs the individual failures...
    * If your system's average error is small, but there are a handful of very wrong predictions, what would you do?
6. What are the costs of failure? How far off does an individual error have to be to be considered a failure?
7. Is there a real "ground truth" value for the targets, or is this an inherently subjective question?
    * How does that affect your interpretation of the metrics?

## AI Applications:

### Weather Forecasting

This is a system (or set of systems) that predicts:

1. The temperature on an hour-by-hour basis.
2. The chance of precipitation on an hour-by-hour basis.

### Bail Setting

This is a system that attempts to generate a monetary bail value for someone who has been charged with a crime.
