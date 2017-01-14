#!/usr/bin/env python
#-*- coding: utf-8 -*-
import base64
import urllib2
import inkex
import json


class UnsplashPlaceholder(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('-W', '--width', action='store', type='string', dest='width',
                                     default='800', help='Set image width')
        self.OptionParser.add_option('-H', '--height', action='store', type='string', dest='height',
                                     default='680', help='Set image height')
        self.OptionParser.add_option('-O', '--orientation', action='store', type='string', dest='orientation',
                                     default='landscape', help='Set image orientation')
        self.OptionParser.add_option('-Q', '--query', action='store', type='string', dest='query',
                                     default='', help='Topic of the image')

    def effect(self):

        query = self.options.query

        svg = self.document.getroot()

        layer = inkex.etree.SubElement(svg, 'g')
        layer.set(inkex.addNS('label', 'inkscape'), '%s image' %(query))
        layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')

        image = self._get_image()
        node = self._create_image_node(image)

        layer.append(node)

    def _get_image(self):
        url = 'https://api.unsplash.com/photos/random?client_id=9fa51188628ff4193338bfb3edf52e1304f21698fcaa47b9aa726a24a748ee11&featured=true&w={width}&h={height}&orientation={orientation}&query={query}'.format(
                                                                    width=self.options.width,
                                                                    height=self.options.height,
                                                                    orientation=self.options.orientation,
                                                                    query=self.options.query
                                                                    # count=self.options.count
                                                                    )
        response = urllib2.urlopen(url)
        dataUrl = response.read()
        data = json.loads(dataUrl)
        imageUrl = urllib2.urlopen(data['links']['download'])
        image = imageUrl.read()
        return image

    def _create_image_node(self, image):
        attribs = {
            'height': self.options.height,
            'width': self.options.width,
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
