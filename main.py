import pandas as pd
from datetime import datetime
from prettytable import PrettyTable

dataSet1 = pd.read_csv('Data set/INOUT.csv')
dataSet2 = pd.read_csv('Data set/INOUTLINE.csv')
dataSet3 = pd.read_csv('Data set/PRODUCTINSTANCE.csv', encoding='cp1252')
dataSet4 = pd.read_csv('Data set/PRODUCTS.csv')
dataSet5 = pd.read_csv('Data set/TRANSFER_ITEM.csv')
dataSet6 = pd.read_csv('Data set/TRANSFER_ITEM_D.csv')
dataSets = [dataSet1, dataSet2, dataSet3, dataSet4, dataSet5, dataSet6]


def dateValidityCheck(data):
    validCount = 0
    for i in range(dataSize):
        for fmt in ("%m/%d/%Y %H:%M","%m/%d/%Y %H:%M:%S %p"):
            try:
                datetime.strptime(data[i], fmt)
                validCount += 1
            except Exception:
                continue
    return round((validCount/dataSize)*100, 3)


def currentnessCalculator(data):
    upToDateData = 0
    for i in range(dataSize):
        for fmt in ("%m/%d/%Y %H:%M","%m/%d/%Y %H:%M:%S %p"):
            try:
                date = datetime.strptime(data[i], fmt)
                if currentYear - date.year <= 3:
                    upToDateData += 1
            except Exception:
                continue
    return round((upToDateData/dataSize)*100, 3)


def stringToInt(data):
    df = pd.to_numeric(data, errors='coerce')  # string ha tabdil be null mishan
    return floatToInt(df)


def floatToInt(data):
    return data.convert_dtypes()


def validityCheck(data):
    validData = data.dropna().size
    return round((validData/dataSize)*100, 3)


tableTitle = ["name", "data size", "null count", "Completeness", "Validity"]

floatToIntData1 = ["DOCUMENTNO","REF_ORG","C_COSTCENTER_ID","COM_BPARTNER_ID","M_PRODUCT_ID","REQUESTNO",\
                  "RESPONSIBLEMANAGER","FROMUSERMANAGERID","COM_BPARTNER_ID_F","M_INOUT_AMVAL_ID","DOCUMENTNO1",\
                  "LOCATIONS_ID","ACCT_AC_HOLDING_ID","LETTERNO","VAHED_MALI","ACCT_AC_JOURNAL_ID","BASEINFO_RECORDID","C_YEAR_ID"]
floatToIntData2 = ["VAHED_MALI","PRODUCT_BATCH_ID","BASEINFO_RECORDID","C_YEAR_ID","M_INOUT_AMVAL_ID",]
floatToIntData3 = ["M_PRODUCT_ID","UPDATEDBY","DATE1","PARENT_ID","ISSUMMARY","BOOKVALUE"]
floatToIntData4 = []
floatToIntData5 = []
floatToIntData6 = []

dateData1 = ["LETTERDATE","REQUESTDATE","DOCUMENTDATE","UPDATED","CREATED"]
dateData2 = ["OPERATIONDATE","REACHMENTDATE","UPDATED","CREATED"]
dateData3 = ["REACHMENTDATE","DATE1","UPDATED","CREATED","ENDOFUSEFULLIFE","OPERATIONDATE","DOCUMENTDATE","LETTERDATE"]
dateData4 = ["CREATED","UPDATED"]
dateData5 = ["CREATED","UPDATED","OPERATIONDATE","FROM_DATE","LETTER_DATE"]
dateData6 = ["CREATED","UPDATED","REACHMENTDATE","OPERATIONDATE","TRANSFER_ITEM_ID"]

stringToIntData1 = ["SUB_REF_ORG","RESPONSIBLEBPARTNER","C_DOCTYPE_ID","DESCRIPTION"]
stringToIntData2 = []
stringToIntData3 = ["AD_CLIENT_ID","AD_ORG_ID","C_COSTCENTER_ID","AD_ORG_REF_ID","M_PI_STATUS_ID","HASCONTROL",\
                    "M_PRODUCTINSTANCE_BASEINFO_ID","COSTLINE","PRIMALVALUE","USEFULLIFE","SALVAGEVALUE",\
                    "PI_VALUEAFTERCOEFFICIENTINC","OPERATIONDATE","PRESENTVALUE","COM_BPARTNER_ID","M_INOUT_AMVAL_ID",\
                    "DOCUMENNO","SUB_REF_ORG","DEPRECATIONRATE","RETURNAMVALTOANBAR","TYPEMELKOFCONTRACT","NEW_L_DATE","MAP_DATE"]
stringToIntData4 = ["C_UOM_ID","NEXTLEVELDIGITS","CODEDIGITS","IRANCODE","IRANCODE","DESC1","M_ACCOUNTINGASSET_ID","M_PRODUCT_ID2",\
                    "M_PRODUCT_TYPE_ID","ESTEHLAK_GROUP_CODE","HAZINE_GROUP","SATH","OLGO_M_PRODUCT_ID"]
stringToIntData5 = ["OLDLABELNO","M_TRANSFER_KALA_ID","DOC_NO","DOCUMENTNO","ADDRESS","LOCATIONS_ID","VAHED_MALI","TYPEPROPERTY"]
stringToIntData6 = ["RETURNAMVALTOANBAR","TYPEPROPERTY","C_YEAR_ID","VAHED_MALI","TYPE_PRODUCT"]

dateDataList = [dateData1, dateData2, dateData3, dateData4, dateData5, dateData6]
floatToIntDataList = [floatToIntData1, floatToIntData2, floatToIntData3, floatToIntData4, floatToIntData5, floatToIntData6]
stringToIntDataList = [stringToIntData1, stringToIntData2, stringToIntData3, stringToIntData4, stringToIntData5, stringToIntData6]

nullCount = []
completeness = []
validity = []
attributeName = []
sizeList = []
table = PrettyTable()
currentYear = 2022

for dataSet in dataSets:
    dateData = dateDataList.pop(0)
    stringToIntData = stringToIntDataList.pop(0)
    floatToIntData = floatToIntDataList.pop(0)

    for attribute in dataSet.columns:
        attributeName.append(attribute)
        data = dataSet[attribute]
        dataSize = data.size
        sizeList.append(dataSize)
        nonNullDataSize = data.dropna().size
        completenessValue = round((nonNullDataSize/dataSize)*100, 3)
        nullCount.append(dataSize - nonNullDataSize)
        completeness.append(completenessValue)

        if attribute in stringToIntData:
            data = stringToInt(data)
        elif attribute in floatToIntData:
            data = floatToInt(data)
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
    print(" Data Currentness: " + str(currentnessCalculator(dataSet["UPDATED"])) + "\n")

    table.clear()
    nullCount.clear()
    completeness.clear()
    validity.clear()
    attributeName.clear()
    sizeList.clear()
