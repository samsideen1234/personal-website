from flask import Flask, render_template
import sys
import logging

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/about")
def about():
    return render_template("About.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/photos")
def photos():
    return render_template("photos.html")


if __name__ == "__main__":
    

    app.run(debug=True)
 

    







 

