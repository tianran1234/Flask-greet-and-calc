from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def do_add():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(add(a,b))

@app.route('/sub')
def do_sub():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(sub(a,b))

@app.route('/mult')
def do_mult():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(mult(a,b))

@app.route('/div')
def do_div():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(div(a,b))

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):

    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operators[oper](a, b)

    return str(result)