import json
import os
import sys
import argparse
import requests

def checkAndCreateFolder(key):
	if not os.path.exists("../assignment3/" + key):
		os.makedirs("../assignment3/" + key)
	else:
		print("../assignment3/" + key + "already exists")

parser = argparse.ArgumentParser(description = 'Analysis1')
args = parser.parse_args()
keyword = "python;pandas"
catelog = "userOfQuestions"
count = 500
resultDict = {}

checkAndCreateFolder(keyword + "/" + catelog)

json_file_user = open("../assignment3/" + keyword + "/" + catelog + "/Output.json", 'w+')
json_file_user.write("[")

json_file_questions = open("../assignment3/" + keyword + "/" + "questions" + "/Output.json", "r")
file_questions = json.load(json_file_questions)

for item in file_questions:
	userTitle = item.get("title")
	userId = item.get("owner").get("user_id")

	user = requests.get("https://api.stackexchange.com/2.2/users/" + str(userId) + "?site=stackoverflow&key=nAl2Y3B479z6yR0TmyjM0A((")
	for u in user.json()["items"]:
		badgeCount = u.get("badge_counts").get("bronze")*1 + u.get("badge_counts").get("silver")*5 + u.get("badge_counts").get("gold")*10

	resultDict[userTitle] = badgeCount

	for u in user.json()["items"]:
		count -= 1
		if count < 0:
		    break
		if count == 0:
		    json_file_user.write(json.dumps(u))
		    continue
		json_file_user.write(json.dumps(u))
		json_file_user.write(",") 
		json_file_user.write("\n")

json_file_user.write("]")

print("The number of badges weightage based on questions Top 10: ")
total = 0
for w in sorted(resultDict, key=resultDict.get, reverse=True):
	if total > 9 :
		break
	print "Questions " + w
	print "Badge Weightage " + str(resultDict[w])
	print "\n"
	total = total + 1









