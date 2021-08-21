import os
from flask import (
    Flask, g, Blueprint, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import json_util
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/home")
def home():
    """
    Renders home page when site is loaded.
    """
    return render_template('home.html')


@app.route("/")
# route function to render the explore page
@app.route("/get_blogs")
#all the blogs written by users
def get_blogs():
    blogs = list(mongo.db.blogs.find())
    return render_template("blogs.html", blogs=blogs)


# search route function
@app.route("/search", methods=["GET", "POST"])
def search():
    """ Passes querys from  the form then
    searches the Database index forany matching criteria
    """
    query = request.form.get("query")
    blogs = list(mongo.db.blogs.find({"$text": {"$search": query}}))
    return render_template("blogs.html", blogs=blogs)


# create a register route function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        email = request.form.get('email')
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "is_admin": False
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful! please login")
        return redirect(url_for(
            "profile", username=session["user"], email=email))

    return render_template("register.html")


# login  route function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        """
          Login user after checking if user is in the Database
        """
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("You are logged in as: {}".format(
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


# create profile route function
@app.route("/profile/<username>")
def profile(username):
    # grab the session user's username from db , display user's blogs on thier profile
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    blogs = list(mongo.db.blogs.find(
        {"created_by": session["user"]}).sort("_id", -1))
    if session["user"]:
        return render_template(
            "profile.html", username=username, blogs=blogs)

    return redirect(url_for("login"))


@app.route("/upload")
def upload_file():
    return render_template('profile.html')


@app.route('/uploader', methods=["GET", "POST"])
def uploader():
    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'


# add / create blogs
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


# edit/update blog function
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


# delete blog function
@app.route("/delete_blog/<blog_id>")
def delete_blog(blog_id):
    mongo.db.blogs.remove({"_id": ObjectId(blog_id)})
    flash('Blog  has been Successfully deleted!')
    return redirect(url_for("get_blogs"))


# create blog categories
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# add blog categories
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# edit/update category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category SuccessfullY Updated")
        return redirect(url_for("get_categories"))
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# delete category route
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


# error pages
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# logout route implementation
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
