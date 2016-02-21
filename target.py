import requests
import simplejson as json 
import random 
from decimal import Decimal

transaction = False

productDict = { 'PS4 Console' : '50522463',
				'Nikon D3300 DX-format DSLR Bundle' : '21490248',
				'Pebble Time Steel Smartwatch' : '49124627',
				'GoPro Camera HERO' : '18760721',
			   	'Bose SoundLink Speaker' : '18854140',
			   	'TomTom Via GPS' : '21456407',
			   	'Panasonic Sensor Microwave' : '16510846',
			   	'LG 55 1080p HD TV' : '17221644',
			   	'Microsoft Surface Pro 4' : '50308839',
			   	'WD External Hard Drive' : '14881813',
				'Beats Solo 2 Wireless Headphones' : '16696652'}

productDictTwo = { '50522463' : 'PS4 Console',
				'21490248' : 'Nikon D3300 DX-format DSLR Bundle',
				'49124627' : 'Pebble Time Steel Smartwatch',
				'18760721' : 'GoPro Camera HERO',
			   	'18854140' : 'Bose SoundLink Speaker',
			   	'21456407' : 'TomTom Via GPS',
			   	'16510846' : 'Panasonic Sensor Microwave',
			   	'17221644' : 'LG 55 1080p HD TV',
			   	'50308839' : 'Microsoft Surface Pro 4',
			   	'14881813' : 'WD External Hard Drive',
				'16696652' : 'Beats Solo 2 Wireless Headphones'}

def get_prices(itemKey):
	value = requests.get('https://api.target.com/products/v3/' + str(itemKey) + '?id_type=tcin&store_id=634&fields=all_fields_group&key=J5PsS2XGuqCnkdQq0Let6RSfvU7oyPwF').content
	# print value.json()
	parsed = json.loads(value)
	print json.dumps(parsed, indent=4, sort_keys=True)
	prices = parsed['product_composite_response']['items'][0]['online_price']
	model_price(prices['list_price'])
	return prices

def get_product(itemKey):
	value = requests.get('https://api.target.com/products/v3/' + str(itemKey) + '?id_type=tcin&store_id=634&fields=all_fields_group&key=J5PsS2XGuqCnkdQq0Let6RSfvU7oyPwF').content
	# print value.json()
	result = json.loads(value)
	
	return result

def model_price(price):
	priceList = []
	TWOPLACES = Decimal(10) ** -2
	for i in range(10):
		priceList.append(float("{:.2f}".format(float(price)*random.uniform(0.95, 1.05))))
	return priceList

def get_list():
	return productDictTwo

def set_transaction_true():
	transaction = True 

