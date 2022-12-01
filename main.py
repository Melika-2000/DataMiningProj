import pandas as pd
from datetime import datetime
from prettytable import PrettyTable

dataSet1 = pd.read_csv('DataSets/INOUT.csv')
dataSet2 = pd.read_csv('DataSets/INOUTLINE.csv')
dataSet3 = pd.read_csv('DataSets/TRANSFER_ITEM_D.csv')
dataSet4 = pd.read_csv('DataSets/TRANSFER_ITEM.csv')
dataSet5 = pd.read_csv('DataSets/PRODUCTS.csv')
dataSet6 = pd.read_csv('DataSets/PRODUCTINSTANCE.csv', encoding='cp1252')
dataSets = [dataSet1, dataSet2, dataSet3, dataSet4, dataSet5, dataSet6]

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

# 111111111111111111111
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

table.clear()
tableTitle.clear()
stringToIntData.clear()
floatToIntData.clear()
dateData.clear()
nullCount.clear()
completeness.clear()
validity.clear()
attributeName.clear()
sizeList.clear()



# 222222222222222222222
tableTitle = ["name", "data size", "null count", "Completeness", "Validity"]

stringToIntData = []

floatToIntData = ["VAHED_MALI","PRODUCT_BATCH_ID","BASEINFO_RECORDID","C_YEAR_ID","M_INOUT_AMVAL_ID",]

dateData = ["OPERATIONDATE","REACHMENTDATE","UPDATED","CREATED"]

nullCount = []
completeness = []
validity = []
attributeName = []
sizeList = []

table = PrettyTable()
for attribute in dataSet2.columns:
    attributeName.append(attribute)
    data = dataSet2[attribute]
    dataSize = data.size
    sizeList.append(dataSize)
    nonNullDataSize = data.dropna().size
    completenessValue = (nonNullDataSize/dataSize)*100
    nullCount.append(dataSize - nonNullDataSize)
    completeness.append(completenessValue)

    if attribute in stringToIntData:
        data = stringToInt(dataSet2[attribute])
    elif attribute in floatToIntData:
        data = floatToInt(dataSet2[attribute])
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

table.clear()
tableTitle.clear()
stringToIntData.clear()
floatToIntData.clear()
dateData.clear()
nullCount.clear()
completeness.clear()
validity.clear()
attributeName.clear()
sizeList.clear()


# 333333333333333333333
tableTitle = ["name", "data size", "null count", "Completeness", "Validity"]

stringToIntData = ["AD_CLIENT_ID","AD_ORG_ID","C_COSTCENTER_ID","AD_ORG_REF_ID","M_PI_STATUS_ID","HASCONTROL","M_PRODUCTINSTANCE_BASEINFO_ID",\
    "COSTLINE","PRIMALVALUE","USEFULLIFE","SALVAGEVALUE","PI_VALUEAFTERCOEFFICIENTINC","OPERATIONDATE","PRESENTVALUE",\
        "COM_BPARTNER_ID","M_INOUT_AMVAL_ID","DOCUMENNO","SUB_REF_ORG","DEPRECATIONRATE","RETURNAMVALTOANBAR","TYPEMELKOFCONTRACT",\
            "NEW_L_DATE","MAP_DATE"]

floatToIntData = ["M_PRODUCT_ID","UPDATED","UPDATEDBY","","DATE1","PARENT_ID","ISSUMMARY","BOOKVALUE"]

dateData = ["REACHMENTDATE","DATE1","UPDATED","CREATED","ENDOFUSEFULLIFE","OPERATIONDATE","DOCUMENTDATE","LETTERDATE"]

nullCount = []
completeness = []
validity = []
attributeName = []
sizeList = []

table = PrettyTable()
for attribute in dataSet2.columns:
    attributeName.append(attribute)
    data = dataSet2[attribute]
    dataSize = data.size
    sizeList.append(dataSize)
    nonNullDataSize = data.dropna().size
    completenessValue = (nonNullDataSize/dataSize)*100
    nullCount.append(dataSize - nonNullDataSize)
    completeness.append(completenessValue)

    if attribute in stringToIntData:
        data = stringToInt(dataSet2[attribute])
    elif attribute in floatToIntData:
        data = floatToInt(dataSet2[attribute])
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

