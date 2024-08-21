#!/usr/bin/env python3

from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:msg>")
def print_string(msg):
    print(msg)
    return msg

@app.route("/count/<int:num>")
def count(num):
    return "\n".join([str(i) for i in range(num)])

@app.route("/math/<int:num1>/<string:op>/<int:num2>")
def math(num1, op, num2):
    
    answer = eval(f'{num1}{op}{num2}') if op not in ["div", "%"] \
        else eval(f'{num1}/{num2}') if op == 'div' else eval(f'{num1}%{num2}')
    return str(answer)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
