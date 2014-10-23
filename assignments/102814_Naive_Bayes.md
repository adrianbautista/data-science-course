# Create a twitter sentiment classifier

Due 10/28/14

* Use with naive bayes and check the sentiment for a keyword of your choice.

* You'll need your own twitter api key.
* Which you get by signing in to twitter (and then searching for api key), and creating an 'application'
* Note that it doesn't matter what you call your application or what the urls you type in are.
* See the "OAuth" section from the NLTK lesson notebook for the tweet acquisition paradigm.

* For the training set, you can use the "STS-Gold Sentiment Corpus". CSV is here.  Note that you need to use `sep = ";"` as an argument, since it uses semi-colons as separators.

Your training set, in this case, is the "STS" corpus.[(CSV is here).](https://gist.githubusercontent.com/datadave/47ed59dd8733b2063dc6/raw/583615c70a1167fcd72899b2d2830493f1c616e6/sts_gold_tweet.csv)

Once you've created your classifier, THEN, run your collected tweets through it, and report on how they scored in terms of sentiment.



Turn in a (link to your) nicely formatted notebook with your well-commented code. You can use this and the previous assignment's code as guidelines.
