import json

def countLikes(term, date):
	r = []

	f = open("../assignment2/" + term + "/" + date + "/output.json", "r")

	json_file = json.load(f)

	for record in json_file:
		count = record.get("favorite_count")
	
		if record.get("retweeted_status"):
			count = record.get("retweeted_status").get("favorite_count")
	
		r.append(count)

	print("Team " + term + " popularity based on Tweet Likes on " + date + " : " + str(sum(r)))


print(" 2016 League of Legends Semifinal 4 Teams popularity on Twitter Prediction:\n")
print("Based on Likes")

print("Team SKT vs Team ROX:")
print("Date Range: 2016-10-20 to 2016-10-22")
countLikes("SKT", "2016-10-20")
countLikes("SKT", "2016-10-21")
countLikes("SKT", "2016-10-22")
countLikes("ROX", "2016-10-20")
countLikes("ROX", "2016-10-21")
countLikes("ROX", "2016-10-22")

print("\n")

print("Team SSG vs Team H2K:")
print("Date Range: 2016-10-21 to 2016-10-23")
countLikes("SSG", "2016-10-21")
countLikes("SSG", "2016-10-22")
countLikes("SSG", "2016-10-23")
countLikes("H2K", "2016-10-21")
countLikes("H2K", "2016-10-22")
countLikes("H2K", "2016-10-23")

