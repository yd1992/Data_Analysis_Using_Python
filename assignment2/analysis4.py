import json

def getTweetsOfRetweets(term, date):
	results = {}

	f = open("../assignment2/" + term + "/" + date + "/output.json", "r")

	json_file = json.load(f)

	for record in json_file:
		count = record.get("retweet_count")

		key = record.get("text")
		results[key] = count
	
	iterator = 0
	print("Top 5 Tweets Retweeted about " + term + " on " + date + " : \n")
	for word in sorted(results, key = results.get, reverse = True):
		iterator += 1

		if iterator > 5:
			break

		print("Ranked No." + str(iterator))
		print("Retweets Amount: " + str(results[word]))
		print("Tweet Content: " + word)
		print("\n")

print("2016 League Of Legends Semifinal 4 Teams Top 5 Tweets: ")
print("Based on Retweets Amount")

print("\n")
getTweetsOfRetweets("SKT", "2016-10-20")
getTweetsOfRetweets("SKT", "2016-10-21")
getTweetsOfRetweets("SKT", "2016-10-22")

print("\n")
getTweetsOfRetweets("ROX", "2016-10-20")
getTweetsOfRetweets("ROX", "2016-10-21")
getTweetsOfRetweets("ROX", "2016-10-22")

print("\n")
getTweetsOfRetweets("SSG", "2016-10-21")
getTweetsOfRetweets("SSG", "2016-10-22")
getTweetsOfRetweets("SSG", "2016-10-23")

print("\n")
getTweetsOfRetweets("H2K", "2016-10-21")
getTweetsOfRetweets("H2K", "2016-10-22")
getTweetsOfRetweets("H2K", "2016-10-23")