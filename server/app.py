#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Python Operations with Flask Routing and Views </h1>'

@app.route ('/print/<string:username>')
def print_string(param):
    print (f'profile for {param}')
    return f'<h1> profile for {param}<h1>'

@app.route('/count/<int:param>') 
def count(param):
    numbers = '\n'.join(str(i) for i in range(1, param + 1))
    return f'<h2>Counting from 1 to {param}:</h2><pre>{numbers}</pre>'

@app.route('/math/<num1><operation><num2>')
def math(num1, operation,num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return '<h2>Error: Division by zero is not allowed.</h2>'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return '<h2>Error: Invalid operation.</h2>'

    return f'<h2>Result of {num1} {operation} {num2}:</h2><p>{result}</p>'



if __name__ == '__main__':
    app.run(port=5555, debug=True)
