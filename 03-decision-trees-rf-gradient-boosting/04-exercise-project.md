## Mini-Project: Putting it all Together.

Now that we've seen a handful of ML algorithms and explored the fundamentals in a more controlled environment, it's time to put it all together in a slightly larger exercise. It's also time to remove some of the rails, and explore these concepts a bit more freely.

In this exercise you will:

* Select a dataset from Kaggle.
* Download that dataset.
* Perform some EDA.
* Train a few models.
* Evaluate their performance.

## Description of the task

### 1. Get Some Data

Kaggle is a website full of data science and machine learning challenges. Companies and enthusiasts upload data and describe a task they want solved. Some challenges include cash prizes, some are purely academic.

You should browse Kaggle and find a dataset that is interesting to you.

**Don't search for a dataset for more than 30 minutes.**

> If you're have a hard time making a choice just pick one of these two:
> 
> * [Classification: Forest Cover Type](https://www.kaggle.com/c/forest-cover-type-prediction)
> * [Regression: Predict Bike Share Demand](https://www.kaggle.com/c/bike-sharing-demand/)

### 2. Explore the Data

Once you have selected a dataset, download the training data and perform some EDA. 

* What are the features?
* Do any correlate well with the targets or each other?
* Are there any outliers?
* Has the data been well cleaned?
    * Missing values?
    * Incorrect types?
* And so on...

### 3. Clean and Prepare The Data

Decide what to do with any oddities you found during EDA.

* Handle missing values.
* Handle outliers.
* Perform any feature engineering and/or feature selection.
* Scale / normalize the data.
* And so on...

### 4. Form a Hypothesis

* Decide which model types you think will be well suited to this data. 
* Decide on some metrics that you'd call "good enough" to go to market with your model.
* Discuss the risks of using AI for this task.
* Discuss the benefits of using AI for this task.

### 5. Build Some Models

Use SKLearn to build and train a few models.

* Build at least 2 different types of model (e.g. a KNN and a Decision Tree, or a Logistic Regression and a Random Forest)
* Perform a hyperparameter search.

### 6. Evaluate The Models' Performance

* Did any hit your benchmark metrics?
* Which model performed best?
* Did your models display different kinds of bias, or did they fail in similar ways?
* What might you try to improve performance next time?

### 7. Present Your Results

Each group will be asked to discuss their findings with the rest of us including:

* Most interesting observations in EDA.
* Which models you chose and why.
* How they performed. 
* What you'd try next to improve your results.