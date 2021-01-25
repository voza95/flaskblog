from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

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