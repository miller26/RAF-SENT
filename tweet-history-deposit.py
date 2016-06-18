#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import MySQLdb
import twitter

config = {}
execfile("config.py", config)

def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
    auth.set_access_token(config["access_key"], config["access_secret"])
    api = tweepy.API(auth)
    print  screen_name
    #initialize a list to hold all the tweepy Tweets
    alltweets = []
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets)  > 0:
        print "getting tweets before %s" % (oldest)

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))
    #transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
#    print outtweets[1][2]
    for i in range(0,len(outtweets)):
#        print outtweets[i][0],outtweets[i][1],outtweets[i][2]
        upload(outtweets[i][0],outtweets[i][1],outtweets[i][2])
    #write the csv
#    with open('%s_tweets.csv' % screen_name, 'wb') as f:
#        writer = csv.writer(f)
#        writer.writerow(["id","created_at","text"])
#        writer.writerows(outtweets)

    pass


def upload(id, created_at, text):
    # Open database connection
    auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
    auth.set_access_token(config["access_key"], config["access_secret"])
    api = tweepy.API(auth)
    mydb = MySQLdb.connect(config["server"],config["username"],config["password"],config["database"] )

    # prepare a cursor object using cursor() method
    cursor = mydb.cursor()
    user = api.get_user(screen_name = screen_name)
    person_account_id = user.id

    try:
        cursor.execute("INSERT INTO ACTIVITY(PERSON_ACCOUNT_ID, RC_ACTIVITY_TYPE_ID, TWEET_ID, POSTED_DATE, BODY, CREATED_DATE, CREATED_BY_USER_ID, MODIFIED_DATE, MODIFIED_BY_USER_ID) VALUES ( %s ,%s,%s,%s, %s, %s,%s,%s, %s);", (person_account_id ,'1', id, created_at , text, created_at, id,created_at, id))
        mydb.commit()
    except:
        print "Error Occured"
        mydb.rollback()
        cursor.close()
        print "Done"



if __name__ == '__main__':
    #pass in the username of the account you want to download
    screen_name = config['screen_name']
    get_all_tweets(screen_name)

