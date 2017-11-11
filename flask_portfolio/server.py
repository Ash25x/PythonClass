# from flask import Flask, render_template, request
from portfolio import app
# app  = Flask('portfolio')
#
# from . import views
if __name__ == '__main__':
    app.run(debug =True, host='localhost',port=5555)
