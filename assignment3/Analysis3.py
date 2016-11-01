import json
import os
import sys
import argparse
import requests

keyword = "python;pandas"
catelog = "questions"

json_file_question = open("../assignment3/" + keyword + "/" + catelog + "/Output.json", 'r')
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


