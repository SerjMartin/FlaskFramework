import os  # import os from python library
import json
from flask import Flask, render_template
# from flask import class name Flask
# capital latter mean class name

app = Flask(__name__)
# variable call app


@app.route("/")  # app.outer decorator @(pie-notation)
# "/"  triggers the index function
def index():  # this function return only Hello, World
    return render_template("index.html")  # "<h1>Hello,</h1> <h2>World</h2>"


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":  # __name__ is he default name in python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
