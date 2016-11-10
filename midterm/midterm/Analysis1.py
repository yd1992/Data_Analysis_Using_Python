import json
import os
import sys
import argparse
import requests
import csv

def checkAndCreateFolder(key):
	if not os.path.exists("../midterm/" + key):
		os.makedirs("../midterm/" + key)
	else:
		print("../midterm/" + key + "already exists")

parser = argparse.ArgumentParser(description = 'Analysis1')
args = parser.parse_args()
keyword = "python;pandas"
catelog = "userOfQuestions"
count = 499
resultDict = {}

checkAndCreateFolder(keyword + "/" + catelog)

json_file_user = open("../midterm/" + keyword + "/" + catelog + "/Output.json", 'w+')
json_file_user.write("[")

json_file_questions = open("../midterm/" + keyword + "/" + "questions" + "/Output.json", "r")
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

checkAndCreateFolder(keyword + "/" + "tags")
tagsInfo = requests.get("https://api.stackexchange.com/2.2/tags/python; pandas/info?site=stackoverflow&key=nAl2Y3B479z6yR0TmyjM0A((")
a = open("../midterm/" + keyword + "/" + "tags" + "/tagsOutput.json", 'w+')
t_count = 2
a.write("[")
for t in tagsInfo.json()['items']:
	t_count -= 1

	if t_count < 0:
		break

	if t_count == 0:
		a.write(json.dumps(t))
		continue

	a.write(json.dumps(t))
	a.write(",")
	a.write("\n")
	
a.write("]")

print("The number of badges weightage based on questions Top 10: ")
total = 0
for w in sorted(resultDict, key=resultDict.get, reverse=True):
	if total > 9 :
		break
	print "Questions " + w
	print "Badge Weightage " + str(resultDict[w])
	print "\n"
	total = total + 1

csvfile = open('../midterm/output/analysis1.csv','w')
writer = csv.writer(csvfile)
title = ["Questions", "Badge Weightage"]
writer.writerow(title)

total = 0
for item in sorted(resultDict, key = resultDict.get, reverse = True):
	if total > 9 :
		break

	data = [item, str(resultDict[item])]
	writer.writerow(data)
	total = total + 1







