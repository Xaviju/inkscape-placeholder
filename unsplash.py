#!/usr/bin/env python
#-*- coding: utf-8 -*-
import urllib2
import inkex
import base64
from lxml import etree

class unsplashPlaceholder(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('-w', '--width', action='store', type='string', dest='width', default='640', help='Set image width')
        self.OptionParser.add_option('-a', '--height', action='store', type='string', dest='height', default='480', help='Set image height')

    def effect(self):
        self.getImage(self.document)

    def getImage(self, document):
        width = self.options.width
        #width = '800'
        height = self.options.height
        #height = '680'

        #url = 'https://unsplash.it/' + self.options.width + '/' + self.options.height + '/?random'
        url = 'https://unsplash.it/' + width + '/' + height + '/?random'
        response = urllib2.urlopen(url)
        data = response.read()
        self.createImage(data, document)

    def createImage(self, data, document):
        self.document=document #not that nice... oh well
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
            'preserveAspectRatio': 'None'
        }

        image = inkex.etree.Element(inkex.addNS('image','svg'), attribs)
        image.set(inkex.addNS('xlink','href'), 'data:%s;base64,%s' % ('image/jpeg', base64.encodestring(data)))
        self.document.getroot().append(image)

e = unsplashPlaceholder()
e.affect()
