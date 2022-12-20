import pandas as pd
import numpy as np
from datetime import datetime

# part 1
# productsDataSet = pd.read_csv('Data set/PRODUCTS.csv')
#
# maxYear = 2022
# minYear = 2013
#
# def goodsPerYearCounter(data):
#
#     for i in range(data.size):
#         for fmt in ("%m/%d/%Y %H:%M", "%m/%d/%Y %H:%M:%S %p"):
#             try:
#                 date = datetime.strptime(data[i], fmt)
#                 yearList[date.year - minYear] += 1
#             except Exception:
#                 continue
#
#
# yearList = [0] * (maxYear - minYear + 1)
# goodsPerYearCounter(productsDataSet["CREATED"])
#
# print("count of registered goods")
# for i in range(len(yearList)):
#     print("year " + str(i + minYear) + " : " + str(yearList[i]))


# part 2
productInsDataSet = pd.read_csv('Data set/PRODUCTINSTANCE.csv', encoding='cp1252')

def stringRemover(data):
    df = pd.to_numeric(data, errors='coerce')
    return df

holdingColumn = productInsDataSet["ACCT_AC_HOLDING_ID"]
holdingData = stringRemover(holdingColumn)
prodIdBookValData = productInsDataSet[["M_PRODUCT_ID", "BOOKVALUE"]]
dataSet = pd.concat([holdingData, prodIdBookValData], join='outer', axis=1)
cleanedDataSet = dataSet.dropna().astype('int64')

defaultItemCount = 1
holdingInfo = {}
itemInfo = {}

for i, holdingId in enumerate(cleanedDataSet["ACCT_AC_HOLDING_ID"]):
    productId = cleanedDataSet["M_PRODUCT_ID"].iloc[i]
    bookValue = cleanedDataSet["BOOKVALUE"].iloc[i]
    ItemKey = str(productId) + "_" + str(holdingId)

    if holdingId not in holdingInfo.keys():
        itemInfo[ItemKey] = [defaultItemCount, bookValue]
        holdingInfo[holdingId] = itemInfo
    else:
        if ItemKey not in itemInfo.keys():
            itemInfo[ItemKey] = [defaultItemCount, bookValue]
            holdingInfo[holdingId] = itemInfo
        else:
            itemCount = itemInfo[ItemKey][0] + 1
            itemValue = itemInfo[ItemKey][1] + bookValue
            itemInfo[ItemKey] = [itemCount, itemValue]
        # holdingInfo[holdingId] = itemInfo

print(holdingInfo)



# finalData = pd.concat([holdingId, bookValue], join='outer', axis=1)
# data3 = finalData.dropna().astype('int64')
# for item in intData["ACCT_AC_HOLDING_ID"]:
#     print(item)
# temp = data3.groupby("ACCT_AC_HOLDING_ID")["BOOKVALUE"].count()
# print(temp)
#
# holding = {}
# defaultCount = 1
# defaultSum = 0
#
# for i in data3["ACCT_AC_HOLDING_ID"]:
#     if i > 20:
#         print(i)
#     if item not in data3.keys():
#         holding[item] =
#     else:
#         holding[item] = holding.get(item) + 1

# print(data2.size)
# data3 = data2[["ACCT_AC_HOLDING_ID","BOOKVALUE"]].dropna()
#
# print(data3.size)
# data4 = data3.astype('int64')
# print(data4)
#


#
#








# part 3
# inOutDataSet = pd.read_csv('Data set/INOUT.csv')
#
# data3 = inOutDataSet[["C_DOCSTATUS_ID","INOUT_ID"]].copy()
#
# pishNevis = data3[data3.C_DOCSTATUS_ID == 3000006]
# print(pishNevis)
#
# nahaii = data3[data3.C_DOCSTATUS_ID == 3000025]
# print(nahaii)
#
# others = data3[(data3.C_DOCSTATUS_ID != 3000006) & (data3.C_DOCSTATUS_ID != 3000025)]
# print(others)