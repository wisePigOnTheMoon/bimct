import os 
from flask import Flask, render_template, request, session, redirect, url_for
from flask_sslify import SSLify

app = Flask('app')
if 'DYNO' in os.environ: 
    sslify = SSLify(app)
app.secret_key = "1234235534534"

@app.route("/")
def index():
    return render_template("/index.html", page="Home Page - BIMCT")

@app.route("/mission")
def mission():
    return render_template("/mission.html", page="Mission - BIMCT")

@app.route("/new_format")
def format():
    return render_template("/new_format.html", page="Format - BIMCT")

@app.route("/archive")
def archive():
    return render_template("/archive.html", page="Archive - BIMCT")

@app.route("/current")
def current():
    return render_template("/current.html", page="Current Contest - BIMCT")

@app.route("/faq")
def faq():
    return render_template("/faq.html", page="FAQ - BIMCT")


@app.route("/people")
def people():
    return render_template("people.html", page="People - BIMCT")

@app.route("/signup")
def signup():
    return render_template("signup.html", page="Signup - BIMCT")

@app.route("/signup_2024")
def signup_2024():
    return render_template("signup_2024.html", page="Spring 2024 - BIMCT")

@app.route("/submit")
def submit():
    val = request.form.items
    print(val)
    return redirect("/signup")
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1000, debug=True)