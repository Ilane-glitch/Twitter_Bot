#!/usr/bin/env python

__author__ = "Ilane"
__version__ = "0.1"

#import
import tweepy

# Variables
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN =''
ACCESS_TOKEN_SECRET = ''

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")