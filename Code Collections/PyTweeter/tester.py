#This is used for the main test of connections and tweepy and mysqldb
#There are some other things in there that can be read through
#Check the explanation doc to see my full thoughts and explanations on things



import tweepy
import MySQLdb

# Connection Info

api_key = "4XvbLzEDAWzwc4YuOc6pAF6uR"
api_key_secret = "lYvfhJiBRgSyNOrGqifnmQh4yDuXpFKapXyBmTQpo2EhS4geJo"
access_token = "1245369347419365376-ZQbeiIq7gM47TXQda9oheTCyMwcL58"
access_token_secret = "yXIrfm17soMv9FpecMowJOyvyAupclycHIHtKfr8ZCsa3"
bearer_token = "AAAAAAAAAAAAAAAAAAAAACEgcgEAAAAAogXi96R02%2BWWx9wbeKJ2%2BNtLSHI%3D5jl3ilexV6jescYyJ2K25qLYJ86M0G7uLLSrCSlrwhGmCYdZbq"




mydb = MySQLdb.connect(
    host="localhost",
    database='sys',
    user="root",
    password="i95lk20ds2W!"

    )


# Sets up the connection here

#Pushes apces between things
def spacer():
    print("\n\n")

#Gets the API Connection and sets it up
def apiCon():
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api



def dbupload(tweet):
    #cursor object allows you to connect multiple things
    dbcursor = mydb.cursor()

    # this is how it should work but currently I am having an issure with the tweet.text because it contains apostrhes 
    insertStatement = ("insert into TweetCollection(ID, Author, Text, TimeCreated) Values ( %s,%s,%s,%s)")
    dataToBeInserted = (tweet.id, tweet.author.name, tweet.text, tweet.created_at)
    dbcursor.execute(insertStatement, dataToBeInserted)
    


# THE MOST IMPORTANT FUNCTION THAT SHOWS ALL THE IMPORTANT THIGNS I WILL BE USING
#gets information about the tweet that will likely be used to save information to the database
# the tweet class contains important things
# author', 'contributors', 'coordinates', 'created_at', 'destroy', 'entities', 'favorite', 'favorite_count', 'favorited', 'geo', 'id', 'id_str', 'in_reply_to_screen_name', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'is_quote_status', 'lang', 'parse', 'parse_list', 'place', 'retweet', 'retweet_count', 'retweeted', 'retweets', 'source', 'source_url', 'text', 'truncated', 'user']
# these are the important things for this 
# will make the tweetid the primary key for it
def getsTweetInfo(tweet):
    print("TweetID: ", tweet.id)
    print("Tweet Author: ", tweet.author.name)
    print("Tweet text: " , tweet.text)
    print("Tweet Time created: " , tweet.created_at)
    dbupload(tweet)
    spacer()



# Gets the 20 most recent tweets from a list of accounts
def getUserTweets20(username):
    # use cursor instead of user_timeline beacuse it pulls things better and go back to 3000

    print("User: " , username)
    for tweet in tweepy.Cursor(api.user_timeline, id=username).items(20):
        getsTweetInfo(tweet)
    spacer()

# Gets the list of users 
def getUserList():
    with open("usernames", "r") as file:
        #print(file.readlines())
        for username in file.readlines():
            getUserTweets20(username.strip())



api = apiCon()

# Explorers all possible things from the tweet object that is passed in

# Acts as the controller for this test
# Will call all the necessary functions
def main():
  
    getUserList()
    #getUserTweets20(api)
    '''
    for tweet in tweepy.Cursor(api.user_timeline,id='USATODAY').items(20):
        print(tweet.text)
        spacer()

    '''
    #print( dir( tweepy.Cursor(api.user_timeline,id='USATODAY').items() ) )
    mydb.commit()


main()





