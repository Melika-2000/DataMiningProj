import pandas as pd

productInsDataSet = pd.read_csv('Data set/PRODUCTINSTANCE.csv', encoding='cp1252')
cleanDataSet = productInsDataSet[["AD_ORG_REF_ID", "RETURNAMVALTOANBAR"]].dropna()

orgInfo = {}

for i, orgId in enumerate(cleanDataSet["AD_ORG_REF_ID"]):
    key = orgId
    if key not in orgInfo.keys():
        orgInfo[key] = (0, 0) #retuenedCount, purchasedCount

    returnedItems = orgInfo[key][0]
    purchasedItems = orgInfo[key][1]
    returnStatus = cleanDataSet["RETURNAMVALTOANBAR"].iloc[i]
    if returnStatus == 3 or returnStatus == 4:
        returnedItems = returnedItems + 1
    orgInfo[key] = (returnedItems, purchasedItems + 1)

#print
for orgId in orgInfo.keys():
    returnedItemsCount = orgInfo[orgId][0]
    purchasedItemsCount = orgInfo[orgId][1]
    print("orgId: " + str(orgId))
    print("Returned Items Count: " + str(returnedItemsCount) +"   Purchased Item Count:" + str(purchasedItemsCount))
    print("returned-purchased Ratio:" + str("%.2f"%(returnedItemsCount/purchasedItemsCount)))
    print("*************************")

