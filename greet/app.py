from flask import Flask, request


app = Flask(__name__)

@app.route("/welcome")
def say_welcome():
    return "Welcome"


@app.route("/welcome/home")
def say_welcomehome():
    return "Welcome home" 


@app.route("/welcome/back")
def say_welcomeback():
    return "Welcome back"


