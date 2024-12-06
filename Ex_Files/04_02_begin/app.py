import csv
from flask import Flask, render_template, jsonify # type: ignore


app = Flask(__name__)

with open("/workspaces/hands-on-python-3084712/Ex_Files/04_02_begin/laureates.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate():
    return jsonify(laureates)


app.run(debug=True)
