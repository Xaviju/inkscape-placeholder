#!/usr/bin/env python
#-*- coding: utf-8 -*-
# import sys, inkex, os
import webbrowser
import urllib2
import tempfile
# import inkex

class unsplashPlaceholder():

    #def __init__(self):
        #inkex.Effect.__init__(self)
        #self.OptionParser.add_option('-w', '--width', action='store', type='string', dest='width', default='640', help='Set image width')
        #self.OptionParser.add_option('-h', '--height', action='store', type='string', dest='height', default='480', help='Set image height')

    def getImage(self):
        #width = self.options.width
        width = '800'
        #height = self.options.height
        height = '480'

        #url = 'https://unsplash.it/' + self.options.width + '/' + self.options.height + '/?random'
        url = 'https://unsplash.it/' + width + '/' + height + '/?random'
        response = urllib2.urlopen(url)
        data = response.read()
        return data

    def createImage(self, data):
        tempFileObj = tempfile.NamedTemporaryFile(mode='w+b',suffix='.jpg',delete=False)
        path=tempFileObj.name
        f=open(path, 'w')
        f.write(data)
        f.close()
        webbrowser.open('file://' + path)

placeholder = unsplashPlaceholder()
getImage = placeholder.getImage()
placeholder.createImage(getImage)
