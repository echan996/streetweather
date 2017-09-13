import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('helloworld.html')

@app.route("/docs")
def docs():
	return render_template('docs.html')