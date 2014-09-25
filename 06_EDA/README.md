# Exploratory Data Analysis

* [In Class Notebook - Analyzing Movies](http://nbviewer.ipython.org/github/TeachingDataScience/data-science-course/blob/forstudentviewing/06_EDA/06_EDA_Main_Notebook.ipynb)


## Objectives
* Understand the importance of Exploratory Data Analysis
* Be able to recite the steps of EDA, and explain each one, and implement each step with python
* Be able to produce an exploratory report on a given data set in one hour.
  
![](http://pandas.pydata.org/pandas-docs/stable/_images/scatter_matrix_kde.png)

## Core Concepts

### The ACES model for Data Exploration:

Letter | Step | Notes
------ | ---- | -----------
A | Assemble the data frame | Find data, import into Pandas
C | Clean the data frame | Identify and limit columns, rows, indices, dates, etc.
E | Explore global properties | Visualize!  Basic plots, subsets, and stats appropriate to the data set
S | Summarize | Describe the core results and questions along with all key visuals

### Technical Skills

[Wes Mckinney's "Tour of Pandas"](* http://nbviewer.ipython.org/gist/wesm/4757075/PandasTour.ipynb) is a good general resource.

#### Acquisition

* [read_csv, read_table, to_csv](http://pandas.pydata.org/pandas-docs/stable/io.html)
* [Using Pickle](https://wiki.python.org/moin/UsingPickle)
  

#### Cleaning

* [dropna, fillna](http://pandas.pydata.org/pandas-docs/stable/missing_data.html#missing-data-basics)
* [Python String Metods](https://docs.python.org/2/library/stdtypes.html#string-methods)
* [pd.to_datetime](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#time-series-date-functionality)


#### Exploration

**Describing and Grouping**

* [pd.Describe](http://pandas.pydata.org/pandas-docs/stable/basics.html)
* [Boolean Indexing](http://pandas.pydata.org/pandas-docs/stable/indexing.html#boolean-indexing)
* [Split, Apply, Combine](http://pandas.pydata.org/pandas-docs/stable/groupby.html)
 
**Visualizing**

* [Basic Pandas Plotting](http://pandas.pydata.org/pandas-docs/stable/visualization.html#basic-plotting-plot)
* [Pandas Histograms](http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms)
* [Scatter Matrix](http://pandas.pydata.org/pandas-docs/stable/visualization.html#scatter-matrix-plot)
* [Plot Formatting](http://pandas.pydata.org/pandas-docs/stable/visualization.html#plot-formatting)
* [Multiple Figures/Axes in Matplotlib](http://matplotlib.org/users/pyplot_tutorial.html#working-with-multiple-figures-and-axes)



####Summarizing

* [Learn controls of the IPython Notebook](http://nbviewer.ipython.org/github/ipython/ipython/blob/2.x/examples/Notebook/Index.ipynb) as a vehicle for presentations
* A good exploratory summary includes:
	* Links to the source materials
	* Description of the variables
	* Brief summary of the cleaning required
	* Descriptive Statistics and Explanation
	* 
* [Use Markdown](http://daringfireball.net/projects/markdown/syntax) to provide images, links, and text formatting to make your notebook into visually appealing narrative
* [The iPython Notebook Viewer](http://nbviewer.ipython.org/) provides a way to post downloadable analysis on the web directly from your notebook and github accoun.






## Activities

### Before
* Complete the data visualization assignment
* Identify a dataset relative to your project and
   * Create a data dictionary describing each variable
   * Run df.describe() and explain the output
   * Create meaningful subsets of your data
   * Graph your data with histograms
 

### During

* Code along with data exploration
* Independent and group work on data exploration



## Additonal Resources

* [Data Exploration](https://sourcegraph.com/github.com/alpinedatalabs/ODST@master/.tree/notebooks) notebooks at ODST
* [EDA with SAT Scores](http://blog.kaggle.com/2013/01/17/getting-started-with-pandas-predicting-sat-scores-for-new-york-city-schools/)
* [Grouping with Pandas](http://pandas.pydata.org/pandas-docs/dev/groupby.html)
* [Data Wrangling Movies](http://nbviewer.ipython.org/github/cs109/content/blob/master/lec_04_wrangling.ipynb)
* [EDA Questions](http://www.itl.nist.gov/div898/handbook/eda/section3/eda32.htm)
* [Volinksy EDA Presentation](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CCYQFjAA&url=http%3A%2F%2Fwww2.research.att.com%2F~volinsky%2FDataMining%2FColumbia2011%2FSlides%2FTopic2-EDAViz.ppt&ei=VA9QU6ODNu2zsASDooCoAQ&usg=AFQjCNEnkeQXZF7l5fIrUGFIrX48qMYUPw&bvm=bv.64764171,d.cWc)
