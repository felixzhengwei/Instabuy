import requests
import simplejson as json 

def get_product():
	value = requests.get('https://api.target.com/products/v3/17274456?id_type=tcin&fields=pricing,images&key=J5PsS2XGuqCnkdQq0Let6RSfvU7oyPwF').content
	# print value.json()
	parsed = json.loads(value)
	print json.dumps(parsed, indent=4, sort_keys=True)
	item_id = parsed['product_composite_response']['items'][0]['item_id']
	return item_id




	
