# you have to install psycopg2 before you can import, install psycopg2 in the
# terminal using:
# pip install psycopg2

import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a coursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 1 - select name from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 2 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# # Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 3 - select only "Queen" from the "Artist" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursos.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
