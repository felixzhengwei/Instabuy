from flask import Flask, jsonify, request, render_template, redirect
import twilio.twiml
from target import *
import requests
import simplejson as json 

app = Flask(__name__)

@app.route('/')
def hello_world():
	get_product(50522463)
	return render_template("index.html")

@app.route('/get_target_data')
def get_target_data():
	result = get_product(50522463)
	result['price_list'] = model_price(result['list_price'])
	return jsonify(result), 200

@app.route("/get_message", methods=['GET', 'POST'])
def get_message():
    incoming_message = request.values.get('Body', None)
    print len(str(incoming_message))
    x =  incoming_message.split(" ")[0].split("-")[0][:-1]
    print len(x)
    print x
    if str(x) == "BUY":
    	print "its working"
    	return set_transaction_true()
    else:
    	return None

@app.route('/profile', methods=['GET', 'POST'])
def profile():

    if request.method == 'POST':
        print request.json

    return 'ok!'

if __name__ == '__main__':
	app.run(debug=True)
