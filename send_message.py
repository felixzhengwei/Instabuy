from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC901af1456b25b143158591660fd76ba1" 
AUTH_TOKEN = "3ac698ce30ee440f792e7e76ee9e015b" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 


def text(name, price):
	client.messages.create(
		to="+12489233097",
		from_="+19706423851",
		body="The " + str(name) + "is affordable, and is currently at a price of " + str(price) + ". Text BUY to purchase the item." ,
	)