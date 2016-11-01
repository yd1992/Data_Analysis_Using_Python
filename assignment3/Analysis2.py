import json
import os
import sys
import argparse
import requests

keyword = "python;pandas"
catelog = "userOfQuestions"

json_file_user = open("../assignment3/" + keyword + "/" + catelog + "/Output.json", 'r')
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

