*09/22/14*

## Exploratory Data Analysis

- (A)quire
- (C)lean
- (E)xplore => descriptives, visualizaiton, split-apply-combine (subset)
- (S)ummarize

Aquire & Clean => also known as *munging*, *wrangling*, *scrubbing*

===

*09/24/14*

## Experimental Design

#### Causation
How "x" causes "y" and its projected trend

#### Correlation
That "x" is a good predictor

## 3 Common Experiment Design Patterns

1. Completely Random (strives to remove bias) 	
2. Randomized Block (segemented to some extend [e.g. "Gender"])
3. Matched pairs (not realistic, identical groups)

## Validating data

Causation is really unrealistic... "correlation does not equal causation"

- chaining - x causes z which causes y
- forking - z causes x and y
- colliders - x and y are independent, but not conditioned on z

## Evaluating Articles

### Article 3

* Does the headline match the content of the story?
	- sort of, its about a higher GPA relative to public schools
	
* Do you think the reporting does injustice to the science?


* What's wrong with the claims of causality?
	- attributed to only the private/public status of the school
	- tried to control using SAT scores and "other measures"
	- claim its the cause for more private students into graduate level programs

* What are alternate, plausible explanations of their results?
	- financial action
	- teaching quality
	- previous education (HS)
	- students at private schools are more likely to enroll in humanites
	- selection of students and exclusivity
	- size of classes, having a relationship with your professor

* Could they have analyzed their data more properly?
	- what happended in 1950? what are the historical implications (changes in policy), grades became more external
	- more explicit about their controls
	- control by majors
	- standardization of teacher quality
	- transfer students who attended both?
	- professors that transferred between schools

**advanced**

* What inferences are actually possible given their data?
	- GPAs in general rose
	- some correlation to higher GPA at a private school

* How are they implemented in python?
	- group by students with similar SAT scores and private/public school
	- get average GPA
	- plotted against graduation date

* If the experiment was flawed, what would have been a proper design?
	- studying students and teachers that had been to both

* Is this practical? If not, how close do you think they could have gotten?
	- probably hard to find a large number of transfer students that have been to both
	
### Article 7

* Does the headline match the content of the story?
	- Yes, it just mentions that this will be a study on the relationship between AEE and incident cognitive impairment in older adults. It makes no claim whether the relationship is strong or if it even exists.
	
* Do you think the reporting does injustice to the science?
	- It's very thorough in describing the procedure used to conduct the study, mentions numbers and confidence levels, and even acknowledges areas that could be furthered studied (e.g. "The significance of overall activity in contrast to vigorous or light activity should be determined").

* What's wrong with the claims of causality?
	- The study acknowledges that this study is limited by its reliance on self-reports. 
	- The definition of "activity" is broad.
	- Cognitive impairment was judged by an exam that could have inherit biases.

* What are alternate, plausible explanations of their results?
	- People with higher cognitive abilities have more will power to perform more activities (so the correlation could be reversed)
	- A healthy diet that someone is more inclined to eat if they are physically active could be a contribution to less cognitive impairment.

* Could they have analyzed their data more properly?
	- They could study family members with differing activity levels but similar genetics?

**advanced**

* What inferences are actually possible given their data?
	- That there is some statistical correlation between AEE and cognitive impairment.

* How are they implemented in python?
	- Group participants by similar AEE (will probably need to round levels to group participants)
	- Plot average results of the Modified Mini-Mental State exam against these groups
	
* If the experiment was flawed, what would have been a proper design?
	- Use more randomized blocks to remove biases that could exist base on gender, race, financial background, education level, etc.
	- Compare AEE and cognitive impairment within these groups instead of a general "elderly population."

* Is this practical? If not, how close do you think they could have gotten?
	- It's costly to find a larger group of participants in human studies so less practical.
	
===

*09/29/14*

## Data Results

* finding linear relationships between the data  
* but not everything is guaranteed to have a relationship


#### how to know what to put on x-axis and what to put on y-axis

* the y-axis should be dependent on x-axis
* if I think brain weight informs how much REM sleep an animal gets, brain weight would be on the x-axis and REM sleep would be on the y-axis

===

*10/01/14*

## Machine Learning

* similar to A.I., teaching a system to learn from data
* two kinds - generalization v. representation
* "features" really means columns
* "K" used as a common variable

#### supervised learning
* know "y", 

#### unsupervised learning
* don't know "y"

===

*10/06/14*

## Linear Algebra

### linear algebra

* y = mx + b vs. y = Bx + p{+E}
* can't plot a direct relationship, will always have some kind of error?
* matrices of the same shape cannot be multipled together
* X and all the others will be dependent on each other in producing Y

### linear regression

* the betas (β) => the coefficients
* X in a linear regression formula will be our matrix?
* transposing the matrix turns M x N into N x M 
	*  X^T refers to the transposed matrix
	*  β will be an array (list of coefficients)
	
### polynomial regression

* if making a linear regression and you have an inverse fitness (negative R^2)... you're in trouble
	* R^2 should be between {0, 1}
	* ideally it should be closer to 1 	
	* means that there is some really bad data in there
* SSE => "sum squared errors"
	* will be between {0, infinity} 
	* MSE => "mean squared errors"
	* MAE => "mean absolute errors"	
	
#### multicollinearity

* if you're trying to predict 'GPA' you could use either income or income tax.. just depends what your hypothesis is.  pick one and then either leave the other one out or you could also replace it.. at this point you're just playing with what makes the  best model for your hypothesis
* if your r^2 is very close to 1 then your model might have collinearity
* if one coefficient is positive and the other negative, also a sign of multicollinearity
* 
	
