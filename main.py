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
title = ["name", "type", "min", "max", "mean", "median", "IQR1(25%)", "IQR3(75%)"]


table = PrettyTable()
maxList = []
minList = []
typeList = []
meanList = []
nameList = []
medianList = []
modeList = []
iqr1 = []
iqr3 = []

for dataSet in dataSets:
    for attribute in dataSet.columns:

        if dataSet[attribute].dtype == 'object':
            continue

        sns.boxplot(y=dataSet[attribute])
        plt.show()

        nameList.append(attribute)
        typeList.append(dataSet[attribute].dtype)
        minList.append(dataSet[attribute].min())
        maxList.append(dataSet[attribute].max())
        meanList.append(dataSet[attribute].mean())
        medianList.append(dataSet[attribute].median())
        iqr1.append(dataSet[attribute].describe()[4])
        iqr3.append(dataSet[attribute].describe()[6])

    table.add_column(title[0], nameList)
    table.add_column(title[1], typeList)
    table.add_column(title[2], minList)
    table.add_column(title[3], maxList)
    table.add_column(title[4], meanList)
    table.add_column(title[5], medianList)
    table.add_column(title[6],iqr1)
    table.add_column(title[7],iqr3)

    print(table)

    maxList.clear()
    minList.clear()
    typeList.clear()
    meanList.clear()
    nameList.clear()
    medianList.clear()
    modeList.clear()
    iqr1.clear()
    iqr3.clear()
    table.clear()

