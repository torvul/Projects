#Here are all my api keys
api_key = "WTZvqz2BSTt3gl2O3Rlfx4DXK"
api_key_secret = "eSjQVYR9Uz7XLnSe4CYhlsRDiBJv5a7I22X5wuptljK9XP0cvV"
access_token = "1245369347419365376-RmwfMHdBciXHf3GayIh0B8Zx5RDAN0"
access_token_secret = "o6iM38b2xK3iKGLwlYg3V5WXV7Ed9d54FlJHAIHFij6EA"
bearer_token = "AAAAAAAAAAAAAAAAAAAAACnhkQEAAAAAMuNBTbZuJkYfkOJWahYyO9QqIGE%3DDGqYYopmnLxwkYFzgr5rdQqxpHm1U2czvzs7boztabbwazVEzV"




import tweepy



#apiCon = tweepy.StreamingClient(bearer_token)
#apiCon.add_rules(tweepy.StreamRule("Mississippi"))


# This is how it works properly you can call the filter function to get everything
class IDPrinter(tweepy.StreamingClient):

    # Can pull all the necessary info here from the object tweet such as text id date author etc
    def on_tweet(self, tweet):
        print(tweet.text)
        print("")


    def on_errors(self, errors):
        print("Received error code {errors}")
        self.disconnect()
        return False




printer = IDPrinter(bearer_token)

#Deleting rules in twitter api



#printer.add_rules(tweepy.StreamRule("from:torvul"))

#remove this comment and get it to make it print: printer.filter()
'''
rulelist = []
for rule in printer.get_rules().data:
    rulelist.append(rule.id)

for rule in rulelist:
    printer.delete_rules(rule)
'''
printer.filter()

print(printer.get_rules())


#need to figure out a streamrule for users to add their names to it
# this is the explanation about streamrule: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query







