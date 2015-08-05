#!/usr/bin/env python
#-*- coding: utf-8 -*-
import base64
import urllib2
import re
import inkex


class UnsplashPlaceholder(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('-s', '--size', action='store', type='string', dest='size',
                                     default='128', help='Desired Image size')

    def effect(self):
        image = self._get_image()
        node = self._create_image_node(image)

        self.document.getroot().append(node)

    def _get_image(self):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        url = 'http://uifaces.com/random'
        response = opener.open(url)
        data = response.read()
        matches = re.findall(r'<img src="([^"]*)"', data)
        image = matches[0]
        for url in matches:
            size = url.split('/')[-1].split(".")[0]
            if size == self.options.size:
                image = opener.open(url).read()
                break
        return image

    def _create_image_node(self, image):
        attribs = {
            'height': self.options.size,
            'width': self.options.size,
            'x': '0',
            'y': '0',
            'preserveAspectRatio': 'None',
            inkex.addNS('href', 'xlink'): u'data:image/jpeg;base64,' + base64.encodestring(image)
        }
        node = inkex.etree.Element(inkex.addNS('image','svg'), attribs)
        return node


if __name__ == '__main__':
    placeholder = UnsplashPlaceholder()
    placeholder.affect()
