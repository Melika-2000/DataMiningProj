import pandas as pd
import re
from sklearn import metrics
from sklearn.cluster import DBSCAN
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt 
from functions import *


# to ignore "DtypeWarning", generated due to reading csv files
import warnings
warnings.filterwarnings("ignore")


#part 1

# productInsDataSet = pd.read_csv('Data set/PRODUCTINSTANCE.csv', encoding='cp1252')
# cleanDataSet = productInsDataSet[["AD_ORG_REF_ID", "RETURNAMVALTOANBAR"]].dropna()

# orgInfo = {}

# for i, orgId in enumerate(cleanDataSet["AD_ORG_REF_ID"]):
#     key = orgId
#     if key not in orgInfo.keys():
#         orgInfo[key] = (0, 0) #retuenedCount, purchasedCount

#     returnedItems = orgInfo[key][0]
#     purchasedItems = orgInfo[key][1]
#     returnStatus = cleanDataSet["RETURNAMVALTOANBAR"].iloc[i]
#     if returnStatus == 3 or returnStatus == 4:
#         returnedItems = returnedItems + 1
#     orgInfo[key] = (returnedItems, purchasedItems + 1)

# #print
# for orgId in orgInfo.keys():
#     returnedItemsCount = orgInfo[orgId][0]
#     purchasedItemsCount = orgInfo[orgId][1]
#     print("orgId: " + str(orgId))
#     print("Returned Items Count: " + str(returnedItemsCount) +"   Purchased Item Count:" + str(purchasedItemsCount))
#     print("returned-purchased Ratio:" + str("%.2f"%(returnedItemsCount/purchasedItemsCount)))
#     print("*************************")



# #part 2
# inOutlineDataSet = pd.read_csv('Data set/INOUTLINE.csv')
# cleanDataSet = inOutlineDataSet[["INOUTLINE_ID", "CREATED", "OPERATIONDATE", "M_WAREHOUSE_ID"]].dropna()

# def goodsPerYearCounter(data):
#     for i in range(data.size):
#         for fmt in ("%m/%d/%Y %H:%M", "%m/%d/%Y %H:%M:%S %p"):
#             try:
#                 year = datetime.strptime(data[i], fmt).year
#             except Exception:
#                 continue

# years = {}
# print(cleanDataSet)
# for item in cleanDataSet.values:
#     print(item)
# print(cleanDataSet["OPERATIONDATE"])

# part 3

products_DataSet = pd.read_csv('Data set/PRODUCTS.csv')

# print(products_DataSet['VALUE'][60])
# print(products_DataSet['VALUE'][61])
# print(products_DataSet['VALUE'][62])
productInstance_DataSet = pd.read_csv('Data set/PRODUCTINSTANCE.csv', encoding='cp1252')

productInstance = productInstance_DataSet[['M_PRODUCT_ID',"BOOKVALUE"]].copy()
products = products_DataSet[['M_PRODUCT_ID','NAME',"VALUE"]].copy()

# products = products_DataSet[['M_PRODUCT_ID','NAME',"VALUE"]].dropna()

# products['VALUE'] = pd.to_numeric(products['VALUE'])
# cleanDataSet = products_DataSet[["NAME","VALUE"]].dropna()

print("************************************")
ls = []
for i,record in enumerate(products['NAME']):
    s1 = re.search(' . .',record)
    s2 = re.search(' .',record)
    if s1 :
        if s1.end() == len(record) and s1.start() == len(record)-4:
            # print(products.VALUE[i])
            if type(products.VALUE[i]) != type(1):
            # if products.VALUE[i].isnumeric():
                try:
                    products.VALUE[i] = pd.to_numeric(products.VALUE[i]) 
                    products.VALUE[i] /= 100000000

                except ValueError:
                    products.VALUE[i] = products.VALUE[i][:len(products.VALUE[i])-8]

            # else:
            # products.VALUE[i] = products.VALUE[i].astype('int64')
            # print(products.VALUE[i])

    elif s2 :
        if s2.end() == len(record) and s2.start() == len(record)-2:
            # print(products.VALUE[i])
            if type(products.VALUE[i]) != type(1):
            # if products.VALUE[i].isnumeric():
                try:
                    products.VALUE[i] = pd.to_numeric(products.VALUE[i]) 
                    products.VALUE[i] /= 10000

                except ValueError:
                    products.VALUE[i] = products.VALUE[i][:len(products.VALUE[i])-4]
                    products.VALUE[i] = int(products.VALUE[i])

            # else:
            # products.VALUE[i] = products.VALUE[i].astype('int64')
            # print(products.VALUE[i])

    try:
        products.VALUE[i] = pd.to_numeric(products.VALUE[i]) 

    except ValueError:
        products.VALUE[i] = products.VALUE[i][:len(products.VALUE[i])-4]
        # products.VALUE[i] = float(products.VALUE[i])
        products.VALUE[i] = pd.to_numeric(products.VALUE[i], errors='coerce') 
    
    # if type(products.VALUE[i]) == type('str'):
    #     products.drop([i])

