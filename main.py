import pandas
import pandas as pd
from prettytable import PrettyTable

dataSet = pd.read_csv('Data set/INOUT.csv')
title = ["name", "type","min", "max", "mean", "median"]

table = PrettyTable()
maxList = []
minList = []
typeList = []
meanList = []
nameList = []
medianList = []
modeList = []

for attribute in dataSet.columns:
    if dataSet[attribute].dtype == 'object':
        continue
    nameList.append(attribute)
    typeList.append(dataSet[attribute].dtype)
    minList.append(dataSet[attribute].min())
    maxList.append(dataSet[attribute].max())
    meanList.append(dataSet[attribute].mean())
    medianList.append(dataSet[attribute].median())


table.add_column(title[0], nameList)
table.add_column(title[1], typeList)
table.add_column(title[2], minList)
table.add_column(title[3], maxList)
table.add_column(title[4], meanList)
table.add_column(title[5], medianList)

print(table)
