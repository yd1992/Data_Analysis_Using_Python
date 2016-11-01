import json
import os
import sys
import argparse
import requests

keyword = "python;pandas"
catelog = "questions"

json_file_question = open("../midterm/" + keyword + "/" + catelog + "/Output.json", 'r')
file_question = json.load(json_file_question)

resDict = {}

for question in file_question:
	content = question.get("title")
	resDict[content] = question.get("view_count")

print("The number of most viewed questions Top 10: ")
total = 0
for item in sorted(resDict, key = resDict.get, reverse = True):
	if total > 9 :
		break
	print "Questions " + item
	print "Viewed Count " + str(resDict[item])
	print "\n"
	total = total + 1
