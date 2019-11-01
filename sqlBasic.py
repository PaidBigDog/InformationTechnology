import sqlite3

database = 'world.db' # create variabale name for db

conn = sqlite3.connect(database) # connect to/open db

# record = conn.execute('SELECT Name, Population FROM Country WHERE POPULATION < 100000')
# record = conn.execute('SELECT NAME, CONTINENT FROM Country WHERE GovernmentForm = "Republic" ORDER BY LifeExpectancy')
# record = conn.execute('SELECT NAME, LifeExpectancy FROM Country WHERE LifeExpectancy < 60 ORDER BY LifeExpectancy')
# record = conn.execute('SELECT NAME')

def select_all();

for row in record:
    print(row)

conn.close()