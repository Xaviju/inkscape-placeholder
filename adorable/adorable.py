#!/usr/bin/env python
#-*- coding: utf-8 -*-
import base64
import urllib2
import inkex


class AdorablePlaceholder(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('-s', '--size', action='store', type='string', dest='size',
                                     default='128', help='Desired Image size')
        self.OptionParser.add_option('-n', '--name', action='store', type='string', dest='name',
                                     default='128', help='Avatar name')

    def effect(self):
        name = self.options.name

        svg = self.document.getroot()

        layer = inkex.etree.SubElement(svg, 'g')
        layer.set(inkex.addNS('label', 'inkscape'), '%s avatar' %(name))
        layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')

        avatar = self._get_avatar()
        node = self._create_image_node(avatar)

        layer.append(node)


    def _get_avatar(self):
        url = 'https://api.adorable.io/avatars/{size}/{name}'.format(
            size=self.options.size,
            name=self.options.name
        )

        response = urllib2.urlopen(url)
        avatar = response.read()
        return avatar

    def _create_image_node(self, avatar):
        attribs = {
            'height': self.options.size,
            'width': self.options.size,
            'x': '0',
            'y': '0',
            'preserveAspectRatio': 'None',
            inkex.addNS('href', 'xlink'): u'data:image/jpeg;base64,' + base64.encodestring(avatar)
        }
        node = inkex.etree.Element(inkex.addNS('image','svg'), attribs)
        return node


if __name__ == '__main__':
    placeholder = AdorablePlaceholder()
    placeholder.affect()
