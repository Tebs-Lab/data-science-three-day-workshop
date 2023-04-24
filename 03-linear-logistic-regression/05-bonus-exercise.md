# A Longer Exercise To Challenge You

This exercise is a chance to practice both the data cleaning and model evaluation sections of the pipeline in a more realistic and more open ended way. Once you've learned about other model types, you can also come back to this exercise and see if the new model types outperform your original models. Software is iterative, after all.

## The Challenge

In the datasets folder of this repo you'll find the NYC housing dataset. You saw it in the previous section on working with data as well. If you were paying careful attention during that section you'll have noticed there were a number of issues with that data. Your goal in this exercise is to perform machine learning using that dataset by working it through the steps of the ML lifecycle, in particular you should:

* Clean the NYC housing data to ensure the data is:
    * Accurate.
    * Complete.
    * And appropriate for your chosen task.
* Preprocess the data to give your model the best chance at success.
* Train and evaluate a model.
* Repeat the above steps and evaluate the impact it has on your models' performance.

## Some Hints

### Define The Problem

There are a few different ways you could model this data into an ML problem, but fundamentally it boils down to picking which field you want to call the label. Two examples would be:

* Try to classify each property based on which borough it's in.
    * Make sure you don't leak the target into the data by including Address or Neighborhood fields in the training data.

* Treat this as a regression problem and try predict the price of each property from it's other attributes.
    * This is a genuinely challenging problem so don't set your expectations too high.

### The Data

#### A Starting Point

In working with data there is a Python file called ETL-reading-exercise. This is an okay starting point for cleaning and transforming the dataset, however it is very incomplete, and not entirely consistent. You may wish to use that code as a starting point or a template for the transformations you wish to make to the data. 

#### Some Issues With The Data to Look for

* Missing data, obviously.
* There are a lot of unrealistic values and outliers in several fields, in particular definitely look carefully at:
    * Price
    * Both Square Feet fields
    * Year Built
    * But there are other problems too, so don't ONLY look there.
* Spot check the data for inconsistencies
    * For example, does "residential units" + "commercial units" == "total units" for every record?

#### Preprocessing

* Consider Normalization or Scaling
    * But pick one and do it to all the numeric fields if you're going to.
* Consider the categorical fields
    * Are there good ones to 'one hot' encode? 
        * Be careful about the curse of dimensionality 
* Consider feature selection:
    * Not all of the fields have valuable statistical information with respect to the label.
* Consider feature engineering
    * One hot encoding the address field yields too many columns, but you COULD use an API to turn address -> latitude longitude...

### Modeling

* Record keeping and versioning is your friend. 
    * Develop a consistent strategy for model validation and evaluation.
    * Develop a strategy to record models' hyperparameters and their performance. 
    * Failures are informative, don't forget to record and document things that didn't work.

### Evaluation

* Track multiple fundamental metrics for every model.
    * Precision/recall/specificity ...
    * MSE, RMSE, MAE, R2 ...
* But go beyond baseline metrics:
    * Is your model failing more often on particular kinds of input?
        * Are their outliers or artifacts in the training data that relate to this?
    * When your model is failing, what might the costs of those failures be?
        * Are the acceptable risks, or not?

## A Final Word

This exercise is quite open ended, so there is no "solution" as such. This dataset is problematic in some ways, and quite informational in other ways. Depending on how you chose to model the problem, your model might do quite well or it might do very poorly, but poor performance might be the best you can do under certain circumstances.

Use this exercise as a way to practice the process of machine learning, and as a way to understand and evaluate both the strengths and limitations of ML modeling.



