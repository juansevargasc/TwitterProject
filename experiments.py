import credentials
import tweepy

auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(f'{tweet.user.screen_name}: \n {tweet.text} \n Date: {str(tweet.created_at)} {"*"*60}')