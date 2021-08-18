import os
from flask import (
<<<<<<< HEAD
    Flask, g, Blueprint, flash, render_template, redirect, request, session, url_for)
=======
    Flask, g, Blueprint, flash, render_template, redirect, request, session, url_for, jsonify)
>>>>>>> 8054a8d96c3c7b315e036728df8177d5cb6a674f
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import json_util
import cloudinary
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
CORS(app)

load_dotenv()


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
<<<<<<< HEAD
ALLOWED_EXTS = {"txt", "jpeg", "jpg", "png"}
=======
cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECRET'))

>>>>>>> 8054a8d96c3c7b315e036728df8177d5cb6a674f

mongo = PyMongo(app)
db = mongo.db


UPLOAD_FOLDER = './static/profile_pics'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


UPLOAD_FOLDER = './static/profile_pics'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

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
        user_email = mongo.db.form.get("email")
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        existing_email = mongo.db.users.find_one(
            {"email": user_email})
        if existing_user:
            flash("That Usernamme is already taken")
            return redirect(url_for("register"))
        if existing_email:
            flash("That email is already taken")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "user_email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))

        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        session["user"] = request.form.get("email")
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
        existing_user = mongo.db.users.find_one({
            "email": request.form.get("email")})

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
    
    """ Profile page
    Finds the profile from the username returns - current_user_profile
    If the profile is not found the user is redirected to profile_not_found.html page
    Finds user from the session['user'] cookie - returns user_session
    If user not in session directs to login.html
    The location function is called and check location - returns loaction
    The member since function is called  to checked for the date the user joined - returns date
"""
    if 'user' in session:
        current_user = mongo.db.users.find_one({"username": username})
        user = mongo.db.users.find_one({'username': session['user']})
        if not current_user:
            return render_template('profile-not-found.html')
<<<<<<< HEAD
=======
    
    if request.method == 'POST':
        location = request.form['user_location']
        about_me = request.form['user_about_me']
        email = request.form['user_email']
        member_since = request.form['memeber_since']
        mongo.db.insert_one({'location': location, 'about_me': about_me, 'email': email, 'member_since': int(member_since)})
        return render_template('profile.html')
>>>>>>> 8054a8d96c3c7b315e036728df8177d5cb6a674f

    if session["user"]:
        return render_template(
            "profile.html", current_user=current_user, user=user)

    return redirect(url_for("login"))


# logout function
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


<<<<<<< HEAD

=======
# upload files route
@app.route("/upload", methods=['POST'])
def upload_file():
  app.logger.info('in upload route')

  cloudinary.config(cloud_name = os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'), 
    api_secret=os.getenv('API_SECRET'))
  upload_result = None
  if request.method == 'POST':
    file_to_upload = request.files['file']
    app.logger.info('%s file_to_upload', file_to_upload)
    if file_to_upload:
      upload_result = cloudinary.uploader.upload(file_to_upload)
      app.logger.info(upload_result)
      return jsonify(upload_result)
 
>>>>>>> 8054a8d96c3c7b315e036728df8177d5cb6a674f
# error pages
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)