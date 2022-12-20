import pandas as pd
import numpy as np
from datetime import datetime

# part 1
productsDataSet = pd.read_csv('Data set/PRODUCTS.csv')

maxYear = 2022
minYear = 2013

def goodsPerYearCounter(data):

    for i in range(data.size):
        for fmt in ("%m/%d/%Y %H:%M", "%m/%d/%Y %H:%M:%S %p"):
            try:
                date = datetime.strptime(data[i], fmt)
                yearList[date.year - minYear] += 1
            except Exception:
                continue


yearList = [0] * (maxYear - minYear + 1)
goodsPerYearCounter(productsDataSet["CREATED"])

print("count of registered goods")
for i in range(len(yearList)):
    print("year " + str(i + minYear) + " : " + str(yearList[i]))



# part 2
productInsDataSet = pd.read_csv('Data set/PRODUCTINSTANCE.csv', encoding='cp1252')

def stringRemover(data):
    df = pd.to_numeric(data, errors='coerce')
    return df

def printFirstNItem(holdingId):
    maxShowCount = 5
    i = 0
    for itemKey in holdingInfo[holdingId]:
        count = itemInfo[itemKey][0]
        value = itemInfo[itemKey][1]
        print("ItemID_HoldingID: " + itemKey)
        print("count: " + str(count) + "  value: " + str("%.2f"%(value/count)) +\
              "  valueSum: " + str(value) +"\n")
        if i == maxShowCount:
            break
        i += 1


holdingColumn = productInsDataSet["ACCT_AC_HOLDING_ID"]
holdingData = stringRemover(holdingColumn)
prodIdBookValData = productInsDataSet[["M_PRODUCT_ID", "BOOKVALUE"]]
dataSet = pd.concat([holdingData, prodIdBookValData], join='outer', axis=1)
cleanedDataSet = dataSet.dropna().astype('int64')

defaultItemCount = 1
holdingInfo = {}
itemInfo = {}
holdingVal = []
for i, holdingId in enumerate(cleanedDataSet["ACCT_AC_HOLDING_ID"]):
    productId = cleanedDataSet["M_PRODUCT_ID"].iloc[i]
    bookValue = cleanedDataSet["BOOKVALUE"].iloc[i]
    ItemKey = str(productId) + "_" + str(holdingId)

    if holdingId not in holdingInfo.keys():
        itemInfo[ItemKey] = [defaultItemCount, bookValue]
        holdingInfo[holdingId] = []
    else:
        if ItemKey not in itemInfo.keys():
            holdingInfo[holdingId].append(ItemKey)
            itemInfo[ItemKey] = [defaultItemCount, bookValue]
        else:
            itemCount = itemInfo[ItemKey][0] + 1
            itemValue = itemInfo[ItemKey][1] + bookValue
            itemInfo[ItemKey] = [itemCount, itemValue]

for holdingKey in holdingInfo.keys():
    printFirstNItem(holdingKey)
    print("----------\n")


# part 3
inOutDataSet = pd.read_csv('Data set/INOUT.csv')

data3 = inOutDataSet[["C_DOCSTATUS_ID","INOUT_ID"]].copy()

pishNevis = data3[data3.C_DOCSTATUS_ID == 3000006]
print(pishNevis)

nahaii = data3[data3.C_DOCSTATUS_ID == 3000025]
print(nahaii)

others = data3[(data3.C_DOCSTATUS_ID != 3000006) & (data3.C_DOCSTATUS_ID != 3000025)]
print(others)