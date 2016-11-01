import json
import os
import sys
import argparse
import requests

keyword = "python;pandas"
catelog = "userOfQuestions"

json_file_user = open("../assignment3/" + keyword + "/" + catelog + "/Output.json", 'r')
file_user = json.load(json_file_user)

resDict = {}
for user in file_user:
	userName = user.get("display_name")
	reputation = user.get("reputation")
	resDict[userName] = reputation

print("Top 10 Users of Reputation: ")
total = 0
for item in sorted(resDict, key = resDict.get, reverse = True):
	if total > 9 :
		break
	print "User Name " + item
	print "Reputation " + str(resDict[item])
	print "\n"
	total = total + 1