products['VALUE'] = products['VALUE'].astype('float64')

merged = pd.merge(left=products,right=productInstance,how='inner',left_on='M_PRODUCT_ID',right_on='M_PRODUCT_ID')


# print(ls[:20])
# merged = pd.merge(left=products,right=productInstance,how='inner',left_on='M_PRODUCT_ID',right_on='M_PRODUCT_ID')

# print(len(merged))
# print(len(products_DataSet))
# print(len(productInstance))
# print(len(products_DataSet.columns))
# print(len(productInstance.columns))
# print(len(merged.columns))
# print(merged.head())

cleanData = merged[['NAME',"VALUE",'BOOKVALUE']].dropna()

X = cleanData[['VALUE','BOOKVALUE']].copy()


X_train, X_test = train_test_split(X,test_size=0.3,shuffle=True,random_state=40)
 # type: ignore
X_train_np = X_train.to_numpy()
 # type: ignore
X_test_np = X_test.to_numpy()
 # type: ignore

standard = StandardScaler().fit(X_train_np)
train = standard.fit_transform(X_train_np)

# print(type(train))
 # type: ignore
# print(train.shape)
# for i in range(100):
#     print(train[i])

print('eps=0.005,min_samples=7')
dbscan = DBSCAN(eps=0.005,min_samples=7).fit(train)
labels = dbscan.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)
print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)


clusters = visualize(dbscan , labels , train, n_clusters_)
# print(f"Homogeneity: {metrics.homogeneity_score(labels_true, labels):.3f}")
# print(f"Completeness: {metrics.completeness_score(labels_true, labels):.3f}")
# print(f"V-measure: {metrics.v_measure_score(labels_true, labels):.3f}")
# print(f"Adjusted Rand Index: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
# print(
#     "Adjusted Mutual Information:"
#     f" {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}"
# )
print('evaluating...')
print(f"Silhouette Coefficient: {metrics.silhouette_score(train, labels):.3f}")

# print(len(cleanData))
# print(cleanData.head())
# print(type(cleanDataSet['VALUE'][0]))

# print(products_DataSet['VALUE'][60])
# print(products_DataSet['VALUE'][61])
# print(products_DataSet['VALUE'][62])
# a = 'hell0 . .'

# s = re.search(' . .' , a)

# print(s.span())

# if s.end() == len(a) and s.start() == len(a)-4:
#     print('kkkk')


# print(clusters)


real_clusters = {}
boundary = {}
price = {}
# print(cleanData.VALUE)
for key in clusters.keys():
    c = clusters.get(key)

    real_c = standard.inverse_transform(c)

    real_clusters[key] = real_c

    if key == -1:
        continue

    max = np.max(real_c)
    min = np.min(real_c)
    # print(type(max),max.shape)

    boundary[key] = (min,max)
    # print(cleanData.VALUE)
    record = cleanData[(cleanData.VALUE >= min) & (cleanData.VALUE <= max)]

    prices = record['BOOKVALUE']

    prices_np = prices.to_numpy()

    price[key] = np.mean(prices_np)

    print(key,price[key],len(real_clusters[key]))


# standard = StandardScaler().fit(X_test_np)
# test = standard.fit_transform(X_test_np)

# dbscan2 = dbscan.fit_predict(test)
# print(dbscan2)

# labels2 = dbscan2.labels_

# n_clusters_2 = len(set(labels)) - (1 if -1 in labels else 0)
# clusters2 = visualize(dbscan2 , labels2 , test, n_clusters_2)

maxBoundary = len(X_test_np)
index = []
for i in range(10):
    index.append(random_int(0,maxBoundary))



for i in index:
    flag=0
    itemValue = X_test_np[i][0]
    itemRealPrice = X_test_np[i][1]
    for key in real_clusters:
        if key == -1:
            continue
           
        min = boundary[key][0]
        max = boundary[key][1]

        if (itemValue >= min) and (itemValue <= max):
            print(f'value=<{itemValue}> price=<{itemRealPrice:.2f}> estimated price= {price[key]:.2f}')
            flag=1
            break

    if flag == 0:
        print("my model detects this data as noise, so it cant predict its price")


 







