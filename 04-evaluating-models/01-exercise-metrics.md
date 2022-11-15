# Metrics

A central question in machine learning: How do I know if my model is working? Or the related: How do I know which of my models is working best?

Typically, we use a variety of metrics to measure model performance. In this section we'll introduce a few of the most commonly used metrics and discuss why we'd want to track them.

### Metrics

Metrics are computed values related to something we care about. We've seen 2 common metrics in the context of the "score" function: the "coefficent of determination" R^2, and accuracy.

Scikit learn has many metrics built into the library which it can track and compute automatically. See the documentation for a big list: [https://scikit-learn.org/stable/modules/model_evaluation.html](https://scikit-learn.org/stable/modules/model_evaluation.html)

It's also possible to build custom metrics in SKLearn, which can be helpful when you have specific domain knowledge about what to track. See an example here: [https://chrisalbon.com/machine_learning/model_evaluation/custom_performance_metric/](https://chrisalbon.com/machine_learning/model_evaluation/custom_performance_metric/)

Metrics are always computed with respect to the model's prediction and the true labels from the training or test data. 

### An Exercise in 3 parts:

In pairs you'll spend 8 minutes (per question) researching and discussing the following 3 questions about some of SKLearns built in metrics. (Keep in mind, they're built in because they're popular!)

After each research period we'll discuss the answer as a class.

##### Question 1: What are precision, recall, and specificity? 

Additionally...Can you think of an example where one of these would be more important than plain old accuracy?

##### Question 2: What are Mean Squared Error and Mean Absolute Error?

Additionally, can think of an example for when you might want to prefer one over the other?

##### Question 3: What is R^2?

Additionally, can you relate this value to MSE or MAE? Is R^2 telling you something similar, or something quite different from those other error metrics?