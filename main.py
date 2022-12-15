import pandas as pd
from datetime import datetime

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