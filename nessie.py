# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

customerId = '56c8c5f4061b2d440baf438d'
ID = '56c8c8f9061b2d440baf4396'
AccountNumber = '1111111111111111'
apiKey = '91a06c499d1e8a39ba720e08ef0e4732'
merchantId = '56c8dc33061b2d440baf43c2'

def checkBalance():
    url = "http://api.reimaginebanking.com/customers/{}/accounts?key={}".format(customerId,apiKey)
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        balance = json_data[0]['balance']
        print balance
        return balance
    else:
        print (response.status_code)
        return None


def purchase():
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key={}".format(ID,apiKey)

balance = checkBalance()


# payload = {
#   "type": "Chequing",
#   "nickname": "test",
#   "rewards": 10000,
#   "balance": 10000,
# }
#
# # payload = {
# #   "medium": "balance",
# #   "amount": 10000,
# #   "description": "Starting Balance"
# # }
#
# # Create a Savings Account
# response = requests.post(
# 	url,
# 	data=json.dumps(payload),
# 	headers={'content-type':'application/json'},
# 	)
#
# if response.status_code == 201:
# 	print('account created')
# else:
#     print (response.status_code)
