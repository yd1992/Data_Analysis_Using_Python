import json

def countRetweets(teamName, date): 
	results = []
	f = open("../assignment2/" + teamName + "/" + date + "/output.json", "r")
	json_file = json.load(f)

	for record in json_file:
		results.append(record.get("retweet_count"))

	print("Team " + teamName + " popularity based on Retweets on " + date + " : " + str(sum(results)))


print(" 2016 League of Legends Semifinal 4 Teams popularity on Twitter Prediction:\n")
print("Based on Retweets")

print("Team SKT vs Team ROX:")
print("Date Range: 2016-10-20 to 2016-10-22")
countRetweets("SKT", "2016-10-20")
countRetweets("SKT", "2016-10-21")
countRetweets("SKT", "2016-10-22")

countRetweets("ROX", "2016-10-20")
countRetweets("ROX", "2016-10-21")
countRetweets("ROX", "2016-10-22")


print("\n")

print("Team SSG vs Team H2K:")
print("Date Range: 2016-10-21 to 2016-10-23")
countRetweets("SSG", "2016-10-21")
countRetweets("SSG", "2016-10-22")
countRetweets("SSG", "2016-10-23")

countRetweets("H2K", "2016-10-21")
countRetweets("H2K", "2016-10-22")
countRetweets("H2K", "2016-10-23")