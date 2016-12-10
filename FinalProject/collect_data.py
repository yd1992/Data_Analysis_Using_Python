#!/usr/bin/python

import pandas as pd
from pandas import *
import glob
import sys
import os

myPath = os.path.split(os.path.realpath(sys.argv[0]))[0]

#Collect Data for Analysis1
datasets_Analysis_1 = read_csv(myPath + '/Datasets/vgsales.csv', sep=",", usecols = ["Name", "Platform", "Year", "Global_Sales"])
datasets_Analysis_1.to_csv(myPath + '/Datasets/Datasets_Analysis_1.csv', sep=',', index = False)

#Collect Data for Analysis2
datasets_Analysis_2 = read_csv(myPath + '/Datasets/vgsales.csv', sep=",", usecols = ["Genre", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"])
datasets_Analysis_2.to_csv(myPath + '/Datasets/Datasets_Analysis_2.csv', sep=',', index = False)

#Collect Data for Analysis3
datasets_Analysis_3 = read_csv(myPath + '/Datasets/vgsales.csv', sep=",", usecols = ["Year", "Publisher", "Global_Sales"])
datasets_Analysis_3.to_csv(myPath + '/Datasets/Datasets_Analysis_3.csv', sep=',', index = False)

#Collect Data for Analysis4
datasets_Analysis_3 = read_csv(myPath + '/Datasets/vgsales.csv', sep=",", usecols = ["Platform", "Genre", "Global_Sales"])
datasets_Analysis_3.to_csv(myPath + '/Datasets/Datasets_Analysis_4.csv', sep=',', index = False)

#Collect Data for Analysis5
datasets_Analysis_3 = read_csv(myPath + '/Datasets/vgsales.csv', sep=",", usecols = ["Year", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"])
datasets_Analysis_3.to_csv(myPath + '/Datasets/Datasets_Analysis_5.csv', sep=',', index = False)