#### regularization vs. overfitting
	
* overfitting could be bad, because the model will not do well against new data
	* complex and will slow down
* L1 regularization used when lots of features
* L2 regularization used for everything else

===

*10/08/14*

# Logistic regression

## problems with linear regression

* you could get more than 100% (not reality)
* distorted by extremes in the data
	* for example, what gets categorized in "above 50%"
	* dangerous in a classification choice (binary, will be completely wrong)
	* it could throw you in the wrong binary option ('like or dislike two-party system')

## binary categorizations

* from my own project:
	* does "X" impact "Y"?
	* hypothesis vs classification
	* will a certain movie make over 1 billion dollars
	* traits =>
		* 3D movie or not 3D movie
		* animated movie or not animated movie
		
## logistic regression

* GLM (generalized linear model)
* logistic regression gives you the probability that a given dataset will produce a target output
* you want to have as few features as possible to get as accurate of a prediction as possible
* in **supervised**, you will have information about the features and the targets
* as it continues, would work towards a straight line* 

## difference

* the outcome variable can only take two values: [0, 1]
* alpha is the shift 
* beta is the slope
* error term is also different (bernoulli dist - coin toss)

## coefficients of logistic regression

* only indicate if it has positive or negative effect, can't really measure magnitude
* because its been transformed by a log function, you have to untransform it to observe magnitude
* if you had categories (e.g. jobs where 1=plumber, 2=teacher)), you could break it up into binary variables
	* to avoid it being treated on a scale
	* like we did with the movie genres
 
===

*10/22/14*

# Decision Trees

- logistic regression is a linear model
- if you have a computer try to develop the optimal decision tree, it will do so forever
- if playing 21 questions, depending on who and what order the people asking are put in, will develop different trees
- decision trees are being greedy/heuristic... what's the fastest/quickest way to get to the answer


## algorithm process

- remove samples as much as possible
- remove data it doesn't have to classify
- which features can easily remove data (e.g. "removable lens for camera types")
- hunter's algorithm
- can tell the computer guidelines when developing decision tree (max nodes/leaves, min nodes, min samples, optimize against a function)
- a better model does okay on both training set and test set vs. does awesome on the training set vs. the test set
- we want to generalize our model (particularily with data we haven't seen yet)
- pruning an already built tree if it's too specific, introduce some impurity (instead of declaring it is a penguin, it produces 60% likelihood it is a penguin)

## random forest

- give different features and number of observations to different decision trees
- so don't have to do cross-validation, training since its randomized
- more accurate, interpretative
- good with large datasets
- great for hadoop clouds since each hadoop server gets a different tree

## random number generators

- sourced from time, heat of cpu, sometimes amount of random
- also has many seeds (set of random numbers the computer will use)
- so if you forget to set `random_state`, people who try to replicate your training and testing set will get something different


## decision tree sklearn

- criterion gini and entropy usually result in similar outcomes
- min_sample_leaf: needs to have at least 5 samples in that option to make a decision
- "accuracy" = number of correct / number of observations
	- correct means how accurate was its prediction in classifying the data
- "confusion matrix" (actual columns, prediction row), shows true positives and false positives, true negatives and false negatives

### positive rates

- false positive rate = (false positives)/(all negatives)
- true positive rate = (true positives)/(positives)
- with these two rates, you have an X,Y coordinate
	- measure the area under the curve (AUC) as the "score" of how well the algorithm does
	- most accurate would be an area of 1 
		- since connecting (0,0) to (1,1) using (0,1) as the only point in between
		
===

*10/27/14*

# Principal Components Analysis

## pre-class questions

- Why would we prefer not to have correlated features? For OLS regression, what happens when two features are identical? What happens when they're almost identical (highly correlated)?
	- may not want correlated features because you can get **multicollinierity**
	- could end up with negative coefficients
- What are the possible costs/benefits of having more features rather than fewer? What is a "good" number of features?
	- can have over-fitting
	- can become more complex and reduce runtime
	- but having more distinct features could produce a more accurate model

## feature selection

- R^2: measures quality
- p-values: significance of variable

### automating the feature selection process

- random forest: finds importance measures
- could also remove a feature at a time and check the score, feature selection:

```
for f in features:
	remove f
	run model
	score it
	if better?
		rerun func
```

- feature extraction (creating new features from the data?), find the numbers that explain the **variances** and use those as the features.

### principal component extraction and feature extraction

- think image compression (how the outputted/compressed image represents the majority of the OG's image variance)
- it becomes less intuitive because the features are not representative
- used in unsupervised learnings since the categories for the data are not known yet (not labeled), so you cluster the data by parameters to develop natural labels?

> In supervised learning the classes are known in advance and also their types, for instance, two classes good and bad customers. When new object(customer) comes on the basis of its attributes the customer can be assigned to bad or good customer class.
> 
> In unsupervised learning the groups/classes are not already known, we have objects (customers), so group the customers having similar buying habits hence different groups are made of the customers i.e. not known already on the basis of similar habits of buying.

- PCA and the whole process will produce an order of how significant the features are
- the general rule is to cut off at a particular rule
- the other general rule is the **elbow rule**
- PCA works well with normally distributed (linear) data

### kernal tricks

- type of linear transformation that trick it into appearing normally distributed
- if `x = y`, `` x` = y` ``



