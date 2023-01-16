import pandas as pd
from itemInfo import ItemsInfo
from consumerInfo import ConsumerInfo
from datetime import datetime
from ast import literal_eval
import matplotlib.pyplot as plt
import re
from sklearn import metrics
from sklearn.cluster import DBSCAN,OPTICS,Birch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import *
import numpy as np
import matplotlib.pyplot as plt
from functions import *
import math
import hdbscan


# to ignore "DtypeWarning", generated due to reading csv files
import warnings
warnings.filterwarnings("ignore")


#part 1

productInsDataSet = pd.read_csv('Data set/PRODUCTINSTANCE.csv', encoding='cp1252')
cleanDataSet = productInsDataSet[["AD_ORG_REF_ID", "RETURNAMVALTOANBAR"]].dropna()

orgInfo = {}

for i, orgId in enumerate(cleanDataSet["AD_ORG_REF_ID"]):
    key = int(orgId)
    if key not in orgInfo.keys():
        orgInfo[key] = (0, 0) #retuenedCount, purchasedCount

    returnedItems = orgInfo[key][0]
    purchasedItems = orgInfo[key][1]
    returnStatus = cleanDataSet["RETURNAMVALTOANBAR"].iloc[i]
    if returnStatus == 3 or returnStatus == 4:
        returnedItems = returnedItems + 1
    orgInfo[key] = (returnedItems, purchasedItems + 1)

for orgId in orgInfo.keys():
    returnedItemsCount = orgInfo[orgId][0]
    purchasedItemsCount = orgInfo[orgId][1]
    print("Organization Id: " + str(orgId))
    print("Returned Items Count: " + str(returnedItemsCount))
    print("Purchased Item Count:" + str(purchasedItemsCount))
    print("returned-purchased Ratio:" + str("%.2f"%(returnedItemsCount/purchasedItemsCount)))
    print("*************************")



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
            if operationYear < createdYear:
                continue

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
        input_item_count = str(ItemsInfo.inputPerYear[year])
        output_item_count = str(ItemsInfo.outputPerYear[year])
        print("_____________________________")
        print("year:" + str(year))
        print("Input: " + input_item_count + "  Output:" + output_item_count)
        print_purchased_info(year)
        top_output, top_output_count = ItemsInfo.get_top_operated_item_per_year(year)
        print("most operated item: " + str(top_output))
        print("most operated item count: " + str(top_output_count))


def print_purchased_info(year):
    most_input_item_id = 0
    most_input_item_count = 0
    consumer_id = 0
    consumer_purchase_count = 0

    for key in items.keys():
        if str(year) in key:
            item = items[key]
            item_count = item.item_count
            if item_count > most_input_item_count:
                most_input_item_count = item_count
                most_input_item_id = item.id
                consumer_id = item.get_top_consumer()
                consumer_purchase_count = item.get_top_consumer_purchase_count()

    print("most purchased item: " + str(most_input_item_id))
    print("most purchased item count:" + str(most_input_item_count))
    print("top consumer: " + str(consumer_id))
    print("top consumer purchase count: " + str(consumer_purchase_count))


def print_top_consumers(min_purchase_count):
    for consumer_id in consumers.keys():
        if consumers[consumer_id].purchase_count > min_purchase_count:
            most_purchased_item, count = consumers[consumer_id].get_most_purchased_item()
            print("________________________")
            print("id:"+str(consumer_id))
            print("most purchased item: " + str(most_purchased_item))
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
print_top_consumers(300)




