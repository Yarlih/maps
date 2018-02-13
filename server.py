from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', text="Kate")

import itertools
def groups_of_countries(countries, items_in_group):
    return list(itertools.zip_longest(*[iter(countries)] *items_in_group))


@app.route("/list_of_countries")
def list_of_countries():
    from map_drawer import list_of_countries_tree, Country

    countries = groups_of_countries(sorted(list_of_countries_tree("world.svg"), key = lambda x: x.name), 4)

    return render_template("list_of_countries.html",countries = countries)

from map_drawer import draw_country
import xml.etree.ElementTree as ET


@app.route("/colored_countries")
def colored_countries():
    ids = request.args.getlist("c")
    if not ids:
        return redirect("/list_of_countries")

    tree = ET.parse("world.svg")

    root = tree.getroot()
    draw_country(root,ids)
    ET.register_namespace("","http://www.w3.org/2000/svg")
    result =  ET.tostring(root).decode()
    return render_template("colored_countries.html", svg_string = result)


if __name__ == "__main__":
    app.run(port=8080)