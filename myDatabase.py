import sqlite3

# create a name for the database
database = 'Company.db'

# create a connection to the database
conn = sqlite3.connect(database)

# conn.execute('DROP TABLE IF EXISTS Customers;')
#
# # create table with fields and datatypes
# conn.execute('''CREATE TABLE Customers
#                 (id INT NOT NULL,
#                 name TEXT NOT NULL,
#                 age INT NOT NULL,
#                 gender TEXT NOT NULL);''')

i = int(input('Press 1 to continue: '))

while i == 1:
    ids = input('Enter id: ')
    name = input('enter name: ')
    age = input('enter age: ')
    gender = input('enter gender: ')

    myTuple = (ids, name, age, gender)
    # ENTER DATA VALUES INTO THE DB
    conn.execute('''INSERT INTO Customers (id,name,age,gender) VALUES
                    (?,?,?,?);''', myTuple)


    # save chnages into db
    conn.commit()
    i = int(input('Press 1 to continue: '))

# print results from query

records = conn.execute('SELECT * FROM Customers;')

for rows in records:
    print(rows)
# closes the db so other programs can access it
conn.close()