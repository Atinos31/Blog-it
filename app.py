  
import os
from flask import (
    Flask, g, Blueprint, flash, render_template, redirect, request, session, url_for)
from werkzeug.exceptions import abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.config["IMAGE_UPLOADS"] = "/workspace/bog-it/static/profile_pics/default.png/"
mongo = PyMongo(app)

#dummy data for blogposts
posts = [
    {
        'author': 'Grace Rock',
        'category': 'Software Development',
        'title': '7 Money Making Side Projects You Can Do As A Developer',
        'content': '1- Ethincal hacking is more active side income than passive income. Personally, I haven’t ‘hacked’ anything yet. But over the past year, I’ve been doing a lot of security-related work and find that organizations are more vulnerable than we actually want to believe.',
        'date_posted': 'August 07, 2021'        
    },
    {
        'author': 'Mary Poppins',
        'title': 'Data related careers',
        'content': 'Data science is not your only career option',
        'date_posted': 'August 08, 2020'
    }
]


@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/")
# function to render the explore page
@app.route("/get_blogs")
def get_blogs():
    blogs = list(mongo.db.blogs.find())
    return render_template("blogs.html", blogs=blogs)


# function to render the post page
@app.route("/get_posts")
def get_posts():
    posts = list(mongo.db.posts.find())
    return render_template("post.html", posts=posts)


# create a register function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))

        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("login", username=session["user"]))

    return render_template("register.html")


# create login function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))



# logout function
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


# upload file function
@app.route("/upload_image", methods=["GET", "POST"])
def upload_image():
    if request.method == 'POST':
        if request.files:
            image = request.files["profile-image"]
            if image.filename == "":
                print('image must have filename')
                return redirect(request.url)
            image.save(os.path.join(app.config[
                "IMAGE-UPLOADS"], image.filename))
            print('image save')
            return redirect(request.url)
    return render_template('profile.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)