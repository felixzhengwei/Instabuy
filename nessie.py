# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json
# import datetime

customerId = '56c8c5f4061b2d440baf438d'
# Credit_ID = '56c8c8f9061b2d440baf4396'
# Credit_AccountNumber = '1111111111111111'
apiKey = '91a06c499d1e8a39ba720e08ef0e4732'
# merchantId = '56c8dc33061b2d440baf43c2'
Checking_ID = '56c90124061b2d440baf440e'
Checking_AccountNumber = '1111111111111112'

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

def purchase(amt,dt):
    url = "http://api.reimaginebanking.com/accounts/{}/purchases?key={}".format(Credit_ID,apiKey)
    vals = {
        "merchant_id": merchantId,
        "medium": "balance",
        "purchase_date": dt, #YYYY-MM-DD
        "amount": amt,
        "status": "completed",
        "description": "purchase"
    }
    response = requests.post(url,data=json.dumps(vals),headers={'content-type':'application/json'})
    if response.status_code == 201:
        return True
    else:
        print (response.status_code)
        print (response.text)
        return False

def withdrawal(amt,dt):
    url = "http://api.reimaginebanking.com/accounts/{}/withdrawals?key={}".format(Checking_ID,apiKey)
    vals = {
      "medium": "balance",
      "transaction_date": dt,
      "status": "completed",
      "amount": amt,
      "description": "string"
    }
    response = requests.post(url,data=json.dumps(vals),headers={'content-type':'application/json'})
    if response.status_code == 201:
        return True
    else:
        print (response.status_code)
        print (response.text)
        return False

def deposits(amt,dt):
    url = "http://api.reimaginebanking.com/accounts/{}/deposits?key={}".format(Checking_ID,apiKey)
    vals = {
      "medium": "balance",
      "transaction_date": dt,
      "status": "completed",
      "amount": amt,
      "description": "string"
    }
    response = requests.post(url,data=json.dumps(vals),headers={'content-type':'application/json'})
    if response.status_code == 201:
        return True
    else:
        print (response.status_code)
        print (response.text)
        return False

# balance = checkBalance()
# deposits(9999800199,"2016-02-20")
# while balance != 9999800199:
#     print datetime.datetime.now()
#     balance = checkBalance()

