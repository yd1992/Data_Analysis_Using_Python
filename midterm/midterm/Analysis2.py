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

keyword = "python;pandas"
catelog = "userOfQuestions"

json_file_user = open("../midterm/" + keyword + "/" + catelog + "/Output.json", 'r')
file_user = json.load(json_file_user)

bronze_total = 0
silver_total = 0
gold_total = 0

for user in file_user:
	bronze_total += user.get("badge_counts").get("bronze")
	silver_total += user.get("badge_counts").get("silver")
	gold_total += user.get("badge_counts").get("gold")

print("Total Bronze " + str(bronze_total))
print("Total Silver " + str(silver_total))
print("Total Gold " + str(gold_total))

checkAndCreateFolder("output")
csvfile = open('../midterm/output/analysis2.csv', 'w')
writer = csv.writer(csvfile)
title = ["BadgeType", "Amount"]
writer.writerow(title)

data1 = ["Bronze", str(bronze_total)]
data2 = ["Silver", str(silver_total)]
data3 = ["Gold", str(gold_total)]

writer.writerow(data1)
writer.writerow(data2)
writer.writerow(data3)



