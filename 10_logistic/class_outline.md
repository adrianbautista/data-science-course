# Logistic Regression/Classification

### Overview


### Background 
* Logistic Regression uses regression method for classification
* Motivation: Load pickled model
* Demonstrate Failure of Linear Regression
	* Threshold Warping
	* > 1
* Advantages
	* Interpretable (coefficients; weights)
	* Parameters are few : increase linearly with dimensionality
	* Extensible to multi-class
	* Foundation for Neural Networks and GLM
* Equation
    * Probability of Y: exp(a + Bx) / (1 + exp(a + Bx))
    * a is location of the 50%, B is the rapidity of the rise
* Coefficient Estimation: Maximum Likelihood Estimation
	* Which values of the coefficients make the observed data most likely to have ocurred?
	* Take the Beta and raise 10^B for odds ratio



### Code 

#### Motivation: Affairs Model

#### Basic Structure: O Rings
* Probability Estimates
* Regularization

#### Multi-Class Prediction: Iris
* Categorical Prediction
* Coefficients
* Test Train
  
#### Predictions - Affairs
* Creating a categorical variable
* Multiple Features
* Scores and coefficients
* Model Prediction
* Persistence

### Practice 
* In teams of 3, create an improved model
* Identify and explain the most predictive features
  
### Homework
* Using the data from your project topic, choose a categorical target
* Choose features to use to predict the target
* Prepare an exploratory analysis of the features and target, include graphs.
* Run a logistic regression on your target using the features
* Make a prediction based on an interesting input set  
* Save your model
* Prepare a test/train split and score your model against the training set
* Turn in the complete analysis as an IPython Notebook	