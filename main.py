import pandas as pd
from prettytable import PrettyTable
import seaborn as sns
import matplotlib.pyplot as plt



dataSet1 = pd.read_csv('DataSets/INOUT.csv')
dataSet2 = pd.read_csv('DataSets/INOUTLINE.csv')
dataSet3 = pd.read_csv('DataSets/TRANSFER_ITEM_D.csv')
dataSet4 = pd.read_csv('DataSets/TRANSFER_ITEM.csv')
dataSet5 = pd.read_csv('DataSets/PRODUCTS.csv')
dataSet6 = pd.read_csv('DataSets/PRODUCTINSTANCE.csv', encoding='cp1252')


dataSets = [dataSet1, dataSet2, dataSet3, dataSet4, dataSet5, dataSet6]
title = ["name", "type", "min", "max", "mean", "median", "Q1(25%)", "Q3(75%)", "IQR", "Q1-(1.5*IQR)", "Q3+(1.5*IQR)"]


table = PrettyTable()
maxList = []
minList = []
typeList = []
meanList = []
nameList = []
medianList = []
modeList = []
q1 = []
q3 = []
iqr = []
q1MinusIQR = []
q3PlusIQR = []

# calculates statistical values, for each attribute in each dataSet
for dataSet in dataSets:
    for attribute in dataSet.columns:
        # jumb over objective attributes
        if dataSet[attribute].dtype == 'object':
            continue
        
        # draws box_plots
        sns.boxplot(y=dataSet[attribute])
        plt.show()

        # generates and stores values for each attribute
        nameList.append(attribute)
        typeList.append(dataSet[attribute].dtype)
        minList.append(dataSet[attribute].min())
        maxList.append(dataSet[attribute].max())
        meanList.append(dataSet[attribute].mean())
        medianList.append(dataSet[attribute].median())
        q1.append(dataSet[attribute].describe()[4])
        q3.append(dataSet[attribute].describe()[6])
        iqr.append(dataSet[attribute].describe()[6] - dataSet[attribute].describe()[4])

    # calculates bounds for outliers
    for d in range(len(iqr)):
        min = q1[d] - (1.5*iqr[d])
        if min < minList[d] :
            min = minList[d]

        q1MinusIQR.append(min)

        max = q3[d] + (1.5*iqr[d])
        if max > maxList[d]:
            max = maxList[d]
            
        q3PlusIQR.append(max)

    # prints the table
    table.add_column(title[0], nameList)
    table.add_column(title[1], typeList)
    table.add_column(title[2], minList)
    table.add_column(title[3], maxList)
    table.add_column(title[4], meanList)
    table.add_column(title[5], medianList)
    table.add_column(title[6],q1)
    table.add_column(title[7],q3)
    table.add_column(title[8],iqr)
    table.add_column(title[9],q1MinusIQR)
    table.add_column(title[10],q3PlusIQR)

    print(table)
    
    # clears lists 
    maxList.clear()
    minList.clear()
    typeList.clear()
    meanList.clear()
    nameList.clear()
    medianList.clear()
    modeList.clear()
    q1.clear()
    q3.clear()
    iqr.clear()
    q1MinusIQR.clear()
    q3PlusIQR.clear()
    table.clear()

