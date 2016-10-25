import json

def getTweetsOfLikes(term, date):
	results = {}

	f = open("../assignment2/" + term + "/" + date + "/output.json", "r")

	json_file = json.load(f)

	for record in json_file:
		count = record.get("favorite_count")
	
		if record.get("retweeted_status"):
			count += record.get("retweeted_status").get("favorite_count")

		key = record.get("text")
		results[key] = count
	
	iterator = 0
	print("Top 5 Tweets Liked about " + term + " on " + date + " : \n")
	for word in sorted(results, key = results.get, reverse = True):
		iterator += 1

		if iterator > 5:
			break

		print("Ranked No." + str(iterator))
		print("Liked Amount: " + str(results[word]))
		print("Tweet Content: " + word)
		print("\n")

print("2016 League Of Legends Semifinal 4 Teams Top 5 Tweets: ")
print("Based on Likes Amount")

print("\n")
getTweetsOfLikes("SKT", "2016-10-20")
getTweetsOfLikes("SKT", "2016-10-21")
getTweetsOfLikes("SKT", "2016-10-22")

print("\n")
getTweetsOfLikes("ROX", "2016-10-20")
getTweetsOfLikes("ROX", "2016-10-21")
getTweetsOfLikes("ROX", "2016-10-22")

print("\n")
getTweetsOfLikes("SSG", "2016-10-21")
getTweetsOfLikes("SSG", "2016-10-22")
getTweetsOfLikes("SSG", "2016-10-23")

print("\n")
getTweetsOfLikes("H2K", "2016-10-21")
getTweetsOfLikes("H2K", "2016-10-22")
getTweetsOfLikes("H2K", "2016-10-23")