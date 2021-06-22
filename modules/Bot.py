#!/usr/bin/env python

__author__ = "Ilane"
__version__ = "0.1"

'''
    Imports
'''
import tweepy
from shutil import copyfile
import os

'''
    Variables
'''
# Paths of the differents files
key = 'key.txt'
temp = 'temp.txt'
# Tweep keys
consumer_key = ''
consumer_secret = ''
access_token =''
access_token_secret = ''

'''
    Functions
'''
# Makes a copy of the key file
def save_file(key,temp):
    copyfile(key,temp)

# Remove all the lines w/ '#'
def replace_all(path_):
    with open(path_,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if "#" not in line:
                f.write(line)
        f.truncate()

# Return all the keys from the temporary file
def return_keys():
    file = open(temp, "r")
    file.seek(0)
    return file.readline(), file.readline(), file.readline(), file.readline()

# Copy the keys and remove the '#' from the key file
def load_temp(key,temp):
    save_file(key,temp)
    replace_all(temp)

# Delete the temporary file
def del_temp(temp):
    os.remove(temp)

'''
    Main
'''
# Setup all the keys from the key File
load_temp(key,temp)
consumer_key, consumer_secret, access_token, access_token_secret = return_keys()
del_temp(temp)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")
    