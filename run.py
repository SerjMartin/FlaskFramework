import os  # import os from python library
import json
from flask import Flask, render_template, request, flash
# from flask import class name Flask
# capital latter mean class name
# flash used to sed the messages
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
# variable call app
app.secret_key = os.environ.get("SECRET_KEY")


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


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":  # __name__ is he default name in python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
