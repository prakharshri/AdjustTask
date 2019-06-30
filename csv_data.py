# !/usr/bin/python
""" Read data and copy to Postgres"""
from __future__ import print_function
import psycopg2

try:
    # open database connection
    connection = psycopg2.connect(database='D1',
                                  user='sky',
                                  password='test123',
                                  host='localhost',
                                  port='5432')
    print("Opened database successfully")
    cursor = connection.cursor()
    with open('shard1.csv', 'r') as f:
        # Skip the header row
        next(f)
        cursor.copy_from(f, 'sharde1',
                         sep=',',
                         columns=('id', 'index',
                                  'country', 'created_at',
                                  'paid', 'installs'))
        connection.commit()
    with open('shard2.csv', 'r') as f:
        # Skip the header row
        next(f)
        cursor.copy_from(f, 'sharde1',
                         sep=',',
                         columns=('id', 'index',
                                  'country', 'created_at',
                                  'paid', 'installs'))
        connection.commit()
    with open('shard3.csv', 'r') as f:
        # Skip the header row
        next(f)
        cursor.copy_from(f, 'sharde1',
                         sep=',',
                         columns=('id', 'index',
                                  'country', 'created_at',
                                  'paid', 'installs'))
        connection.commit()
        print("Data imported successfully")
except (Exception, psycopg2.DatabaseError) as error:
    print("Error while importing data to table", error)
finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
