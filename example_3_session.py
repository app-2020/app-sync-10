from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///twitter.db"
app.config['SECRET_KEY'] = 'this is secret, change it!'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "username:{},id:{}".format(self.username, self.id)

class Tweet(db.Model):
    __tablename__ = "tweets"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tweet = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tweets', lazy=True))

@app.route("/login")
def login():
    return render_template(
        "login.html")

@app.route("/login", methods=["POST"])
def handle_login():
    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter(User.username == username).filter(User.password == password).first()

    if user is not None:
        session["username"] = username
        session["user_id"] = user.id
        return redirect(url_for("index"))
    else:
        return render_template("login.html")

@app.route("/")
def index():
    tweets = Tweet.query.all()

    return render_template(
        "index.html",
        tweets = tweets)


app.run(debug = True)
