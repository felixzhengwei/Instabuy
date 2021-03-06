from flask import Flask, jsonify, request, render_template, redirect
import twilio.twiml
from target import *
from nessie import checkBalance
import requests
from visa_direct import transaction
import simplejson as json 
from send_message import text

app = Flask(__name__)
global globvar
global response
global finalPrice

@app.route('/')
def hello_world():
	# get_product(50522463)
	return render_template("index.html")

@app.route('/get_target_data')
def get_target_data():
	result = get_prices(globvar)
	print result['list_price']
	print model_price(result['list_price'])
	parse = get_product(globvar)
	parse['price_list'] = model_price(result['list_price'])
	parse['balance'] = checkBalance()
	return jsonify(parse), 200

@app.route("/get_message", methods=['GET', 'POST'])
def get_message():
	incoming_message = request.values.get('Body', None)
	print len(str(incoming_message))
	x = incoming_message.split(" ")[0].split("-")[0][:-1]
	print len(x)
 	print x
	if str(x).upper() == "BUY":
		print "its working"
		print finalPrice
		status = transaction(float(finalPrice))
		print status
		return "True"
	else:
		return "False"

@app.route('/profile', methods=['GET', 'POST'])
def profile():

    if request.method == 'POST':
        global globvar 
        globvar= request.json['key']
        print globvar
    return globvar

@app.route('/buy', methods=['GET', 'POST'])
def buy():
	if request.method == 'POST':
		print request.json['key']
        money = int(request.json['key'])
        print money
        status = transaction(money)
        if status == None:
        	global response
        	response = 'False'
        else: 
        	response = 'True'
        return response

@app.route('/message', methods=['GET', 'POST'])
def message():
	if request.method == 'POST':
		name = request.json['name']
        money = request.json['price']
        global finalPrice
        finalPrice = money
        print money
        text(name, money)
        return 'ok!'

@app.route('/get_response')
def get_response():
	newBalance = checkBalance()
	return response

@app.route('/get_product_list')
def get_product_list():
	productList = get_list()
	return jsonify(productList)

if __name__ == '__main__':
	app.run(debug=True)
