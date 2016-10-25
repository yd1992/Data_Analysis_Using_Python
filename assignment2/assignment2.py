import json
import oauth2 as oauth
import argparse
import os
import time
from datetime import date
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

parser = argparse.ArgumentParser(description = "Twitter Search")
parser.add_argument("term", help = "search key word")
parser.add_argument("start", help = "start date")
parser.add_argument("end", help = "end date")
args = parser.parse_args()

def checkAndCreateFolder(key):

	if not os.path.exists("../assignment2" + key):
		os.makedirs("../assignment2" + key)
	else:
		print("../asignment2" + key + "already exists")


def searchTwitterAPI():

	consumer_key = 'fKv612bdWbadlTrSw6yDuOOzb'
	consumer_secret = 'eZDDVCZ7YoEgzCRRIrLjg9SRHz73XW9LzkVTKdMPBDboVhwiHj'
	access_token = '790329852343754752-0xz9DzKwMnLxJBmTOKUAsKfx4tcj8tf'
	access_secret = 'QziJXPEGD6tSDON6J23pCrIrsQlWB9DQsMLWM2n1c92gP'

	oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)
	twitter = Twitter(auth=oauth)
	twitter_stream = TwitterStream(auth=oauth)

	result = twitter.search.tweets(q = args.term, since = args.start, until = args.end, count = 100)
    
	termPath = "/" + args.term
	checkAndCreateFolder(termPath)

	datePath = termPath + "/" + args.start
	checkAndCreateFolder(datePath)

	f = open("../assignment2" + datePath + "/output.json", 'w+')
	f.write("[")


	count = 100
	for tweet in result["statuses"]:
		count -= 1

		if count < 0:
			break
		if count == 0:
			f.write(json.dumps(tweet))
			continue

		f.write(json.dumps(tweet))
		f.write(",")
		f.write("\n")

	f.write("]")


searchTwitterAPI()
 
