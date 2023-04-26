# to install sqlAlchemy, use: pip3 install sqlalchemy==1.4.46
from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
# /// signifies that the database is hosted locally
# within the workspace environment
db = create_engine("postgresql:///chinook")

# creates a meta data class, where the class contains
# a collection of all the table
# objects in the db,
# in addition to all of the associated data within those objects
meta = MetaData(db)

# turn the artist table into a variable
# before establishing columns,
# check what columns exist on table
# so that you can code them in accurately
# this can be done by using sql commands to
# check table like so:
# psql -d chinook(AKA database name)
# SELECT * FROM "TableName" WHERE false;
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# turn the Album table into a variable
# be sure to follow steps above when creating columns
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# turn the track table into a variable
# same as before, follow above steps
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:

    # query 1 - select all records from the "Artist" table
    # s_query = artist_table.select()

    # query 2 - select only the "Name" colmn from the artist table
    # s_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # query 3 - select only the "Queen" colmn from the artist table
    # s_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # query 4 - select only the "Queen" colmn from the artist table
    # s_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # query 5 - select only the "Queen" colmn from the artist table
    # s_query = album_table.select().where(album_table.c.ArtistId == 51)

    # query 6 - select only the "Queen" colmn from the artist table
    s_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(s_query)
    for result in results:
        print(result)
