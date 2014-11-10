# Notes

## Where We are Going
Demonstrate a clean copy of the flask application. We can refer to this for help along the way with coding.



## Nomenclature 
General Web Terms:

* [Cookies](http://en.wikipedia.org/wiki/HTTP_cookie)
* [Sessions](http://stackoverflow.com/questions/3804209/what-are-sessions-how-do-they-work)
* [Cascading Style Sheets](http://www.w3schools.com/css/css_intro.asp)

Flask Terms:

* Templates
	* [Jinja2](http://jinja.pocoo.org/)
* Contexts
	* [Application](http://flask.pocoo.org/docs/appcontext/)
	* [Request](http://flask.pocoo.org/docs/reqcontext/)
* [Message Flashing](http://flask.pocoo.org/docs/patterns/flashing/)
	* Not the same as Adobe Flash!

New SQL Terms:

* Schema

New Python Terms:

* Pickle
* [Decorators](http://www.artima.com/weblogs/viewpost.jsp?thread=240808)

## Data Explanation

Mention the following:

* Where the data came from
	* [musiXmatch](http://labrosa.ee.columbia.edu/millionsong/), part of the [Million Song Dataset](http://labrosa.ee.columbia.edu/millionsong/)
	

	
The ``templates`` and ``static`` directories for Flask. The ``msd`` directory contains helper Python routines to ensure input lyrics are stemmed the same way as in the Million Song Dataset.

	
## Create a Classifier Class 
Define the following in lyrics_classifier.py. The skeleton has all of the definitions but most need to be populated.

	"""Lyrics classifier for Flask application"""
	
	# Our familiar imports	
	import pandas as pd
	from sklearn.feature_extraction.text import CountVectorizer
	from sklearn.naive_bayes import MultinomialNB

	# A new import
	import pickle
	
	# Local imports for the Million Song Dataset stemming algorithm
	from msd.stem import transformLyrics

	class LyricsClf():
		"""A MultinomialNB classifier for predicting artists from lyrics.
		Offers train, save, and load routines for offline and startup
		purposes. Offers predictArtist for online use.
		"""
		def __init__(self,picklefile=None):
			"""Constructor that creates an empty artistLabels dictionary,
			a CountVectorizer placeholder, and a classifier placeholder.
			If a picklefile is specified, the returned object is instantiated
	        from a pickled version on disk.
			"""
			self.artistLabels = dict()
			self.vectorizer = None
			self.clf = None
			if picklefile:
	            self.load(picklefile)
		
		def makeArtistLabels(self,artistList):
			"""Creates a mapping between artist names and
			integer class labels.
			"""
			for i, artist in enumerate(artistList):
				self.artistLabels[artist] = i
		
		def getLabel(self,artist):
			"""Returns the integer label for a given artist.
			Returns -1 if an artist does not exist.
			"""
			if artist in self.artistLabels:
				return self.artistLabels[artist]
			else:
				return -1
		
		def predictArtist(self,lyrics):
			"""Returns an artist name given sample song lyrics.
			Applies the Million Song Dataset stemming routine to
			the lyrics (pre-processing), vectorizes the lyrics,
			and runs them through the MultinomialNB classifier.
			Returns the artist name associated with the predicted
			label.
			"""
			transformed_lyrics = transformLyrics(lyrics)
			df = pd.DataFrame({'Lyrics':[transformed_lyrics]})
			X = self.vectorizer.transform(df['Lyrics'])
			y = self.clf.predict(X)
			for artist, label in self.artistLabels.items():
				if label == y:
					return artist
			return "Artist Not Found (predicted label %d)"%(y)

	
		def train(self,csvfile):
			"""Read in a csv of lyrics then do the following:
			- Turn artist names into class labels
			- Build a CountVectorizer
			- Define the classifier's training inputs and outputs
			- Instantiate the classifier
			- Train the classifier
			"""
			# Read the input file
	    	df = pd.read_csv(csvfile)
	    	
	    	# Create a mapping of artist (string) to label (integer)
	 	  	self.makeArtistLabels(df['Artist'].unique())
	 	   	
	 	   	# Create a new column, Label, which will be the model's output label
		    df['Label'] = df['Artist'].apply(self.getLabel)
		    
		    # Create the input and output for training the classifier
		    self.vectorizer = CountVectorizer()
		    X = self.vectorizer.fit_transform(df['Lyrics'])
		    y = df['Label']
		    
			# Instantiate and train the classifier
		    self.clf = MultinomialNB()
		    self.clf.fit(X,y)
			
		def save(self,picklefile):
			"""Save this LyricsClf object to disk as picklefile."""
			# Note: 'wb' means write in binary mode
			# No effect on Linux/Mac
			# May set line endings in Windows
			pickle.dump(self, open(picklefile,'wb'))
			
		def load(self,picklefile):
			"""Load a LyricsClf object from picklefile.
			Return this loaded object for future use.
			"""
			self = pickle.load(open(picklefile,'rb'))
			return self
			
	# end of LyricsClf class

## Using LyricsClf from the CLI
We will use our new class right from the Python interpreter. After showing that it works, we will pickle it for use with the web app.

	$ python
	>>> from lyrics_classifier import LyricsClf
	>>> lclf = LyricsClf()
	>>> lclf.train('lyrics.csv')
	>>> lclf.predictArtist("i want to hold your hand")
	'The Beatles'
	>>> lclf.save('classifier.p')
	>>> quit()
	
## Review the Basic Web App Database Routines
Edit lyricsapp.py and look at ``connect_db``, ``get_db`` and ``init_db``. All of the code is provided to students.

## Prepare the Database from the Schema (5 mins)

	$ python
	>>> from lyricsapp import init_db
	>>> init_db()
	
The instructor may wish to show this in sqlite3 (don't expect every student to have this utility):

	$ sqlite3 lyrics.db
	SQLite version 3.7.13 2012-07-17 17:46:21
	Enter ".help" for instructions
	Enter SQL statements terminated with a ";"
	sqlite> .tables
	predictions
	sqlite> PRAGMA table_info(predictions);
	0|id|integer|0||1
	1|lyrics|text|1||0
	2|artist|text|1||0
	sqlite> .quit
	
## App testing
The application should load and present the interface, but the prediction form shouldn't do anything because the ``/add`` endpoint is incomplete.

	$ python lyricsapp.py
	 * Running on http://127.0.0.1:5000/
	 * Restarting with reloader

## Build the Views
Finish ``show_predictions()`` and ``add_prediction()``.

	@app.route('/')
	def show_predictions():
    	"""Main view to display all lyric/artist predictions.
	    Returns them in descending order by id.
    	"""
    	db = get_db()
    	cur = db.execute('SELECT lyrics, artist FROM predictions ORDER BY id DESC')
    	predictions = cur.fetchall()
    	return render_template('show_predictions.html', predictions=predictions)
	# end of show_predictions()

	@app.route('/add', methods=['POST'])
	def add_prediction():
    	"""Predicts an artist based on the lyrics posted in the form.
	    Finds the lyrics in the request object's form dictionary.
    	Calls our classifier's predictArtist routine to return an artist
	    name. Connects to the database and inserts the prediction.
    	Flashes a message that the prediction was posted. Redirects the
	    user from the /add endpoint back to the show_predictions endpoint.
    	"""
	    lyrics = request.form['lyrics']
    	artistName = clf.predictArtist(lyrics)
	    db = get_db()
    	# remember how we set our SQL driver to treat rows as dictionaries? win!
	    # note: question mark notation safer than string replacement
    	# helps to prevent SQLi attacks
	    db.execute('INSERT INTO predictions (lyrics, artist) values (?, ?)',
    	    [lyrics, artistName])
	    db.commit()
    	flash('Prediction was successfully posted')
	    # another example where the framework is omnipotent: url_for()
    	return redirect(url_for('show_predictions'))
	# end of add_prediction()

## Run the App!
Run the application now and it should work:

	$ python lyricsapp.py
	 * Running on http://127.0.0.1:5000/
	 * Restarting with reloader


