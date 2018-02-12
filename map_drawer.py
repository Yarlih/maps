def list_of_countries_minidom (f):
    import xml.dom.minidom

    svg = xml.dom.minidom.parse(f)
    svg.normalize()
    nodes = svg.getElementsByTagName("path")
    countris= []
    for i in nodes:
        name = i.getAttribute("data-name")
        id = i.getAttribute("data-id")
        countris.append((name,id))
    return countris

def list_of_countries_sax(f):
    import xml.sax

    parser = xml.sax.make_parser()

    class SvgParser (xml.sax.ContentHandler):
        def __init__(self):
            xml.sax.ContentHandler.__init__(self)
            self.countries = []

        def startElement(self, name, attrs):
            if name == 'path':
                self.countries.append((attrs.get("data-name"), attrs.get("data-id")))

    svg_parser = SvgParser()
    parser.setContentHandler(svg_parser)
    parser.parse(f)
    return svg_parser.countries


import xml.etree.ElementTree as ET
def list_of_countries_tree (f):
    tree = ET.parse(f)
    root = tree.getroot()
    return [(child.get("data-name"), child.get("data-id")) for child in root.findall("{http://www.w3.org/2000/svg}path")]


# print(list_of_countries_sax("world.svg"))
#print(list_of_countries_minidom("world.svg"))
# print(list_of_countries_tree ("world.svg"))

def change_style(style, new_color):
    a = (dict(i.split(":") for i in style.split(";")))
    a['fill'] = new_color
    b =';'.join([key+':'+value for key, value in a.items()])
    return b

def rgb_to_hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

import colorsys
def hsv_to_rgb(h, s, v):

    b = [int(i* 255) for i in colorsys.hsv_to_rgb(h, s, v)]
    return b


def colors(N):
    return [rgb_to_hex(*hsv_to_rgb(i/360,1,1)) for i in range(0, 360, int(360/N))]


def draw_country(root,counries):
    colors_countries = dict(zip(counries,colors(len(counries))))

    for child in root.findall("{http://www.w3.org/2000/svg}path"):

        country_code = child.get("data-id") or child.get("id")


        if country_code in counries:
            style = child.get("style")
            new_style = change_style(style, colors_countries[country_code])
            child.set("style", new_style)


