# Data Science and Machine Learning: The Big Picture

Data Science is, as you might guess, a scientific research discipline. Practitioners leverage the scientific method to form hypotheses, design experiments to test those hypotheses, and carry out those experiments primarily to uncover some sort truth. Data Science is also a software engineering discipline. Practitioners build software systems that leverage the knowledge uncovered by their experiments, often to automate a process or make predictions about the future based on data from the past.

While "data scientist" and "AI engineer" are not perfectly synonymous, there is significant overlap between the two and they'll often collaborate in both research and industrial settings. One of the tools at the forefront of both of these disciplines is machine learning. ML is pushing the state of the art forward in just about every AI subdomain, from language translation to facial recognition.

In this first class we'll take a birds-eye view of AI, ML, and Data Science. First, we'll hammer down a loose definition of these different roles/disciplines and the kinds of responsibilities each one might be assigned. Second, we'll define the AI product lifecycle to further contextualize these roles as well as get a handle on the scope and scale of AI product creation.

After that we'll discuss a few different kinds of machine learning, and differentiate between the types of tasks AI systems can perform. In particular we'll distinguish between the following:

* Classification vs Regression
* Supervised Learning vs Unsupervised Learning vs Reinforcement Learning

With those definitions in hand we'll discuss some concrete applications of this technology, including both successes and some catastrophic failures.

Finally, to close out the day, we'll look at a concrete (albeit simple) example of performing machine learning in Python. Using this simple script, we'll name and define some of the key terminology that we'll be exploring in detail as the course goes on, in particular:

* Test data vs training data vs validation data.
    * Cross validation
* The model training process
* Underfitting and overfitting

## Class Topics

* The Big Picture: What are AI, ML, and Data Science
    * Types of AI
        * Classification vs Regression
        * Supervised Learning vs Unsupervised Learning vs Reinforcement Learning
    * The Machine Learning Product Lifecycle
* Small sampling of ML use cases.
* Prominent ML failures and some causes.
    * Class imbalance.
    * Assumed objectivity.
    * Poor data quality.
    * Adversarial data.
* A Concrete example, with terminology
    * Test data vs training data vs validation data.
        * Cross validation
    * The model training process
    * Underfitting and overfitting

## A Critical Aside, The Command Line:

If you are not already familiar with the command line interface for your computer (Terminal in MacOS and Linux, Powershell in Windows) then read one of these tutorials first.** The use of the command line is absolutely essential for developers of all kinds — from data science to web development. Becoming a proficient user of the command line interface (CLI) is of the utmost importance on your journey, even if it's not exactly a data science concept. **Do not skip this step.**

* [Intro to Terminal for Mac and Linux](https://programminghistorian.org/en/lessons/intro-to-bash)
* [Intro to Powershell for Windows](https://programminghistorian.org/en/lessons/intro-to-powershell)

## Suggested Courses on Pluralsight For Self Guided Study

* [A good high level overview of Data Science, 1.5 hours total video](https://app.pluralsight.com/library/courses/data-science-big-picture/table-of-contents)
    * This will be similar information to what was presented in class, a good chance to get another viewpoint and review some of what we discussed.
* [Understanding Machine Learning With Python, 2 hours total video](https://app.pluralsight.com/library/courses/python-understanding-machine-learning/table-of-contents)
    * This will be a preview of what we'll be doing as the course goes on, including using Jupyter Notebooks and Scikit-Learn to build and train machine learning models in Python.

## Suggested Reading Material For Self Guided Study

These selected readings are all examples of ML products that have been released into the wild or ML research that has been published. This is an incomplete selection, but it does provide examples of ML being used from a wide variety of domains and disciplines. 

You may prefer to do some self-guided research into an area that ML is being applied that is of personal interest to you, which would be perfectly appropriate. 

* [Machine Learning for Weather Prediction at Google](https://ai.googleblog.com/2020/01/using-machine-learning-to-nowcast.html)
* [Machine Learning Solves Protein Folding](https://deepmind.com/blog/article/alphafold-a-solution-to-a-50-year-old-grand-challenge-in-biology)
* [The State of the Art in Machine Translation](https://www.topbots.com/ai-nlp-research-neural-machine-translation/)
* [ML for Email Spam Filtering: A Review](https://www.sciencedirect.com/science/article/pii/S2405844018353404)
* [Clearview AI, The Secretive Company That Might End Privacy as We Know It](https://www.nytimes.com/2020/01/18/technology/clearview-privacy-facial-recognition.html)
* [The Netflix Recommender System](https://dl.acm.org/doi/10.1145/2843948)
* [AlphaGo, Playing Go](https://www.theatlantic.com/technology/archive/2017/10/alphago-zero-the-ai-that-taught-itself-go/543450/)
* [OpenAI Five, Playing DOTA 2](https://openai.com/projects/five/)
* [Attacking Machine Learning With Adversarial Samples](https://openai.com/blog/adversarial-example-research/)
* [Amazon Scraps Secret Resume Scanning Tool](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-againstwomen-idUSKCN1MK08G)
* [Machine Bias in U.S. Justice System](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)