import twitter
import tweepy
import config

auth = tweepy.OAuthHandler(config.TWITTER_API_KEY, config.TWITTER_API_KEY_SECRET)
# auth = tweepy.OAuthHandler(config.CLIENT_ID, config.CLIENT_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
api.update_status('Bot Test')
# client = tweepy.Client(bearer_token=config.TWITTER_BEARER_TOKEN)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
#     print(tweet.id)
# likeID = public_tweets[0].id

# client.like(likeID)
# api.create_tweet('Bot Test')
