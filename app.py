from flask import Flask, render_template, request
import re
import requests
import math
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


def process_query(strg):
    if strg == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    if strg == "token":
        return "We fixed the silly token"
    if "name" in strg:
        return "Molly"
    if "plus" in strg:
        aaa = re.findall(r'\d+', strg)
        return str(sum(map(int, aaa)))
    if "largest" in strg:
        aaa = re.findall(r'\d+', strg)
        return str(max(map(int, aaa)))
    if "multiplied" in strg:
        aaa = re.findall(r'\d+', strg)
        return str(int(aaa[0]) * int(aaa[1]))
    if "square" in strg:
        aaa = re.findall(r'\d+', strg)
        bbb = []
        for n in aaa:
            if math.isqrt(int(n)):
                if abs((float(n))**(1/3) % 1) < 0.01:
                    bbb.append(n)
        return ', '.join(bbb)
    if "minus" in strg:
        aaa = re.findall(r'\d+', strg)
        return str(int(aaa[0]) - int(aaa[1]))
    if "power" in strg:
        aaa = re.findall(r'\d+', strg)
        return str(int(aaa[0])**int(aaa[1]))
    if "prime" in strg:
        aaa = re.findall(r'\d+', strg)
        bbb = []
        for n in map(int, aaa):
            is_prime = False
            if n == 2 or n == 3:
                is_prime = True
            for i in range(4, math.sqrt(n)):
                if n % i == 0:
                    is_prime = True
            if is_prime:
                bbb.append(str(n))
        return ', '.join(bbb)
    return "Unknown"


@app.route("/username", methods=["POST"])
def username():
    input_username = request.form.get("username")

    response = requests.get(
        f'https://api.github.com/users/{input_username}/repos'
    )

    if response.status_code == 200:
        repos = response.json()  # returns list of repos
    else:
        print("Error fetching repos")
        return render_template(
            "username.html",
            username=input_username,
            output_jsons=[]
        )

    commits = []

    for repo in repos:
        url: str = repo["commits_url"]
        commit_response = requests.get(
            url[:-6]
        )
        if commit_response.status_code == 200:
            commits.append(commit_response.json())
        else:
            print("Error fetching commits")
            # return render_template(
            #    "username.html",
            #    username=input_username,
            #    output_jsons=[]
            # )

    o_dicts = []

    for i in range(len(repos)):
        try:
            o_dicts.append({"full_name": repos[i]["full_name"]})
            o_dicts[i]["html_url"] = repos[i]["html_url"]
            o_dicts[i]["updated_at"] = repos[i]["updated_at"]
            o_dicts[i]["sha"] = commits[i][0]["sha"]
            o_dicts[i]["author"] = commits[i][0]["commit"]["author"]["name"]
            o_dicts[i]["message"] = commits[i][0]["commit"]["message"]
        except RuntimeError:
            print("Error accessing commit json")
        except IndexError:
            print("OOB error !")

    return render_template(
        "username.html",
        username=input_username,
        output_jsons=o_dicts
    )
