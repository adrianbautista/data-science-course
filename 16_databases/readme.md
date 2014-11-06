# Relational Databases

## Core Objectives

* Draw similarities between iterating through data in pandas vs SQL.
* Learn the various ways to aggregate and select data from a database
* Understand principles of database connections in a programming language
* Connecting dots between previous lessons and database use cases

## BEFORE
Load in the two includes csv files: customers.csv and orders.csv.

Write the pandas code that would return or print data frames consisting of the following information:

1. List the first five customers in region 2.
2. Count the number of customers by State
3. Return the number of customers that have a first name that start with 'Z'
4. Return the mean, median, min, max, and standard deviation of age per gender.
5. Count the number of orders by age of customer.

## CORE MATERIAL

### SQL data types:

What are the basic data types in python, and how do they convert to SQL?

|python type|SQL type|
|-----------|---------|
|int|INT, BIGINT|
|float|FLOAT, DECIMAL|
|str|CHAR, VARCHAR, TEXT|
|list/tuple/set|ARRAY|
|dictionary|JSON|
|boolean|BOOLEAN|

Find more about them [here](http://www.postgresql.org/docs/9.3/static/datatype.html).

### SQL SELECT Syntax

```sql
SELECT [columns]
FROM [table]
[JOINS]
[WHERE [equality checks]]
[GROUP BY [columns]]
[HAVING [equality checks]]
[ORDER BY [columns]]
[LIMIT val]
```

**Question**: What are some common aggregation techniques in Pandas, and how would we do them in SQL?

1. Consider the first 4 questions from the start of class. What would the SQL look like?

2. What do we think are some of the advantages and disadvantages to writing SQL (vs say, doing the same thing in pandas)


## SQL database curation (for postgres)

1. Create the database in your shell:
```sh
createdb dellstore
```

2.  dump the .sql file into postgres

```sh
psql -d dellstore -a -f ~/Downloads/dellstore2-normal-1.0/dellstore2-normal-1.0.sql
```

3. open up a connection
```sh
psql
```
```sql
computer=#

\list -- show databases
\c dellstore -- close a connection and open a new one at dellstore
\d -- show tables in dellstore

/* also, just a quick example of
a block of code being commented out.
Consider this similar to python's docstring (Triple quotes)
*/
```


## SQL Joins:

<img src='static/GbJ7N.png'>

PRACTICE: Given joins, how would we approach the last question from the start of class today, using SQL?

## Using SQL in python:

psycopg2 ('psycho pig 2') is the primary connector engine for postgres and python. Docs are [here](http://initd.org/psycopg/docs/).


*Note: First try this line from the terminal for anaconda installation.  This fix works for mac users at least.

`conda install -c https://conda.binstar.org/alefnula psycopg2`

*If you still have issues, try [This fix](http://mithun.co/hacks/library-not-loaded-libcrypto-1-0-0-dylib-issue-in-mac/) may be helpful for those with dylib issues on the mac*


**Other noteworthy connectors**:

[dataset](http://dataset.readthedocs.org/en/latest/api.html) is an incredibly simple orm wrapper around SQLAlchemy. If you feel frustrated in class with psycopg2, try out dataset.

[sqlalchemy](http://www.sqlalchemy.org/) is typically the de-facto ORM for python. You'll find heavier python applications using it. Generally you would not use it unless you're building large applications yourself, or your engineering team uses it as well.

## Using Pandas and psycopg2 together: Storing twitter data from the API.

If we want to keep a "tweet" table, how would we update the following code in python?

See the python script for example code.
