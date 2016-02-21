import requests
import simplejson as json 
import random 
from decimal import Decimal

productDict = {'ps4 console' : '50522463',
				'Nikon D3300 DX-format DSLR Bundle' : '21490248',
				'Pebble Time Steel Smartwatch' : '49124627',
				'Pebble Time Round Smartwatch' : '50845993',
				'GoPro Camera HERO' : '18760721',
				'Beats Solo 2 Wireless Headphones' : '16696652'}

def get_prices(itemKey):
	value = requests.get('https://api.target.com/products/v3/' + str(itemKey) + '?id_type=tcin&store_id=634&fields=all_fields_group&key=J5PsS2XGuqCnkdQq0Let6RSfvU7oyPwF').content
	# print value.json()
	parsed = json.loads(value)
	print json.dumps(parsed, indent=4, sort_keys=True)
	prices = parsed['product_composite_response']['items'][0]['online_price']
	print prices['list_price']
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
		priceList.append(float("{:.2f}".format(float(price)*random.uniform(0.6, 1.2))))

	print priceList

def get_list():
	return productDict



	
