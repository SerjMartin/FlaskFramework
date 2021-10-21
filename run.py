import os # import os from python library
from flask import Flask, render_template
# from flask import class name Flask
# capital latter mean class name

app = Flask(__name__)
# variable call app


@app.route("/")  # app.outer decorator @(pie-notation)
# "/"  triggers the index function
def index():  # this function return only Hello, World
    return  render_template("index.html")  # "<h1>Hello,</h1> <h2>World</h2>"


if __name__ == "__main__":  # __name__ is he default name in python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
