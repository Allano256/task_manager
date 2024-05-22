# from flask import render_template
# from taskmanager import app, db

from flask import render_template
from taskmanager import app, db

#To get the app running we create app route
@app.route("/")
def home():
    return render_template("base.html")