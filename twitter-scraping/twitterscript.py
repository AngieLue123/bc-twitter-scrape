import tweepy

# your bearer token
# MY_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIdBdAEAAAAAZWBqcXnUcN8LZaskM8C53HVLAL8%3DunlaKgRFflGuyORKaXBuC5vKsHdSfZnbjKj5oti5VP51OSaw7c"
# consumer_key = "AACfxea0Piq6LlcOsgCGwHSLM"
# consumer_secret = "2TbbyqK3i8RMl7NS2KKpEMq97NWZF5uaJZxDS6zK219OFt3CLH"
# access_token = "3160571802-E6TQ7h1fvIxAiUHdOVjWjwDyEGQwKnRsz2mmXoL"
# access_token_secret = "od6k18AWcjhImm7kyxdPQYS9UflVV4HUyOS4Jgi9DgugD"
MY_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHrvegEAAAAAkrgD7m5CSOFHJWrHjIPK0%2FtEYck%3D7IAtGK85T9ORIgSdehuj48oOthjGv9P9Y6pHtdc2UAahAoEwZa"
consumer_key = "HxLcIPV6AvhzhTXt5T3ZnhL9M"
consumer_secret = "co3BpC8EhCtRJ2LSUGevTcBrAs1q6Vnl2SD9Xx190FtdbponHs"
access_token = "1251006517299408896-lpEYU4uSYCYRPuAKBaITLHPU0Ck5EN"
access_token_secret = "nSK2rt6ChlVwiO8OZaglQAtrlkzL9rHZoptqnIsEz1b4f"

# create your client 
client = tweepy.Client(bearer_token=MY_BEARER_TOKEN)

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth)

# query to search for tweets
query = "#cloudcomputing"

# get tweets from the API
tweets = client.search_recent_tweets(query=query,
                                     tweet_fields = ["created_at", "text", "source"],
                                     user_fields = ["name", "username", "location", "verified", "description"],
                                     max_results = 100,
                                     expansions='author_id'
                                     )


# get user ids from tweets
users = []
for t in tweets.data:
    t_dict = dict(t)
    users.append(t.author_id)


# text to be sent
text = "Hi! My name is Jayden, and I’m part of an undergrad research group at UCLA focused on understanding cloud computing infrastructure priorities, trends, and marketing needs for AI developers and business focused clients. If you have career experience in these fields or know anyone who does, we would greatly appreciate it if you could spend 5 minutes completing our quick survey linked here: https://bit.ly/AICloudSurvey. All questions are optional so please feel free to skip any that do not apply. Participants can win free $30 Amazon gift cards, and will receive a summary of the survey findings."

# sending the direct message
n_attempted = 0
n_failed = 0
for recipient_id in users:
    try:
        n_attempted += 1
        msg = api.send_direct_message(recipient_id, text)
    except:
        n_failed += 1
        print('unable to send')

print(f'attempting to send {n_attempted} messages')
print(f'successfully sent {n_attempted-n_failed} messages')




#put in my own api key things
#put in my own text
#change number of responses (max currently set to 100)
#also custom search filters