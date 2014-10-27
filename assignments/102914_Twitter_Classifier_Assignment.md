
# Create and use a twitter sentiment classifier

Due 10/29/14

1) Use the provided [training data](https://github.com/TeachingDataScience/data-science-course/tree/forstudentviewing/12_Naive_Bayes/twitter_training) to create a twitter sentiment classifier using Naive Bayes.


2) Describe the resulting sentiment from a topic on Twitter (using your own API key)

3) Summarize your work

4) Create additional classifiers using 1 or more other supervised algorithms.  Note any differences in performance or output.

### Additional Notes

* The training data includes tweets (your "X") which are classified with sentiment ("Y")  use these and Naive Bayes to create a classifier
* You'll then collect new data from Twitter and run it through the completed classifier to see how the classifier rates it.  

* You'll need your own twitter api key which you get by signing in to twitter (and then searching for api key), and creating an 'application'
* Note that it doesn't matter what you call your application or what the urls you type in are.
* See the "OAuth" section from the NLTK lesson notebook for the tweet acquisition paradigm.
* For the training set, use the "STS-Gold Sentiment Corpus" (which has nothing to do with gold, its just pre-coded tweets). CSV is [here](https://github.com/TeachingDataScience/data-science-course/tree/forstudentviewing/12_Naive_Bayes/twitter_training).  Note that you need to use `sep = ";"` as an argument, since it uses semi-colons as separators.  

Your training set, in this case, is this corpus.

Once you've created your classifier, THEN, run your collected tweets through it, and report on how they scored in terms of sentiment.



Turn in a (link to your) nicely formatted notebook with your well-commented code. You can use this and the previous assignment's code as guidelines.
