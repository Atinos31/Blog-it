import os
from flask import (
    Flask, g, Blueprint, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import json_util
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/home")
def home():
    return render_template('home.html')


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
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


#login function
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


# profile function
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# add blogs
@app.route("/add_blog", methods=["GET", "POST"])
def add_blog():
    if request.method == "POST":
        blog = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "content": request.form.get("content"),
            "img_url": request.form.get("img_url"),
            "published_date": request.form.get("published_date"),
            "tags": request.form.get("tags"),
            "read_time": request.form.get("read_time"),
            "created_by": session['user']
        }
        mongo.db.blogs.insert_one(blog)
        flash('Blog Successfully Added')
        return redirect(url_for("get_blogs"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template('add_blog.html', categories=categories)


@app.route("/edit_blog/<blog_id>", methods=["GET", "POST"])
def edit_blog(blog_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "content": request.form.get("content"),
            "img_url": request.form.get("img_url"),
            "published_date": request.form.get("published_date"),
            "tags": request.form.get("tags"),
            "read_time": request.form.get("read_time"),
            "created_by": session['user']
        }
        mongo.db.blogs.update({"_id": ObjectId(blog_id)}, submit)
        flash('Blog Successfully Updated')

    blog = mongo.db.blogs.find_one({"_id": ObjectId(blog_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template('edit_blog.html', blog=blog, categories=categories)


# error pages
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
