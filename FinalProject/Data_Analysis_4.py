import argparse
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os
import csv

#Analyze Total Global Sales based on Platform and Genre
myPath = os.path.split(os.path.realpath(sys.argv[0]))[0]

myParser = argparse.ArgumentParser(description = 'Lookup Total Global Sales based on Platform in different years')
myParser.add_argument("platform", help = "Choose one of the platform")
myParser.add_argument("genre", help = "Choose one of the genre")
args = myParser.parse_args()

df = pd.read_csv(myPath + '/Datasets/Datasets_Analysis_4.csv', sep= ",", usecols = ["Platform", "Genre", "Global_Sales"])
pfArray = df.Platform
grArray = df.Genre
gsArray = df.Global_Sales

infoDict = {}
for i in range(len(pfArray)):
	if pfArray[i] in infoDict:
		infoDict[pfArray[i]].append(grArray[i] + ":" + str(gsArray[i]))
	else:
		infoDict[pfArray[i]] = [grArray[i] + ":" + str(gsArray[i])]

#User Interaction
sum = 0
for temp in infoDict[args.platform]:
	tempList = temp.split(":")
	if(tempList[0] == args.genre):
		sum += float(tempList[1])

print sum

#Save to csv
csvfile = open(myPath + '/Result/Analysis4_User_Result.csv','w')
writer = csv.writer(csvfile)
title = ["Platform", "Genre" ,"Total_Global_Sales"]
writer.writerow(title)

data = [args.platform, args.genre, str(sum)]
writer.writerow(data)

#Visualization
platGenre = pd.crosstab(df.Platform,df.Genre)
platGenre['Total'] = platGenre.sum(axis=1)
popPlatform = platGenre[platGenre['Total']>0].sort_values(by='Total', ascending = False)
neededdata = popPlatform.loc[:,:'Strategy']
maxi = neededdata.values.max()
mini = neededdata.values.min()
popPlatformfinal = popPlatform.append(pd.DataFrame(popPlatform.sum(), columns=['total']).T, ignore_index=False)
sns.set(font_scale=0.7)
plt.figure(figsize=(10,5))
sns.heatmap(popPlatformfinal, vmin = mini, vmax = maxi, annot=True, fmt="d")
plt.xticks(rotation = 90)
plt.show()




