from flask import Flask, jsonify, request, render_template
from target import get_product, model_price, get_prices, get_list
import requests
import simplejson as json 

app = Flask(__name__)

@app.route('/')
def hello_world():
	get_product(50522463)
	return render_template("index.html")

@app.route('/get_target_data')
def get_target_data():
	result = get_prices(50522463)
	result['price_list'] = model_price(result['list_price'])
	parse = get_product(50522463)
	return jsonify(parse), 200

@app.route('/profile', methods=['GET', 'POST'])
def profile():

    if request.method == 'POST':
        print request.json

    return 'ok!'

@app.route('/get_product_list')
def get_product_list():
	productList = get_list()
	return jsonify(productList)

if __name__ == '__main__':
	app.run(debug=True)
