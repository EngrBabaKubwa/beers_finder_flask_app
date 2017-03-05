from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(address):

	auth = Oauth1Authenticator(
	consumer_key=os.environ['CONSUMER_KEY'],
	consumer_secret=os.environ['CONSUMER_SECRET'],
	token=os.environ['TOKEN'],
	token_secret=os.environ['TOKEN_SECRET']
	)

	client = Client(auth)
	
	params = {
	'term': "beer",
	'lang': 'en',
	'limit': 3
	}

	response = client.search(address, **params)

	businesses = []

	for business in response.businesses:
		# print(business.name, business.rating, business.phone)
		businesses.append({"name": business.name, 
			"rating": business.rating
			})

	return businesses

# businesses = get_businesses("Boulder")

# print(businesses)


