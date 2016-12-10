# !/usr/bin/python

import argparse
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os
import csv

#Analyze people' s favorite genre of video games based on districts
myPath = os.path.split(os.path.realpath(sys.argv[0]))[0]

myParser = argparse.ArgumentParser(description = 'Top3 genres of video games people likes most, based on different districts')
myParser.add_argument("district", help = "Choose one of districts")
args = myParser.parse_args()

df_Sales = pd.read_csv(myPath + '/Datasets/Datasets_Analysis_2.csv', sep= ",", usecols = ["Genre", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"])
genreArray = df_Sales.Genre.unique()

genre_NA_Dic = {}
for g in genreArray:
	genre_NA_Dic[g] = round((df_Sales.loc[df_Sales["Genre"] == g, 'NA_Sales'].sum())*1000000)

genre_EU_Dic = {}
for g in genreArray:
	genre_EU_Dic[g] = round((df_Sales.loc[df_Sales["Genre"] == g, 'EU_Sales'].sum())*1000000)

genre_JP_Dic = {}
for g in genreArray:
	genre_JP_Dic[g] = round((df_Sales.loc[df_Sales["Genre"] == g, 'JP_Sales'].sum())*1000000)

genre_Other_Dic = {}
for g in genreArray:
	genre_Other_Dic[g] = round((df_Sales.loc[df_Sales["Genre"] == g, 'Other_Sales'].sum())*1000000)

#User Interaction
print "Result: "
print "The District: " + args.district
if(args.district == "NA"):
	for item in sorted(genre_NA_Dic, key = genre_NA_Dic.get, reverse = True)[:3]:
		print item, genre_NA_Dic[item]
elif(args.district == "EU"):
	for item in sorted(genre_EU_Dic, key = genre_EU_Dic.get, reverse = True)[:3]:
		print item, genre_EU_Dic[item]
elif(args.district == "JP"):
	for item in sorted(genre_JP_Dic, key = genre_JP_Dic.get, reverse = True)[:3]:
		print item, genre_JP_Dic[item]
else:
	for item in sorted(genre_JP_Dic, key = genre_Other_Dic.get, reverse = True)[:3]:
		print item, genre_Other_Dic[item]

# Save to csv
csvfile = open(myPath + '/Result/Analysis2_Result.csv','w')
writer = csv.writer(csvfile)
title = ["District", "Genre", "Total_District_Sales"]
writer.writerow(title)

for item in sorted(genre_NA_Dic, key = genre_NA_Dic.get, reverse = True):
	data = ["NA", item, str(genre_NA_Dic[item])]
	writer.writerow(data)

for item in sorted(genre_EU_Dic, key = genre_EU_Dic.get, reverse = True):
	data = ["EU", item, str(genre_EU_Dic[item])]
	writer.writerow(data)

for item in sorted(genre_JP_Dic, key = genre_JP_Dic.get, reverse = True):
	data = ["JP", item, str(genre_JP_Dic[item])]
	writer.writerow(data)

for item in sorted(genre_Other_Dic, key = genre_Other_Dic.get, reverse = True):
	data = ["Other", item, str(genre_Other_Dic[item])]
	writer.writerow(data)


csvfile = open(myPath + '/Result/Analysis2_User_Result.csv','w')
writer = csv.writer(csvfile)
title = ["District", "Genre", "Total_District_Sales"]
writer.writerow(title)

if(args.district == "NA"):
	for item in sorted(genre_NA_Dic, key = genre_NA_Dic.get, reverse = True)[:3]:
		data = ["NA", item, str(genre_NA_Dic[item])]
		writer.writerow(data)

elif(args.district == "EU"):
	for item in sorted(genre_EU_Dic, key = genre_EU_Dic.get, reverse = True)[:3]:
		data = ["EU", item, str(genre_EU_Dic[item])]
		writer.writerow(data)

elif(args.district == "JP"):
	for item in sorted(genre_JP_Dic, key = genre_JP_Dic.get, reverse = True)[:3]:
		data = ["JP", item, str(genre_JP_Dic[item])]
		writer.writerow(data)

else:
	for item in sorted(genre_Other_Dic, key = genre_Other_Dic.get, reverse = True)[:3]:
		data = ["Other", item, str(genre_Other_Dic[item])]
		writer.writerow(data)


#Visulization
GenreGroup = df_Sales.groupby(['Genre']).sum().loc[:, 'NA_Sales':'Global_Sales']
GenreGroup['NA_Sales%'] = GenreGroup['NA_Sales']/GenreGroup['Global_Sales']
GenreGroup['EU_Sales%'] = GenreGroup['EU_Sales']/GenreGroup['Global_Sales']
GenreGroup['JP_Sales%'] = GenreGroup['JP_Sales']/GenreGroup['Global_Sales']
GenreGroup['Other_Sales%'] = GenreGroup['Other_Sales']/GenreGroup['Global_Sales']
plt.figure(figsize=(8, 10))
sns.set(font_scale=0.7)
plt.subplot(211)
sns.heatmap(GenreGroup.loc[:, 'NA_Sales':'Other_Sales'], annot=True, fmt = '.1f')
plt.title("Comparison based on Districts and Genres of Video Games")
plt.subplot(212)
sns.heatmap(GenreGroup.loc[:,'NA_Sales%':'Other_Sales%'], vmax =1, vmin=0, annot=True, fmt = '.2%')
plt.title("Comparison based on Districts and Genres of Video Games (Percentage)")
plt.show()








