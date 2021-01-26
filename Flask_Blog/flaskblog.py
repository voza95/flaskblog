from flask import Flask, url_for, render_template, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '05afacefed2a03ae3bbe05258fc992c8'

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