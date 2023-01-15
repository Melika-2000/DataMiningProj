import pandas as pd
from itemInfo import ItemsInfo
from consumerInfo import ConsumerInfo
from datetime import datetime
from ast import literal_eval
import matplotlib.pyplot as plt


#part 1
#
# productInsDataSet = pd.read_csv('Data set/PRODUCTINSTANCE.csv', encoding='cp1252')
# cleanDataSet = productInsDataSet[["AD_ORG_REF_ID", "RETURNAMVALTOANBAR"]].dropna()
#
# orgInfo = {}
#
# for i, orgId in enumerate(cleanDataSet["AD_ORG_REF_ID"]):
#     key = int(orgId)
#     if key not in orgInfo.keys():
#         orgInfo[key] = (0, 0) #retuenedCount, purchasedCount
#
#     returnedItems = orgInfo[key][0]
#     purchasedItems = orgInfo[key][1]
#     returnStatus = cleanDataSet["RETURNAMVALTOANBAR"].iloc[i]
#     if returnStatus == 3 or returnStatus == 4:
#         returnedItems = returnedItems + 1
#     orgInfo[key] = (returnedItems, purchasedItems + 1)
#
# #print
# for orgId in orgInfo.keys():
#     returnedItemsCount = orgInfo[orgId][0]
#     purchasedItemsCount = orgInfo[orgId][1]
#     print("Organization Id: " + str(orgId))
#     print("Returned Items Count: " + str(returnedItemsCount))
#     print("Purchased Item Count:" + str(purchasedItemsCount))
#     print("returned-purchased Ratio:" + str("%.2f"%(returnedItemsCount/purchasedItemsCount)))
#     print("*************************")



#part 2
inOutlineDataSet = pd.read_csv('Data set/INOUTLINE.csv')
cleanDataSet = inOutlineDataSet[["M_PRODUCT_ID", "CONSUMER", "CREATED", "OPERATIONDATE"]].dropna()
items = {}
consumers = {}

for i in range(cleanDataSet["CREATED"].size):
    for fmt in ("%m/%d/%Y %H:%M", "%m/%d/%Y %H:%M:%S %p"):
        try:
            createdYear = datetime.strptime(cleanDataSet["CREATED"].iloc[i], fmt).year
            operationYear = datetime.strptime(cleanDataSet["OPERATIONDATE"].iloc[i], fmt).year
            itemId = int(cleanDataSet["M_PRODUCT_ID"].iloc[i])
            consumerId = int(cleanDataSet["CONSUMER"].iloc[i])

            itemKey = str(createdYear) + "_" + str(itemId)
            if itemKey not in items.keys():
                items[itemKey] = ItemsInfo(itemId, consumerId, createdYear, operationYear)
            else:
                item = items[itemKey]
                item.update_item_info(consumerId, createdYear, operationYear)

            consumerKey = consumerId
            if consumerKey not in consumers.keys():
                consumers[consumerKey] = ConsumerInfo(consumerId, itemId, createdYear, operationYear)
            else:
                consumer = consumers[consumerKey]
                consumer.update_consumer_info(itemId, createdYear, operationYear)

        except Exception as e:
            continue


def print_inout_per_year():
    for year in ItemsInfo.inputPerYear.keys():
        inItemCount = str(ItemsInfo.inputPerYear[year])
        outItemCount = str(ItemsInfo.outputPerYear[year])
        print(str(year) + "________________________________")
        print("Input: " + inItemCount + "  Output:" + outItemCount)
        print_most_purchased_item(year)
        topOutput, topOutputCoount = ItemsInfo.get_top_operated_item_per_year(year)
        print("most operated item: "+str(topOutput))
        print("most operated item count: " + str(topOutputCoount))


def print_most_purchased_item(year):
    mostInputItemId = 0
    mostInputItemCount = 0
    consumerId = 0
    consumerPurchaseCount = 0

    for key in items.keys():
        if str(year) in key:
            item = items[key]
            itemCount = item.item_count
            if itemCount > mostInputItemCount:
                mostInputItemCount = itemCount
                mostInputItemId = item.id
                consumerId = item.get_top_consumer()
                consumerPurchaseCount = item.get_top_consumer_purchase_count()

    print("most purchased item: " + str(mostInputItemId))
    print("most purchased item count:" + str(mostInputItemCount))
    print("top consumer: " + str(consumerId))
    print("top consumer purchase count: " + str(consumerPurchaseCount))

def print_top_consumers(min_purchase_count):
    for consumer_id in consumers.keys():
        if consumers[consumer_id].purchase_count > min_purchase_count:
            mostPurchasedItem, count = consumers[consumer_id].get_most_purchased_item()
            print(str(consumer_id) + "______________________")
            print("most purchased item: " + str(mostPurchasedItem))
            print("most purchased item count: " + str(count))
            input_per_year = consumers[consumer_id].inputPerYearCount
            output_per_year = consumers[consumer_id].outputPerYearCount
            print("input:")
            for year in input_per_year.keys():
                print("year: " + str(year) + "   count: " + str(input_per_year[year]))
            print("output:")
            for year in output_per_year.keys():
                print("year: " + str(year) + "   count: " + str(output_per_year[year]))



print_inout_per_year()
print_top_consumers(700)
