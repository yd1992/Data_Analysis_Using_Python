import json
import os
import sys
import argparse
from stackapi import StackAPI

parser = argparse.ArgumentParser(description = "Search StackOverFlow")
args = parser.parse_args()

def checkAndCreateFolder(key):

	if not os.path.exists("../midterm/" + key):
		os.makedirs("../midterm/" + key)
	else:
		print("../midterm/" + key + "already exists")

def collectData(inputKeyword, inputCatelog):
	website = "stackoverflow"
	API_Key = "nAl2Y3B479z6yR0TmyjM0A(("
	keyword = inputKeyword
	catelog = inputCatelog
	kAndc = keyword + "/" + catelog
	directory = "../midterm/" + kAndc
	count = 500

	visitWebsite = StackAPI(website)
	questions = visitWebsite.fetch(catelog, tagged = keyword)

	checkAndCreateFolder(keyword)
	checkAndCreateFolder(kAndc)

	f = open(directory + "/Output.json", 'w+')
	f.write("[")
	for t in questions['items']:
	    count -= 1

	    if count < 0:
	    	break

	    if count == 0:
	    	f.write(json.dumps(t))
	    	continue

	    f.write(json.dumps(t))
	    f.write(",") 
	    f.write("\n")
	    
	f.write("]")

collectData("python;pandas", "questions")