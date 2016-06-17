#!/usr/bin/python

import MySQLdb

# Open database connection
mydb = MySQLdb.connect(“server”,”user”,”password”,”database” )

# prepare a cursor object using cursor() method
cursor = mydb.cursor()

try:
    cursor.execute("INSERT INTO ACTIVITY(PERSON_ACCOUNT_ID, RC_ACTIVITY_TYPE_ID, TWEET_ID, POSTED_DATE, BODY, CREATED_DATE, CREATED_BY_USER_ID, MODIFIED_DATE, MODIFIED_BY_USER_ID) VALUES ( '2345243' ,'1','738165687412133888,2016','2016-06-13 00:00:00', 'chickens dont have lips', '2016-06-13 00:00:01', '1234','2016-06-13 00:00:01', '1')")
    mydb.commit()
except:
    print "Error Occured"
    mydb.rollback()
cursor.close()
print "Done"

