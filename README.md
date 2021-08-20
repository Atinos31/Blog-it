# Blog it

![Main Mockup]()

[Link to Live Website]()

[GitHub Repo](https://github.com/)
Happy blogging!


*** 

## About  
Welcome to Blog It, a webapp to helps bloggers with similar interest interact with each other! 
This is a Python Flask app using MongoDB and Flask Mail to produce a social blogging  application.

Blog it brings bloggers together and allows them to interact and share their interests in similar subjects! 
Anyone can write on Blog It. Thought-leaders, journalists, experts, and individuals with unique perspectives can share their thinking here.
The application lets users create a profile that allows them to add their  details, add photos, let other users know when they last posted,how many followers they have add comments both  and private message each other.
The site offers the additional functionality; reset passwords, change passwords contact us, editing and deleting comments, backend validation. Please look at the [features](#features) section for a more detailed description. 

 
## Index – Table of Contents

- [User Experience (UX)](#user-experience--ux-)
- [Strategy](#strategy)
  * [User Stories](#user-stories)
- [Scope](#scope)
- [Structure](#structure)
- [Database](#database)
- [Validation](#validation)
  * [Backend Validation](#backend-validation)
  * [Front End Validation](#front-end-validation)
- [Security](#security)
- [Features](#features)
- [Design](#design)
- [Skeleton](#skeleton)
  * [Layout](#layout)
- [Surface](#surface)
  * [Typography](#typography)
  * [Call to Action](#call-to-action)
  * [Imagery](#imagery)
- [Technologies](#technologies)
    + [Languages & Frameworks](#languages---frameworks)
    + [Front End](#front-end)
    + [Backend](#backend)
    + [Helpers](#helpers)
    + [Planning](#planning)
  * [Flask](#flask)
    + [Testing Tools](#testing-tools)
    + [Technology Configuration](#technology-configuration)
    + [MongoDB](#mongodb)
  * [Flask Mail](#flask-mail)
- [Testing](#testing)
- [Deployment](#deployment)
  * [Configuration](#configuration)
    + [Local Environment](#local-environment)
  * [Adding and Committing files](#adding-and-committing-files)
  * [Deploying](#deploying)
  * [Forking](#forking)
  * [Cloning](#cloning)
- [Known Bugs](#known-bugs)
- [Acknowledgements](#acknowledgements)
  * [Credit](#credit)
      - [People](#people)
      - [Additional Testers](#additional-testers)
      - [Tools and Docs](#tools-and-docs)
  * [Code:](#code-)
  * [Content:](#content-)
  * [Inspiration & Research:](#inspiration---research-)


*** 

## User Experience (UX)
## Strategy
Everyone has got something interesting to say or even full depth of knowledge about a particular subject.
Blog it enables people to blog about anything and everything and also provides users with a way to communicate with others and attain information about a particular subject.


### User Stories 

#### New User
* I would like to find out what the site is about
* i would like to explore blogposts written by other bloggers without registering
* I would like to easily register 
* I would like to be able to add my profile details ie username


#### Existing User
* I want to be able to sign in and out easily
* I would like to be able to delete my account
* i would like to be able to reset my password incase i forgot my previous password
* I would like to be able to add/read/edit and delete my blogposts.
* I would like to be able to check out other user's profiles.
* I would like to follow users that interest me.
* I would like other users to follow me.
* I would like to see the blogs by other people to decide which blog I would like to read.
* I would like to easily add new blogs.
* I would like to receive any feedback in comments or messages on the site for new posts.
* I would like to leave a comment for blogs that interest me. I understand I’ll have to sign in to do this.
* I would like to be able to upload a profile photo or change my profile photo. 
i.  If I don’t have a profile photo, I'd like to have a choice of placeholder (default avatar). 

## Features
 
### Existing Features
- User Registration: allows new users to create an account so they can log in.
- User Log-in: allows existing users to log in using their username or email and password. Passwords are hashed for security reasons. Log-in is required to read , post your own blogs and give feedback. 
- User Profiles: allow users to tell others about themselves, provide a username,bio.date stamp, and maybe followers. 
- A user must be logged in to edit their own profile. A user cannot edit someone else's profile. 
- A user must be logged in to view messages and interact with other members.
- Password reset page- allows users to reset their password incase they had forgotten it.
- Expore: This allows both non registered and registered users to explore blogposts in the system that all the users have written.
- Search: allows a registed bloggers  to search for blogposts by simple words and more complex phrases
- Logout : allows a user to securely logout of the page.
- Pagination- user can search other blogposts and users using pagination of old and new posts.
- User comments: users can interact with each other by leaving comments on eachothers blogposts.
- Followers: users are able to follow othe users and choose to filter the blog post list on the home page to include only those from users they follow
- Admin-If user is an admin, He or she can edit and delete blog categories. 

### Features Left to Implement
- Allow users to upload their own cover image for a blog.
- Allow bloggers to rate other people's blogposts.
- Allow bloggers to search for blogposts based on other users' ratings.
- Allow admins to block/suspend users when necessary.
- follower feature
- comments feature
- upload profile pic
***


## Technologies
#### Languages & Frameworks 
* HTML5 - Mark-up language using semantic structure.
* CCS3 - Cascading style sheet used to style.
* JavaScript - Programming language.  
* Python - Programming language
* [Flask](#flask) - Framework + Extensions
* [Materialize](https://materializecss.com/) - CSS Framework for structure, buttons, and some styling
* [jQuery](https://jquery.com/) - Materialize initialising
* Gitpod.io - for writing the code. Using the command line for committing and pushing to Git Hub
* GitHub - hosting repositories
* GIT - Pushing code to repositories

#### Front End
* [Google fonts](https://fonts.google.com/)  - for the font
* [Font Awesome](https://fontawesome.com/) - for icons used

#### Backend 
* [MongoDB](https://www.mongodb.com/)
* [Heroku](https://dashboard.heroku.com/)

#### Helpers
* [Beautifier](https://beautifier.io/) - for helping to keep code tidy 
* [Random Key Gen](https://randomkeygen.com/) - to generate a random secret key
* [Power Mapper](https://www.powermapper.com/) to check for browser compatibility
* [Temp Mail](https://temp-mail.org/en/)

#### Planning
[wireframes](https://lucidchart/app/dashboard/) - for planning of site flow, creating wire frames and general mind mapping


### Flask
The application was built using the [Flask](https://flask.palletsprojects.com/en/1.1.x/) Framework which is reliant on the [Jinja](https://www.palletsprojects.com/p/jinja/) templating language. The application was written in python. 

I used the following Extensions:
* [Flask Mail](https://pythonhosted.org/Flask-Mail/) - For emailing users
* [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - For interacting with the MongoDB database
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/utils/) - For providing security’s, password_hash, check_password_hash



#### Testing Tools
* [HTML Validator](https://validator.w3.org/) - checking the validity of code
* [CSS Validator](https://validator.w3.org/) - checking the validity of code
* [JSHint](https://jshint.com/)- Testing and checking JS.  - checking for errors in code
* [Pep8 Online](http://pep8online.com/) - Testing and checking PEP8 compliance 
* [Am I Responsive](http://ami.responsivedesign.is/#) - checking whether the site is responsive. 
* [Internet Marketing Ninjas](https://www.internetmarketingninjas.com/online-spell-checker.php) - spell check
* [Python Tutor](http://pythontutor.com/) - For function testing 
* [Studio 3T](https://studio3t.com/) - Testing Database Schema 
* [Regrex101](https://regex101.com/r/OnE0BG/1/) - Testing Regrex Patterns
* DEV Tools - Lighthouse


***
#### Technology Configuration

#### MongoDB 

[MongoDB](https://www.mongodb.com/) was used as the database to store the users details to set up MongoDB follow the steps below

* Sign up to MongoDB
* Create a new shared Cluster
* Select a Cloud provider and region
* For free use  m0 cluster tier
* Give your cluster a name
* Go to collections and add a database
* Go to database access and add a username and password

Connecting - via application
* Go back to the cluster overview
* Click the CONNECT button.
* Select 'connect your application'
* Select your language/ driver (I used Python 3.6 or later)
* Copy the connection string and change the details. 
* Set the cluster name, collection name, URI connection string and password as environmental - see [Configuration](#Configeration) to set up your application configurations
 

### Flask Mail 
I have chosen to use Gmail as my mail provider alongside [Flask Mail](https://pythonhosted.org/Flask-Mail/) to send mail to users from within the app. 
You will need to ensure you set your email provider up  to Allow less secure apps otherwise Gmail will block you being able to send/receive emails through the application.  
You will also need to enable IMAP as well.  You can find some helpful tips [Flask Mail Help](https://www.twilio.com/blog/2018/03/send-email-programmatically-with-gmail-python-and-flask.html)
I have used Gmail’s smtp server.  -  see [Configuration](#Configeration) to set up your application configurations


***

## Testing 

[TESTING DOC ](docs/testing.md)

Please see the testing document for Testing


***


## Deployment 

### Configuration 
Beneath your imports you will need to configure your app.py file.  You will need to import your local env.py for local environments.  For [configuration for Heroku](#deploying). 

Configure as follows:

        if os.path.exists('env.py'):
            import env


        app = Flask(__name__)

        app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
        app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
        app.secret_key = os.environ.get('SECRET_KEY')
    

        mongo = PyMongo(app)
        mail = Mail(app)

To start your application, you will need to user the following at the bottom of your app.py file. You will need to ensure that debug=False prior to deployment.

        if __name__ == '__main__':
            app.run(host=os.environ.get('IP'),
                    port=int(os.environ.get('PORT')),
                    debug=False)

You will need to add a Procfile and ensure your requirements.txt are up to date. 
In your root folder in the terminal type - touch Procfile -  this will create a Procfile
Add the following with the following 
    echo web: python app.py

To install the requirements.txt use the following command in the terminal command line
    pip3 install -r requirements.txt



#### Local Environment
Create env.py file in the same file system.  In your route folder type - touch env.py - to create the file. 
Your virtual configurations should look similar to this. You will need to create a SECRET_KEY and input the IP and PORT settings. I used [Random Key Gen](https://randomkeygen.com/).

        import os

        # App config
        os.environ.setdefault("IP", "0.0.0.0")
        os.environ.setdefault("PORT", "5000")
        os.environ.setdefault("SECRET_KEY", "<Your secret key>")

        # MongoDB config
        os.environ.setdefault(
            "MONGO_URI", "mongodb+srv://<user>:<password>@<project>.af8bz.mongodb.net/<database>?retryWrites=true&w=majority")
        os.environ.setdefault("MONGO_DBNAME", "<database>")



### Adding and Committing files

To add files to the repository, take the following steps

In the command line type -
        git add .  
        git commit -m "This is being committed"
        git push

To add all new files or modified file use " ."  - To add a single file, use the pathway to the file eg .index.html  or assets/css/style.css
When committing make sure your comments are clear about what changes have been made. 
Pushing will send your work to the repository


### Deploying 
Requirements for deploying:
* MongoDB Account
* Heroku Account
* Email account

Deploying to [Heroku](https://dashboard.heroku.com/)

* You will need to sign up to [Heroku](https://dashboard.heroku.com/)
* Once logged in click the create new app button
* Select the region closest to you and give the APP a name
* Set your deployment method to 'GitHub'
* Connect to GitHub and login
* Search for the repository you wish to deploy from
* You will need to head to settings and click 'Config Vars'
    * You will now need to set up your Configuration Vars the same way as you did for your env.py
![Config Vars](docs/images/config.png)    
* Make sure you have set up your Procfile and you have updated the requirements.txt prior to deploying    
* Click the deploy tab and go to manual deploy
* Select the branch you wish to deploy and deploy the application
* Once it is deployed you will be able to view the app
* You can set it to automatically deploy every time you push to the repository by enabling the Automatic deploys


### Forking

Forking the GitHub Repository

By forking the GitHub Repository, you can make a copy of the original repository in your own GitHub account.  This means we can view or make changes without making the changes affecting the original.

* Log into GitHub and locate the GitHub Repository.
* At the top of the Repository there is a "Fork" button about the "Settings" button on the menu.
* You should now have a new copy of the original repository in your own GitHub account.
* You will need to install the requirements.txt using the following command the command line
        pip3 install -r requirements.txt
* You will need to set up your local environments and key value pairs for deployment

### Cloning 

Making a Local Clone

* Log into your GitHub then find the gitpod repository
* Under the repository name there is a button that says, "Clone or download". Click on this button.
* If cloning with HTTPS "Clone with HTTPS", copy this link.
* Open Gitbash
* Change the current working directory to the location where you want the cloned directory to be.
* Type git clone, and then paste the URL you copied earlier.

        $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
        Press - Enter- Your local clone will be created.
        $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
                > Cloning into `CI-Clone`...
                > remote: Counting objects: 10, done.
                > remote: Compressing objects: 100% (8/8), done.
                > remove: Total 10 (delta 1), reused 10 (delta 1)
                > Unpacking objects: 100% (10/10), done.
[Click Here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository) for more info on cloning. 

You will need to install the requirements.txt using the following command the command line
        pip3 install -r requirements.txt
* You will need to set up your local environments and key value pairs for deployment and running the application in your local environment. 


## Deployment

This project is hosted on [Heroku](heroku.com). It's been deployed using the following steps:
1. Sign up (new user) or sign in to Heroku account. _I already had an account from previous projects, so only needed to sign in._
1. Click the button at the top right that says "New", select "Create new app" in the dropdown.
1. Choose an app name. __Caution! This must be unique!__
1. Select your region. _In my case, this is Europe._ 
1. You'll be redirected to the Deploy tab of the new app.
1. Go to Deployment method. Select your prefered deployment method. _As my code was already on Github, I chose the "Connect to Github" option. The following steps will be specific to this option._
1. Sign in to your Github account to allow Heroku access to repositories.
1. Search for your repo name. If you can't remember the specific spelling of the name, leave the input field blank and click "Search" to get a list of all your repos.
1. When you've found your repo in the list, click the "Connect" button.
1. You now have the choice to enable automatic deploys or deploy manually. 
1. Your project will need to contain the following in order for Heroku to deploy it:
    - a Procfile: this specifies the commands that are executed by the app on startup. You can use a Procfile to declare a variety of process types, including:
        - Your app’s web server
        - Multiple types of worker processes
        - A singleton process, such as a clock
        - Tasks to run before a new release is deployed.

        _In the case of this project, the Procfile contains only a single line:_
        ```
        echo web: python app.py
        ```
    - a requirements.txt file. This tells Heroku which dependencies need to be installed in order for the project to run. It's created by using the command `pip install` + the name of any dependencies you have (for example, Flask needs to be installed for this project) in the terminal of your prefered editor, followed by the command `pip freeze > requirements.txt` which will write the installed dependencies to a text file which Heroku then installs using `pip install requirements.txt`. 
1. Go to settings in the Heroku tab. Click "Reveal Config Vars". Add the relevant environment variables you've used in your project to the Config Vars so Heroku can access them. Specifically, for this particular project, that means the following Config Vars were added: 
    - DEBUG (set to False to turn off Debug mode in the deployed version. Locally, in development, this variable was set to True.)
    - IP
    - MONGO_DBNAME
    - MONGO_URI
    - PORT
    - SECRET_KEY
1. Check the activity tab. The two most recent items in the list should read "Deployed" and "Build Succeeded" in their status. 
1. Click "Open App" in the top right side if this is the case, this will take you to the live site of the [Blog It]().

### To run this project locally:
1. Clone the [Github repo]() using the green "Clone or download" button. Several options are available here.
1. Open the project in your prefered editor.
1. Create a virtual environment using the command `python -m venv envname`, replacing "envname" with the name you want to give this environment. (More information on virtual environments: https://docs.python.org/3/library/venv.html)
1. Open the virtual environment:
    - Windows Cmd Shell: `<envname>\Scripts\Activate`
    - Posix/Linux bash Shell:
    `$ source <envname>/bin/activate`
1. Install the dependencies using the command `pip install -r requirements.txt`
1. Set up environment variables. There are different ways to do this  depending on your system and/or editor. In my editor of choice, VS Code running on Windows, you can do this in the .vscode directory that's generated for every project. This will contain a settings.json file. Add the following to the json dictionary: 
    ``` 
    "terminal.integrated.env.windows": 
    {
        "MONGO_DBNAME": "theDatabaseName",
        "MONGO_URI": "theDatabaseURL",
        "SECRET_KEY": "YourSecretKeyHere"
    },
    ``` 
1. Run the project in your terminal using the command `python app.py` (like pip, for Unix-based systems you may need to use `python3`).

## Credits

### Content


### Media
   - homepage image1 is from pexels.com by cottonbro 
   [girl in a yellow top](https://www.pexels.com/photo/girl-in-yellow-jacket-holding-white-printer-paper-7595160/)
   - homepage image2 is from pexels.com by Tony Schnagly
   [man in brown sweater using mac book pro](https://www.pexels.com/photo/man-in-brown-sweater-using-macbook-pro-5588211/)
   - blogpost pics
   

### Acknowledgements

- I based the layout for the site on this [flask mini project-code institute]().
