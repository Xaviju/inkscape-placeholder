#!/usr/bin/env python
#-*- coding: utf-8 -*-
#import sys, inkex, os
import urllib2
import re

#connect to a URL
url = 'https://unsplash.it/800/600/?random'
response = urllib2.urlopen(url)
data = response.read()

print(data)
