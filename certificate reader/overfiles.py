#!/usr/bin/env python

import os

def create_file_list(directory):
    a = os.listdir(directory)
    #a.sort(key=lambda x: os.path.getctime(directory + '/' + x))
    return a
    #returns sorted list of files
