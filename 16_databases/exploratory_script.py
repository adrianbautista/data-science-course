import psycopg2
import psycopg2.extras
try:
    conn = psycopg2.connect("dbname='dellstore' user='edjoy' host='localhost'")
except:
    print "Connection failure; please check connection parameters;"

cur = conn.cursor()
cur.execute('SELECT * from Customers LIMIT 1;')
rows = cur.fetchall()
print rows

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur.execute('SELECT * from Customers LIMIT 1;')
rows = cur.fetchall()

print rows
print rows[0].keys()
print rows[0]['creditcardexpiration']

## Twitter database
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

create_db = 'CREATE DATABASE twitter'
create_table = '''CREATE TABLE tweet (
        id BIGINT,
        text VARCHAR(255),
        created_at TIMESTAMP
    );
    '''
cur.execute(create_db)
conn.commit()

conn = psycopg2.connect("dbname='twitter' user='edjoy' host='localhost'")
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute(create_table)
conn.commit()

from twitter import *
t = Twitter(
    auth=OAuth(
        token=TOKEN,
        token_secret=TOKEN_SECRET,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET)
    )


for h in ['#justsayyes', '#taylorswift']
    results = t.search.tweets(q='#justsayyes', count=100, result_type='mixed')
    for r in results['statuses']:
        try:
            row = {
                'id': r['id'],
                'tweet': r['text'],
                'created_at': r['created_at'],
            }
            cur.execute("""INSERT INTO tweet (id, text, created_at) VALUES (%(id)s, %(tweet)s, %(created_at)s)""", row)
            conn.commit()
        except UnicodeDecodeError:
            conn.commit() # close transaction anyway
            pass

import pandas
df = pandas.read_sql_query('SELECT * FROM tweet;', con=conn)
