
from collections import namedtuple

Country = namedtuple("Country", ["name","id"])

import xml.etree.ElementTree as ET
def list_of_countries_tree (f):
    tree = ET.parse(f)
    root = tree.getroot()
    return [Country(name= child.get("data-name"), id= child.get("data-id")) for child in root.findall("{http://www.w3.org/2000/svg}path")]


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


