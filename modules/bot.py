#!/usr/bin/env python

__author__ = "Ilane"

'''
    Imports
'''
import read
import tweepy

'''
    Variables
'''

# Tweep keys
consumer_key,consumer_secret,access_token,access_token_secret = read.key_setup()

'''
    Functions
'''

# Call a Tweet
def tweetCall(message):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    # Create a tweet
    api.update_status(message)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

