#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect(“server”,”user”,”password”,”database” )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM ACTIVITY"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      ACTIVITY_ID = row[0]
      PERSON_ACCOUNT_ID = row[1]
      TWEET_ID = row[2]
      RC_ACTIVITY_TYPE_ID = row[3]
      POSTED_DATE = row[4]
      BODY = row[5]
      CREATED_DATE = row[6]
      CREATED_BY_USER_ID = row[7]
      MODIFIED_DATE = row[8]
      MODIFIED_BY_USER_ID = row[9]
      # Now print fetched result
      print "ACTIVITY_ID=%s,PERSON_ACCOUNT_ID=%s, TWEET_ID=%s, RC_ACTIVITY_TYPE_ID=%s, POSTED_DATE=%s, BODY=%s, CREATED_DATE=%s, CREATED_BY_USER_ID=%s, MODIFIED_DATE=%s, MODIFIED_BY_USER_ID=%s " % \
             (ACTIVITY_ID,PERSON_ACCOUNT_ID, TWEET_ID, RC_ACTIVITY_TYPE_ID, POSTED_DATE, BODY, CREATED_DATE, CREATED_BY_USER_ID, MODIFIED_DATE, MODIFIED_BY_USER_ID)
except:
   print "Error: unable to fetch data"

# disconnect from server
db.close()