table.clear()
tableTitle.clear()
stringToIntData.clear()
floatToIntData.clear()
dateData.clear()
nullCount.clear()
completeness.clear()
validity.clear()
attributeName.clear()
sizeList.clear()



# 444444444444444444444
tableTitle = ["name", "data size", "null count", "Completeness", "Validity"]

stringToIntData = ["C_UOM_ID","NEXTLEVELDIGITS","CODEDIGITS","IRANCODE","IRANCODE","DESC1","M_ACCOUNTINGASSET_ID","M_PRODUCT_ID2",\
    "M_PRODUCT_TYPE_ID","ESTEHLAK_GROUP_CODE","HAZINE_GROUP","SATH","OLGO_M_PRODUCT_ID"]

floatToIntData = []

dateData = ["CREATED","CREATED"]

nullCount = []
completeness = []
validity = []
attributeName = []
sizeList = []

table = PrettyTable()
for attribute in dataSet2.columns:
    attributeName.append(attribute)
    data = dataSet2[attribute]
    dataSize = data.size
    sizeList.append(dataSize)
    nonNullDataSize = data.dropna().size
    completenessValue = (nonNullDataSize/dataSize)*100
    nullCount.append(dataSize - nonNullDataSize)
    completeness.append(completenessValue)

    if attribute in stringToIntData:
        data = stringToInt(dataSet2[attribute])
    elif attribute in floatToIntData:
        data = floatToInt(dataSet2[attribute])
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

table.clear()
tableTitle.clear()
stringToIntData.clear()
floatToIntData.clear()
dateData.clear()
nullCount.clear()
completeness.clear()
validity.clear()
attributeName.clear()
sizeList.clear()

# 555555555555555555555
tableTitle = ["name", "data size", "null count", "Completeness", "Validity"]

stringToIntData = ["OLDLABELNO","M_TRANSFER_KALA_ID","DOC_NO","DOCUMENTNO","ADDRESS","LETTER_DATE","LOCATIONS_ID","VAHED_MALI",\
    "TYPEPROPERTY"]

floatToIntData = []

dateData = ["CREATED","UPDATED","OPERATIONDATE","FROM_DATE",""]

nullCount = []
completeness = []
validity = []
attributeName = []
sizeList = []

table = PrettyTable()
for attribute in dataSet2.columns:
    attributeName.append(attribute)
    data = dataSet2[attribute]
    dataSize = data.size
    sizeList.append(dataSize)
    nonNullDataSize = data.dropna().size
    completenessValue = (nonNullDataSize/dataSize)*100
    nullCount.append(dataSize - nonNullDataSize)
    completeness.append(completenessValue)

    if attribute in stringToIntData:
        data = stringToInt(dataSet2[attribute])
    elif attribute in floatToIntData:
        data = floatToInt(dataSet2[attribute])
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

table.clear()
tableTitle.clear()
stringToIntData.clear()
floatToIntData.clear()
dateData.clear()
nullCount.clear()
completeness.clear()
validity.clear()
attributeName.clear()
sizeList.clear()

# 666666666666666666666
tableTitle = ["name", "data size", "null count", "Completeness", "Validity"]

stringToIntData = ["RETURNAMVALTOANBAR","TYPEPROPERTY","C_YEAR_ID","VAHED_MALI","TYPE_PRODUCT"]

floatToIntData = []

dateData = ["CREATED","UPDATED","REACHMENTDATE","OPERATIONDATE","TRANSFER_ITEM_ID",""]

nullCount = []
completeness = []
validity = []
attributeName = []
sizeList = []

table = PrettyTable()
for attribute in dataSet2.columns:
    attributeName.append(attribute)
    data = dataSet2[attribute]
    dataSize = data.size
    sizeList.append(dataSize)
    nonNullDataSize = data.dropna().size
    completenessValue = (nonNullDataSize/dataSize)*100
    nullCount.append(dataSize - nonNullDataSize)
    completeness.append(completenessValue)

    if attribute in stringToIntData:
        data = stringToInt(dataSet2[attribute])
    elif attribute in floatToIntData:
        data = floatToInt(dataSet2[attribute])
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

table.clear()
tableTitle.clear()
stringToIntData.clear()
floatToIntData.clear()
dateData.clear()
nullCount.clear()
completeness.clear()
validity.clear()
attributeName.clear()
sizeList.clear()

