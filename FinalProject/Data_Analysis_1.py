#!/usr/bin/python

import argparse
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os
import csv

#Analyze total Global Sales based on different Platforms
myPath = os.path.split(os.path.realpath(sys.argv[0]))[0]

myParser = argparse.ArgumentParser(description = 'Lookup Total Global Sales based on Platform')
myParser.add_argument("platform", help = "Choose one of the platforms")
args = myParser.parse_args()

infos = pd.read_csv(myPath + '/Datasets/Datasets_Analysis_1.csv', sep= ",", usecols = ["Platform", "Year", "Global_Sales"])
infoArray = infos.Platform.unique()
yearArray = infos.Year.unique()

globalSalesSumDic = {}
for pf in infoArray:
	globalSalesSumDic[pf] = round((infos.loc[infos["Platform"] == pf, 'Global_Sales'].sum())*1000000)

startYear = int(min(yearArray))
endYear = int(max(yearArray))

print "Top 3 Total Global Sales Start from " + str(startYear) + " to " + str(endYear) + " based on Platforms"
for item in sorted(globalSalesSumDic, key = globalSalesSumDic.get, reverse = True)[:3]:
	print item, globalSalesSumDic[item]

#User Interaction
print "Result: " + args.platform, globalSalesSumDic[args.platform]

#Save to csv
csvfile = open(myPath + '/Result/Analysis1_Result.csv','w')
writer = csv.writer(csvfile)
title = ["Platform", "Total Global Sales"]
writer.writerow(title)

for item in sorted(globalSalesSumDic, key = globalSalesSumDic.get, reverse = True):
	data = [item, str(globalSalesSumDic[item])]
	writer.writerow(data)


csvfile = open(myPath + '/Result/Analysis1_User_Result.csv','w')
writer = csv.writer(csvfile)
title = ["Platform", "Total_Global_Sales"]
writer.writerow(title)

data = [args.platform, str(globalSalesSumDic[args.platform])]
writer.writerow(data)


#Visualization
platGenre = pd.crosstab(infos.Platform, infos.Year)
platGenreTotal = platGenre.sum(axis=1).sort_values(ascending = False)
plt.figure(figsize=(8,6))
sns.barplot(y = platGenreTotal.index, x = platGenreTotal.values, orient='h')
plt.ylabel = "Platforms"
plt.xlabel = "Total Sales of Video Game"
plt.show()
