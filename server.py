from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', text="Kate")

@app.route("/max")
def render_max():
    return render_template('index.html', text="Max")


@app.route("/list_of_countries")
def list_of_countries():
    from map_drawer import list_of_countries_tree

    country = list_of_countries_tree("world.svg")
    return render_template("list_of_countries.html",countries = country)

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
    print(result)
    return render_template("colored_countries.html", svg_string = result)




# print(draw_country(root, ["NL","BE","CH", "CZ", "GR","IT", "TR","UA", "FR", "ES", "RU"]))
# tree.write('out.svg')

if __name__ == "__main__":
    app.run(port=8080)