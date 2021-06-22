#!/usr/bin/env python

__author__ = "Ilane"

'''
    Imports
'''
from shutil import copyfile
import os

'''
    Variables
'''
# Paths of the differents files
key = 'key.txt'
temp = 'temp.txt'

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

    