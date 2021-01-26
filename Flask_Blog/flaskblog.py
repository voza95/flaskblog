from datetime import datetime
from flask import Flask, url_for, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '05afacefed2a03ae3bbe05258fc992c8'

# URI for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# /// are relative path from the current file. Hence site.db will be created in same directory.
db = SQLAlchemy(app)

# Dummy class model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # Here 'Post' refers to Post class
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # Here 'user.id' refer user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"

# Opening python in terminal and running this two line will create the database:
# >>>from flaskblog import db 
# >>>db.create_all()

# To add entry in DB through terminal run:
# >>>from flaskblog import User, Post
# >>>user_1 = User(username='Vaibhav Oza', email='xyz@gmail.com', password='password')
# This tells our database we want to make some changes but this will not save the changes.
# >>>db.session.add(user_1)
# >>>db.session.commit() #this will save the changes in database

# To get data from the DB in terminal run:
# >>>User.query.all()
# [User('Vaibhav Oza','xyz@gmail.com','default.jpg'), User('JohnDoe','jd@gmail.com','default.jpg')]
# >>>User.query.first()
# User('Vaibhav Oza','xyz@gmail.com','default.jpg')
# >>> User.query.filter_by(username='Vaibhav Oza').all()
# [User('Vaibhav Oza','xyz@gmail.com','default.jpg')]
# >>>user = User.query.filter_by(username='Vaibhav Oza').first() # or user = User.query.get(1)
# >>>user.id
# 1



posts = [
    {
        'author': 'Vaibhav Oza',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'January 25, 2021'
    },
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jame Doe',
        'title': 'Blog Post 3',
        'content': 'Third Post Content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "password":
            flash(f'You have logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)

# set: for windows , export for linux
# set FLASK_APP=flaskblog.py
# $env:FLASK_APP = "flaskblog.py"
# flask run

# To stop recall the server run this commend
# set FLASK_DEBUG=1
# Or else use this
if __name__ == "__main__":
    app.run(debug=True)
    # after this we can run this file directly using "python flaskblog.py"