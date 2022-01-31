from flask import Flask, render_template, url_for
import random
import datetime as dt
import requests

app = Flask(__name__)

num = random.randint(1,100)

now = dt.datetime.now()

year = now.year

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
posts = response.json()

@app.route("/")
@app.route("/index")
@app.route("/blog")
def index():
    return render_template("index.html", num=num, year=year, posts=posts)



@app.route("/guess/<name>")
def guess(name: str):
    params = {
        "name": name,
    }
    response_gender = requests.get(f"https://api.genderize.io", params=params)
    response_gender.raise_for_status()
    gender = response_gender.json()["gender"]

    response_age = requests.get(f"https://api.agify.io", params=params)
    response_age.raise_for_status()
    age = response_age.json()["age"]

    response_nation = requests.get(f"https://api.nationalize.io", params=params)
    response_nation.raise_for_status()
    nation = response_nation.json()["country"][0]["country_id"]

    return render_template("guess.html", name=name.capitalize(), gender=gender, age=age, nation=nation)


@app.route("/post/<int:id>")
def post(id: int):
    post = posts[id -1]
    return render_template("post.html", post=post)




if __name__ == "__main__":
    app.run(debug=True)