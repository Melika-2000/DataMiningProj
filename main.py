import pandas as pd
from datetime import datetime
from prettytable import PrettyTable

dataSet1 = pd.read_csv('Data set/INOUT.csv')
# dataSet2 = pd.read_csv('Data set/INOUTLINE.csv')
# dataSet3 = pd.read_csv('Data set/TRANSFER_ITEM_D.csv')
# dataSet4 = pd.read_csv('Data set/TRANSFER_ITEM.csv')
# dataSet5 = pd.read_csv('Data set/PRODUCTS.csv')
# dataSet6 = pd.read_csv('Data set/PRODUCTINSTANCE.csv', encoding='cp1252')
#dataSets = [dataSet1, dataSet2, dataSet3, dataSet4, dataSet5, dataSet6]

def dateValidityCheck(data):
    validCount = 0
    for i in range(dataSize):
        try:
            datetime.strptime(data[i], "%m/%d/%Y %H:%M")
            validCount += 1
        except Exception:
            continue
    return (validCount/dataSize)*100

def stringToInt(data):
    df = pd.to_numeric(data, errors='coerce')  # string ha tabdil be null mishan
    return floatToInt(df)

def floatToInt(data):
    return data.convert_dtypes()

def validityCheck(data):
    validData = data.dropna().size
    return (validData/dataSize)*100


tableTitle = ["name", "data size", "null count", "Completeness", "Validity"]

stringToIntData = ["SUB_REF_ORG","RESPONSIBLEBPARTNER","C_DOCTYPE_ID","DESCRIPTION"]

floatToIntData = ["DOCUMENTNO","REF_ORG","C_COSTCENTER_ID","COM_BPARTNER_ID","M_PRODUCT_ID","REQUESTNO",\
                  "RESPONSIBLEMANAGER","FROMUSERMANAGERID","COM_BPARTNER_ID_F","M_INOUT_AMVAL_ID","DOCUMENTNO1",\
                  "LOCATIONS_ID","ACCT_AC_HOLDING_ID","LETTERNO","VAHED_MALI","ACCT_AC_JOURNAL_ID","BASEINFO_RECORDID","C_YEAR_ID"]

dateData = ["LETTERDATE","REQUESTDATE","DOCUMENTDATE","UPDATED","CREATED"]


nullCount = []
completeness = []
validity = []
attributeName = []
sizeList = []

table = PrettyTable()

for attribute in dataSet1.columns:
    attributeName.append(attribute)
    data = dataSet1[attribute]
    dataSize = data.size
    sizeList.append(dataSize)
    nonNullDataSize = data.dropna().size
    completenessValue = (nonNullDataSize/dataSize)*100
    nullCount.append(dataSize - nonNullDataSize)
    completeness.append(completenessValue)

    if attribute in stringToIntData:
        data = stringToInt(dataSet1[attribute])
    elif attribute in floatToIntData:
        data = floatToInt(dataSet1[attribute])
    elif attribute in dateData:
        result = dateValidityCheck(data)
        validity.append(result)
        continue

    result = validityCheck(data)
    validity.append(result)


table.add_column(tableTitle[0], attributeName)
table.add_column(tableTitle[1], sizeList)
table.add_column(tableTitle[2], nullCount)
table.add_column(tableTitle[3], completeness)
table.add_column(tableTitle[4], validity)

print(table)