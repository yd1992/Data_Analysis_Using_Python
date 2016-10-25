import json

def averagePopularity(term, date):
	r1 = []
	r2 = []

	f = open("../assignment2/" + term + "/" + date + "/output.json", "r")

	json_file = json.load(f)

	for record in json_file:
		count = record.get("favorite_count")
	
		if record.get("retweeted_status"):
			count = record.get("retweeted_status").get("favorite_count")
		
		r1.append(count)
		r2.append(record.get("retweet_count"))

	print("Team " + term + " popularity based on Tweet Likes on " + date + " : " + str(sum(r1)/float(len(r1))))
	print("Team " + term + " popularity based on Retweets on " + date + " : " + str(sum(r2)/float(len(r2))))


print(" 2016 League of Legends Semifinal 4 Teams popularity on Twitter Prediction:\n")
print("Based on average Retweets and Likes on 2016-10-22")

print("Team SKT")
averagePopularity("SKT", "2016-10-22")

print("Team ROX")
averagePopularity("ROX", "2016-10-22")

print("Team SSG")
averagePopularity("SSG", "2016-10-22")

print("Team H2K")
averagePopularity("H2K", "2016-10-22")
