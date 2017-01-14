#!/usr/bin/env python
#-*- coding: utf-8 -*-
import base64
import urllib2
import inkex
import ssl


class UnsplashPlaceholder(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('-W', '--width', action='store', type='string', dest='width',
                                     default='800', help='Set image width')
        self.OptionParser.add_option('-H', '--height', action='store', type='string', dest='height',
                                     default='680', help='Set image height')
        self.OptionParser.add_option('-C', '--category', action='store', type='string', dest='category',
                                     default='', help='Set image category')

    def effect(self):
        category = self.options.category

        svg = self.document.getroot()

        layer = inkex.etree.SubElement(svg, 'g')
        layer.set(inkex.addNS('label', 'inkscape'), '%s lorempixel' %(category))
        layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')

        image = self._get_image()
        node = self._create_image_node(image)

        layer.append(node)

    def _get_image(self):
        url = 'http://lorempixel.com/{width}/{height}/{category}'.format(
            width=self.options.width,
            height=self.options.height,
            category=self.options.category
        )
        response = urllib2.urlopen(url)
        image = response.read()
        return image

    def _create_image_node(self, data):
        attribs = {
            'height': self.options.height,
            'width': self.options.width,
            'category': self.options.category,
            'x': '0',
            'y': '0',
            'preserveAspectRatio': 'None',
            inkex.addNS('href', 'xlink'): u'data:image/jpeg;base64,' + base64.encodestring(data)
        }
        node = inkex.etree.Element(inkex.addNS('image','svg'), attribs)
        return node


if __name__ == '__main__':
    placeholder = UnsplashPlaceholder()
    placeholder.affect()
