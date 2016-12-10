#!/usr/bin/python

import argparse
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os
import csv

#Lookup Total Global Sales based on Publishers in different years
myPath = os.path.split(os.path.realpath(sys.argv[0]))[0]

myParser = argparse.ArgumentParser(description = 'Lookup Total Global Sales based on Platform in different years')
myParser.add_argument("publisher", help = "Choose one of the publishers")
args = myParser.parse_args()

df_publisher_sales = pd.read_csv(myPath + '/Datasets/Datasets_Analysis_3.csv', sep= ",", usecols = ["Year", "Publisher", "Global_Sales"])
df_publisher_sales = df_publisher_sales.sort_values(by = ['Publisher', 'Year'])

publisherArray = df_publisher_sales.Publisher.unique()
yearArray = df_publisher_sales.Year.unique()

publisher_year_dict = {}

for pb in publisherArray:
	publisher_year_dict[pb] = round((df_publisher_sales.loc[df_publisher_sales["Publisher"] == pb, 'Global_Sales'].sum())*1000000)

startYear = int(min(yearArray))
endYear = int(max(yearArray))

print "Top 3 Total Global Sales Start from " + str(startYear) + " to " + str(endYear) + " based on publishers"
for item in sorted(publisher_year_dict, key = publisher_year_dict.get, reverse = True)[:3]:
	print item, publisher_year_dict[item]


#User Interaction
print "Result: " + args.publisher, publisher_year_dict[args.publisher]

#Save to csv
csvfile = open(myPath + '/Result/Analysis3_User_Result.csv','w')
writer = csv.writer(csvfile)
title = ["Publisher", "Total_Global_Sales"]
writer.writerow(title)

data = [args.publisher, str(publisher_year_dict[args.publisher])]
writer.writerow(data)

csvfile = open(myPath + '/Result/Analysis3_Result.csv','w')
writer = csv.writer(csvfile)
title = ["Publisher", "Total_Global_Sales"]
writer.writerow(title)

for item in sorted(publisher_year_dict, key = publisher_year_dict.get, reverse = True):
	data = [item, str(publisher_year_dict[item])]
	writer.writerow(data)

#Visualization
explode = (0.1, 0)
colors = ['blue', 'green']
labels = [args.publisher, 'Other Publishers']

this_Sales = round((df_publisher_sales.loc[df_publisher_sales["Publisher"] == args.publisher, 'Global_Sales'].sum())*1000000)

sum_Sales = 0
for item in sorted(publisher_year_dict, key = publisher_year_dict.get, reverse = True):
	sum_Sales += publisher_year_dict[item]

sizes = [this_Sales, sum_Sales - this_Sales]

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Percentage of Global Sales of Publisher' + args.publisher)
plt.show()

