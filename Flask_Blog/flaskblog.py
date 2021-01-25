from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template('about.html')

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