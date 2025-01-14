#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  
    return f'{parameter}' 

@app.route('/count/<int:parameter>')
def count_int(parameter):
    numbers = [str(i) for i in range(parameter)]  
    numbers_list = "\n".join(numbers) +  "\n"
    return numbers_list

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math_operation(num1, operation, num2):
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation == 'div':
        return f'{num1 / num2}'
    elif operation == '%':
        return f'{num1 % num2}'
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
