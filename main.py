import pandas as pd
from datetime import datetime
# part 1
dataSet = pd.read_csv('Data set/PRODUCTS.csv')

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
goodsPerYearCounter(dataSet["CREATED"])

print("count of registered goods")
for i in range(len(yearList)):
    print("year " + str(i + minYear) + " : " + str(yearList[i]))

# part 3
dataSet3 = pd.read_csv('Data set/INOUT.csv')

data3 = dataSet3[["C_DOCSTATUS_ID","INOUT_ID"]].copy()

pishNevis = data3[data3.C_DOCSTATUS_ID == 3000006]
print(pishNevis)

nahaii = data3[data3.C_DOCSTATUS_ID == 3000025]
print(nahaii)

others = data3[(data3.C_DOCSTATUS_ID != 3000006) & (data3.C_DOCSTATUS_ID != 3000025)]
print(others)