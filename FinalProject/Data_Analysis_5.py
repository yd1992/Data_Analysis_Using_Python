import argparse
import pandas as pd
from matplotlib import pyplot as plt
import pylab as pl
import seaborn as sns
import numpy as np
import sys
import os
import csv
import collections

#Analyze Total Global Sales based on Platform and Genre
myPath = os.path.split(os.path.realpath(sys.argv[0]))[0]

myParser = argparse.ArgumentParser(description = 'Lookup Total Global Sales based on Platform in different years')
myParser.add_argument("district", help = "Choose one of the district")
args = myParser.parse_args()

year_dist_df = pd.read_csv(myPath + '/Datasets/Datasets_Analysis_5.csv', sep= ",", usecols = ["Year", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"])

yearArray = year_dist_df.Year.unique()

naDict = {}
euDict = {}
jpDict = {}
othDict = {}
for y in sorted(yearArray):
	naDict[y] = round((year_dist_df.loc[year_dist_df["Year"] == y, 'NA_Sales'].sum())*1000000)
	euDict[y] = round((year_dist_df.loc[year_dist_df["Year"] == y, 'EU_Sales'].sum())*100000)
	jpDict[y] = round((year_dist_df.loc[year_dist_df["Year"] == y, 'JP_Sales'].sum())*1000000)
	othDict[y] = round((year_dist_df.loc[year_dist_df["Year"] == y, 'Other_Sales'].sum())*100000)

# Save to csv
csvfile = open(myPath + '/Result/Analysis5_Result.csv','w')
writer = csv.writer(csvfile)
title = ["Year", "District", "Total_District_Sales"]
writer.writerow(title)

odnaDict = collections.OrderedDict(sorted(naDict.items()))
for item in odnaDict:
	data = [str(item), "NA", str(odnaDict[item])]
	writer.writerow(data)

odeuDict = collections.OrderedDict(sorted(euDict.items()))
for item in odeuDict:
	data = [str(item), "EU", str(odeuDict[item])]
	writer.writerow(data)

odjpDict = collections.OrderedDict(sorted(jpDict.items()))
for item in odjpDict:
	data = [str(item), "JP", str(odjpDict[item])]
	writer.writerow(data)

odothDict = collections.OrderedDict(sorted(othDict.items()))
for item in odothDict:
	data = [str(item), "Other", str(odothDict[item])]
	writer.writerow(data)

csvfile = open(myPath + '/Result/Analysis5_User_Result.csv','w')
writer = csv.writer(csvfile)
title = ["District", "Year", "Total_District_Sales"]
writer.writerow(title)

if args.district == "NA": 
	for item in odnaDict:
		data = ["NA", item, str(odnaDict[item])]
		writer.writerow(data)

elif args.district == "EU": 
	for item in odeuDict:
		data = ["EU", item, str(odeuDict[item])]
		writer.writerow(data)

elif args.district == "JP": 
	for item in odjpDict:
		data = ["JP", item, str(odjpDict[item])]
		writer.writerow(data)

elif args.district == "Other": 
	for item in odothDict:
		data = ["Other", item, str(odothDict[item])]
		writer.writerow(data)

#Visualization
naX = list(naDict.keys())
naY = list(naDict.values())

euX = list(euDict.keys())
euY = list(euDict.values())

jpX = list(jpDict.keys())
jpY = list(jpDict.values())

othX = list(othDict.keys())
othY = list(othDict.values())
 
pl.plot(naX, naY, "g")
pl.plot(euX, euY, "r")
pl.plot(jpX, jpY, "b")
pl.plot(othX, othY, "y")

pl.xlim(min(yearArray), max(yearArray))
 
pl.title("Four Districts Total Sales in different years")
pl.xlabel("Year")
pl.ylabel("Total Sales")
 
pl.show()
