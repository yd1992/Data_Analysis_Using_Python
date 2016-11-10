import json
import os
import sys
import argparse
import requests
import csv

keyword = "python;pandas"
catelog = "questions"

json_file_question = open("../midterm/" + keyword + "/" + catelog + "/Output.json", 'r')
file_question = json.load(json_file_question)

resDict = {}

for question in file_question:
	content = question.get("title")
	if(question.get("is_answered") == "false"):
		resDict[content] = 0
	else:
		resDict[content] = question.get("answer_count")

print("The number of most answered questions Top 10: ")
total = 0
for item in sorted(resDict, key = resDict.get, reverse = True):
	if total > 9 :
		break
	print "Questions " + item
	print "Answer Count " + str(resDict[item])
	print "\n"
	total = total + 1

csvfile = open('../midterm/output/analysis3.csv','w')
writer = csv.writer(csvfile)
title = ["Questions", "Answer Count"]
writer.writerow(title)

total = 0
for item in sorted(resDict, key = resDict.get, reverse = True):
	if total > 9 :
		break

	data = [item, str(resDict[item])]
	writer.writerow(data)
	total = total + 1

