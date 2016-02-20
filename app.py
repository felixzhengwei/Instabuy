from flask import Flask, jsonify, render_template
from target import get_product
import requests
import simplejson as json 

app = Flask(__name__)

@app.route('/')
def hello_world():
	get_product()
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
