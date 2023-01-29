# List of imports used for this script
import tweepy
import MySQLdb


''' Inside the tweet class
['__abstractmethods__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_abc_impl', 'attachments', 'author_id', 'context_annotations', 'conversation_id', 'created_at', 'data', 'edit_controls', 'edit_history_tweet_ids', 'entities', 'geo', 'get', 'id', 'in_reply_to_user_id', 'items', 'keys', 'lang', 'non_public_metrics', 'organic_metrics', 'possibly_sensitive', 'promoted_metrics', 'public_metrics', 'referenced_tweets', 'reply_settings', 'source', 'text', 'values', 'withheld']

'''


#Here are all my api keys
api_key = "WTZvqz2BSTt3gl2O3Rlfx4DXK"
api_key_secret = "eSjQVYR9Uz7XLnSe4CYhlsRDiBJv5a7I22X5wuptljK9XP0cvV"
access_token = "1245369347419365376-RmwfMHdBciXHf3GayIh0B8Zx5RDAN0"
access_token_secret = "o6iM38b2xK3iKGLwlYg3V5WXV7Ed9d54FlJHAIHFij6EA"
bearer_token = "AAAAAAAAAAAAAAAAAAAAACnhkQEAAAAAMuNBTbZuJkYfkOJWahYyO9QqIGE%3DDGqYYopmnLxwkYFzgr5rdQqxpHm1U2czvzs7boztabbwazVEzV"


#Here is the mysqldb connection
mydb = MySQLdb.connect(
    host="localhost",
    database='sys',
    user="root",
    password="i95lk20ds2W!"

    )

# sets the api access point

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Used to print spaces between things if necessary
# Just have this here for my own code
# I dont think it is necessary in a "production" sense
def spacer():
    print("\n\n")



# Uploads the tweet passed object to the database
# Had issues with doing it with a single line in the execute() method but doing two strings, an insertStatement and a dataToBeInserted statement helped
def dbupload(tweet):
    #cursor object allows you to connect multiple things
    dbcursor = mydb.cursor()

    insertStatement = ("insert into TweetCollection(ID, Author, Text, TimeCreated, JSONDATA) Values ( %s,%s,%s,%s,%s)")
    dataToBeInserted = (tweet.id, tweet.author.name, tweet.text, tweet.created_at, tweet)
    dbcursor.execute(insertStatement, dataToBeInserted)
    mydb.commit()


# Used as a debugger function
# Can probably be removed, but I will keep it here if someone wants to call it
def getsTweetInfo(tweet):
    print("TweetID: ", tweet.id)
    print("Tweet Author: ", "AUTHORHOLDER")
    print("Tweet text: " , tweet.text)
    print("Tweet Time created: " , tweet.created_at)
    dbupload(tweet) #This is the important function call. Should be called in another function
    spacer()


# Used as a debugger function
# Gets the 20 most recent tweets from a list of accounts
# This was used during the testing stages alot, but I am altering the for tweet part of it to actually upload to the database
def getUserTweets20(username):
    # use cursor instead of user_timeline beacuse it pulls things better and go back to 3000

    print("User: " , username)
    for tweet in tweepy.Cursor(api.user_timeline, id=username).items(20):
        getsTweetInfo(tweet) #This is the important function for printing



# Gets the list of users
# Adds 
def getUserList():
    with open("usernames", "r") as file:
        #print(file.readlines())
        rulesList = []
        for username in file.readlines():
            #getUserTweets20(username.strip())
            rulesList.append(username.strip())

        return rulesList


def getActualTweetObj(tweetID):
    #print(api.get_status(tweetID))
    dbupload(api.get_status(tweetID))



# This class was basically copied from here
# https://gist.github.com/sparack/e8021298115f4a1289a637e25f284daf
# This is the main way in which it currently calls the api and recieves the tweet

class IDPrinter(tweepy.StreamingClient):

    # Can pull all the necessary info here from the object tweet such as text id date author etc
    # calls the dbupload function so it can actually upload the tweet to the setup database
    #does not pass in a tweet with all of the normal info for it
    #ORIGINALLY I WROTE IT USING ON_TWEET BUT ON_DATA IS THE ONE THAT ACTUALLY PULLS EVERYHTING
    #ORIGINALLY I WROTE IT TRYING TO PULL JUST FROM THE ID BUT I PASS IT TO THE GETACTUALTWEETOBJ THAT WILL HAVE EVERYTHING I NEED THERE
    def on_tweet(self, tweet):
        #print(tweet.id, tweet.author_id , tweet.created_at , tweet.text)
        getActualTweetObj(tweet.id)
        #dbupload(tweet)
    
    '''
    def on_data(self, raw_data):
        print("Inside raw_data")
        print(raw_data)
    '''

    def on_errors(self, errors):
        print("Received error code {errors}")
        self.disconnect()
        mydb.commit() # Added so when everything fails it saves all things to the db
        print("\n\nshould be committed \n")
        return False




# Acts as the main controller of the project
# Calls all necessary functions
# Mostly uses the IDPrinter class for it
def main():

    # Adds all the users to the the filter rules
    # control is the main way in which it all is controlled
    control = IDPrinter(bearer_token)

    # Adds all the users to the list
    rulesList = getUserList()

    print(control.get_rules())

    # now adds each rule to the list
    # This could be put into its own function 
    for rule in rulesList:
        control.add_rules(tweepy.StreamRule("from:%s"%rule))
        print("from:",rule.strip())
    
    print("\n\n")
    print("RUNNING...")
    # Now calls the the filter which will add everything
    control.filter()




main()



