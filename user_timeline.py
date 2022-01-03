import credentials
import tweepy

auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def user_timel(userID):
    id = None
    count = 0
    while count <= 3000: # Se supone que admite hasta 3.000 tweets cada 15 minutos.
        tweets = api.user_timeline(userID, max_id=id, include_rts=False, exclude_replies=True, tweet_mode='extended')
        for tweet in tweets:
            #if tweet.full_text.startswith('RT'):
                #count += 1
                #continue
            f = open( (userID + '.txt'), 'a', encoding='utf-8')
            f.write(tweet.full_text + ' Date: ' + str(tweet.created_at) + '\n\n')
            #print(f'{tweet.user.screen_name}: \n {tweet.text} \n {"*"*60}')
            
            count += 1
        id = tweet.id # id del último tweet
    f.write(f'Total: {count}, últimoID: {id}')
    print(count)
    f.close

#  Llamado
user_timel('zonafranca')

# Prints my Timeline Tweets


