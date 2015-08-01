#!/usr/bin/env python
#-*- coding: utf-8 -*-
import urllib2
import inkex
from lxml import etree

class unsplashPlaceholder(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        #self.OptionParser.add_option('-w', '--width', action='store', type='string', dest='width', default='640', help='Set image width')
        #self.OptionParser.add_option('-h', '--height', action='store', type='string', dest='height', default='480', help='Set image height')

    def getImage(self):
        #width = self.options.width
        width = '800'
        #height = self.options.height
        height = '680'

        #url = 'https://unsplash.it/' + self.options.width + '/' + self.options.height + '/?random'
        url = 'https://unsplash.it/' + width + '/' + height + '/?random'
        response = urllib2.urlopen(url)
        data = response.read()
        print data
        return data

    def createImage(self, data):
        svg = etree.Element("svg")
        #Create a new layer.
        layer = inkex.etree.SubElement(svg, 'g')
        layer.set(inkex.addNS('label', 'inkscape'), 'unsplash')
        layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')

        attribs = {
            'height'    : '800',
            'width'     : '600',
            'x'         : '0',
            'y'         : '0',
            'preserveAspectRatio': 'None',
            inkex.addNS('xlink','href'): 'data:image/jpeg;base64,' + data
        }
        image = inkex.etree.Element(inkex.addNS('image','svg'), attribs)
        layer.append(image)

placeholder = unsplashPlaceholder()
getImage = placeholder.getImage()
placeholder.createImage(getImage)
