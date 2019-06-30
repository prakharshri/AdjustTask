# !/usr/bin/python
""" Get paid amount of installs for May 2019 per country"""
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
    result_query = '''SELECT a.country, SUM(a.installs)
                      FROM(
                      (SELECT country,SUM(installs) AS installs
                      FROM sharde1
                      WHERE paid = 't'
                      AND (created_at) BETWEEN
                      '2019-05-01 00:00:00' AND '2019-05-30 00:00:00'
                      GROUP BY country)
                      UNION ALL
                      (SELECT country,SUM(installs) AS installs
                      FROM sharde2
                      WHERE paid = 't'AND (created_at) BETWEEN
                      '2019-05-01 00:00:00' AND '2019-05-30 00:00:00'
                      GROUP BY country)
                      UNION ALL
                      (SELECT country,SUM(installs) AS installs
                      FROM sharde3
                      WHERE paid = 't' AND (created_at) BETWEEN
                      '2019-05-01 00:00:00' AND '2019-05-30 00:00:00'
                      GROUP BY country)
                      ) AS a GROUP BY a.country;'''

    cursor = connection.cursor()
    cursor.execute(result_query)
    result = cursor.fetchall()
    connection.commit()
    print("Result fetched successfully\n")
    print("COUNTRY  INSTALLS(TOTAL)\n")
    for res in result:
        print(res[0] + '\t' + str(res[1]))
except (Exception, psycopg2.DatabaseError) as error:
    print("Error while fetching result", error)
finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
