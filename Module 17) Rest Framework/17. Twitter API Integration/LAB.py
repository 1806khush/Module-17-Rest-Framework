# twitter_fetcher/views.py
import tweepy
from django.shortcuts import render
from django.conf import settings

# Authenticate to Twitter using Tweepy
def authenticate_twitter():
    auth = tweepy.OAuth1UserHandler(
        consumer_key=settings.TWITTER_API_KEY,
        consumer_secret=settings.TWITTER_API_SECRET_KEY,
        access_token=settings.TWITTER_ACCESS_TOKEN,
        access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET,
    )
    api = tweepy.API(auth)
    return api

def fetch_recent_tweets(request):
    """Fetch the latest 5 tweets from a Twitter user."""
    username = request.GET.get('username', 'Twitter')  # Default to 'Twitter' if no username is provided
    count = 5  # Number of tweets to fetch
    
    api = authenticate_twitter()
    
    try:
        # Get the user's timeline (latest 5 tweets)
        tweets = api.user_timeline(screen_name=username, count=count, tweet_mode="extended")
        tweets_data = []
        
        for tweet in tweets:
            tweets_data.append({
                'text': tweet.full_text,
                'created_at': tweet.created_at,
            })
        
        return render(request, 'twitter_fetcher/tweets.html', {'tweets': tweets_data})
    
    except tweepy.TweepError as e:
        return render(request, 'twitter_fetcher/error.html', {'error': str(e)})

