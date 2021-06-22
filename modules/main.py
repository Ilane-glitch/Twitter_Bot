#!/usr/bin/env python

__author__ = "Ilane"
__version__ = "0.1"

'''
    Imports
'''
import read
import tweepy

'''
    Variables
'''

# Tweep keys
consumer_key = ''
consumer_secret = ''
access_token =''
access_token_secret = ''

'''
    Main
'''
# Setup all the keys from the key File
read.load_temp(read.key,read.temp)
consumer_key, consumer_secret, access_token, access_token_secret = read.return_keys()
read.del_temp(read.temp)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")
