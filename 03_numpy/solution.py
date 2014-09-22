# Import modules
import requests
import csv

# set the url to a string
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'

# use requests to get the data
r = requests.get(url)

# initialize an empty counter dictionary.
counter = {}

# create a csv reader object (a python generator)
# If you're not sure about the difference about iterators vs generators yet,
# check out this link!
# https://wiki.python.org/moin/Generators

reader = csv.reader(r.text.splitlines())

# iterate through the rows of the text file.
for row in reader:
    # check if row exists first. an empty list [] will return false and not pass the if statement
    if row:
        label = str(row[3] + row[9])
        if label not in counter:
            counter[label] = {}
            counter[label]['hours'] = [float(row[12])]
            counter[label]['count'] = 1
        else:
            counter[label]['hours'].append(float(row[12]))
            counter[label]['count'] += 1

# iterate through the keys that you generated to find the average hours per grouping
for k in counter.iterkeys():
    counter[k]['avg_hours'] = round(sum(counter[k]['hours']) / float(counter[k]['count']), 2)

# pretty print the groupings.
for k, v in counter.iteritems():
    print k, 'avg_hours:', counter[k]['avg_hours']