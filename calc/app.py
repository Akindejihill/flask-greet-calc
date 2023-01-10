# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)


@app.route("/calc")
def calc():
    return """
        <html>
            <body>
                <h1>Calculator</h1><br><br>

                <h2>Add two numbers</h2>
                <form action="/add" method = "GET">
                    <input type="text" id="addnum1" name="a"> + <input type="text" id="addnum2" name="b"><br><br>
                    <input type="submit" value="Add">
                </form><br><br><br>

                <h2>Subtract</h2>
                <form action="/sub" method = "GET">
                    <input type="text" id="subnum1" name="a"> - <input type="text" id="subnum2" name="b"><br><br>
                    <input type="submit" value="Subtract">
                </form><br><br><br>

                <h2>Multiply two numbers</h2>
                <form action="/mult" method = "GET">
                    <input type="text" id="multnum1" name="a"> * <input type="text" id="multnum2" name="b"><br><br>
                    <input type="submit" value="Multiply">
                </form><br><br><br>

                <h2>Divide</h2>
                <form action="/div" method = "GET">
                    <input type="text" id="divnum1" name="a"> / <input type="text" id="divnum2" name="b"><br><br>
                    <input type="submit" value="Divide">
                </form><br><br><br>
            </body>
        </html>
    """

@app.route("/add")
def handle_add():
    num1 = int(request.args["a"])
    num2 = int(request.args["b"])
    answer = add(num1, num2)
    return f"""The answer is {answer}"""


@app.route("/sub")
def handle_sub():
    num1 = int(request.args["a"])
    num2 = int(request.args["b"])
    answer = sub(num1, num2)
    return f"""<h1>The answer is {answer}</h1>"""

@app.route("/mult")
def handle_mult():
    num1 = int(request.args["a"])
    num2 = int(request.args["b"])
    answer = mult(num1, num2)
    return f"""<h1>The answer is {answer}</h1>"""

@app.route("/div")
def handle_div():
    num1 = int(request.args["a"])
    num2 = int(request.args["b"])
    answer = div(num1, num2)
    return f"""<h1>The answer is {answer}</h1>"""

