# !/usr/bin/python
""" To make local instance of postgres """
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
    shard1_query = '''CREATE TABLE IF NOT EXISTS sharde1(
                                                 id int NOT NULL UNIQUE,
                                                 index int,
                                                 country varchar(50),
                                                 created_at timestamp,
                                                 paid boolean,
                                                 installs int); '''
    shard2_query = '''CREATE TABLE IF NOT EXISTS sharde2(
                                                 id int NOT NULL UNIQUE,
                                                 index int,
                                                 country varchar(50),
                                                 created_at timestamp,
                                                 paid boolean,
                                                 installs int); '''
    shard3_query = '''CREATE TABLE IF NOT EXISTS sharde3(
                                                 id int NOT NULL UNIQUE,
                                                 index int,
                                                 country varchar(50),
                                                 created_at timestamp,
                                                 paid boolean,
                                                 installs int); '''
    cursor = connection.cursor()
    cursor.execute(shard1_query)
    cursor.execute(shard2_query)
    cursor.execute(shard3_query)
    connection.commit()
    print("Shard1,Shard2,Shard3 created successfully in PostgreSQL ")
except (Exception, psycopg2.DatabaseError) as error:
    print("Error while creating PostgreSQL tables", error)
finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
