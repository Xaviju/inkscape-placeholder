#!/usr/bin/env python
#-*- coding: utf-8 -*-
import base64
import urllib2
import inkex
import json


class DiverseUIPlaceholder(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('-g', '--gender', action='store', type='string', dest='gender',
                                     default='female', help='Desired Gender')

    def effect(self):
        gender = self.options.gender

        svg = self.document.getroot()

        layer = inkex.etree.SubElement(svg, 'g')
        layer.set(inkex.addNS('label', 'inkscape'), '%s diverseUI' %(gender))
        layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')

        image = self._get_avatar()
        node = self._create_image_node(image)

        layer.append(node)


    def _get_avatar(self):
        url = 'https://www.diverseui.com/images?count=1&gender={gender}'.format(
            gender=self.options.gender
        )
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

        req = urllib2.Request(url, headers=hdr)

        response = urllib2.urlopen(req)
        dataUrl = response.read()
        data = json.loads(dataUrl)
        imageUrl = urllib2.urlopen(data[0]['url'])
        image = imageUrl.read()
        return image

    def _create_image_node(self, image):
        attribs = {
            'height': '360',
            'width': '360',
            'x': '0',
            'y': '0',
            'preserveAspectRatio': 'None',
            inkex.addNS('href', 'xlink'): u'data:image/jpeg;base64,' + base64.encodestring(image)
        }
        node = inkex.etree.Element(inkex.addNS('image','svg'), attribs)
        return node


if __name__ == '__main__':
    placeholder = DiverseUIPlaceholder()
    placeholder.affect()
