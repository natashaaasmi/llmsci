import flask
from flask import Flask
from flask_restful import Api
from flask import request

from script import *

app = Flask(__name__)
api = Api(app)

@app.route('/',methods=['GET','POST'])
#use this function to get data from form 
def page_home():
    if request.method=='POST':
        test = request.args.get('input')
        #print(test)
    return flask.render_template('index.html',test)

@app.route('/result',methods=['GET','POST'])
def get_input():
    if request.method=='POST':
        test = request.args.get('input')
        print(test)
        #pass form input to script, get API response somewhere else

@app.route("/hello/", methods=["GET", "POST"])
def hello_world():
    return flask.render_template('index.html')

if __name__ == 'main':
    app.run(port=8000,debug=True)