import credentials
import tweepy

auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Prints my Timeline Tweets
'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(f'{tweet.user.screen_name}: \n {tweet.text} \n {"*"*60}')
'''

# Search Tweets
def searchTweets(topic):
    id = None
    count = 0
    while count <= 3000: # Se supone que admite hasta 3.000 tweets cada 15 minutos.
        tweets = api.search(q = topic, lang = 'es', tweet_mode = 'extended', max_id = id)
        for tweet in tweets:
            if tweet.full_text.startswith('RT'):
                count += 1
                continue
            f = open((topic + '.txt') , 'a', encoding='utf-8')
            f.write(tweet.full_text + '\n')
            f.close
            count += 1
        id = tweet.id # id del último tweet
    print(count)


searchTweets('#Colombia')