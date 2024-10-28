from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_save = request.form.get("save")
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name,
                           age=input_age, save=input_save)


@app.route("/query")
def get_query():
    query = request.args.get('q')
    return process_query(query)


def process_query(str):
    if str == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    if str == "token":
        return "We fixed the silly token"
    if "name" in str:
        return "Molly"
    return "Unknown"
