import pandas as pd
import re
from sklearn import metrics
from sklearn.cluster import DBSCAN,OPTICS,Birch,KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import *
import numpy as np
import matplotlib.pyplot as plt 
from functions import *
plt.style.use(plt.style.available[5])


# to ignore "DtypeWarning", generated due to reading csv files
import warnings
warnings.filterwarnings("ignore")


# Loading Data
products_DataSet = pd.read_csv('Data set/PRODUCTS.csv')

productInstance_DataSet = pd.read_csv('Data set/PRODUCTINSTANCE.csv', encoding='cp1252')

productInstance = productInstance_DataSet[['M_PRODUCT_ID',"BOOKVALUE","PRIMALVALUE"]].copy()
products = products_DataSet[['M_PRODUCT_ID','NAME',"VALUE"]].copy()


"""
part 1: # Pre-proccessing
"""
print("*****************running*******************")
ls = []
for i,record in enumerate(products['NAME']):
    s1 = re.search(' . .',record)
    s2 = re.search(' .',record)
    if s1 :
        if s1.end() == len(record) and s1.start() == len(record)-4:

            if type(products.VALUE[i]) != type(1):
                try:
                    products.VALUE[i] = pd.to_numeric(products.VALUE[i]) 
                    products.VALUE[i] /= 100000000

                except ValueError:
                    products.VALUE[i] = products.VALUE[i][:len(products.VALUE[i])-8]


    elif s2 :
        if s2.end() == len(record) and s2.start() == len(record)-2:
            if type(products.VALUE[i]) != type(1):
                try:
                    products.VALUE[i] = pd.to_numeric(products.VALUE[i]) 
                    products.VALUE[i] /= 10000

                except ValueError:
                    products.VALUE[i] = products.VALUE[i][:len(products.VALUE[i])-4]
                    products.VALUE[i] = int(products.VALUE[i])


    try:
        products.VALUE[i] = pd.to_numeric(products.VALUE[i]) 

    except ValueError:
        products.VALUE[i] = products.VALUE[i][:len(products.VALUE[i])-4]
        products.VALUE[i] = pd.to_numeric(products.VALUE[i], errors='coerce') 
    

products['VALUE'] = products['VALUE'].astype('float64')

# merge columns 
merged = pd.merge(left=products,right=productInstance,how='inner',left_on='M_PRODUCT_ID',right_on='M_PRODUCT_ID')

# remove null records
cleanData = merged[['NAME',"VALUE",'BOOKVALUE','PRIMALVALUE']].dropna()

Xc = cleanData[['VALUE','BOOKVALUE','PRIMALVALUE']].copy()

# cast data to numpy, for easier use in libraries
X = Xc.to_numpy()

# split data to train & test segments. about 30% of data remain for test.
X_train_np, X_test_np = train_test_split(X,test_size=0.3,shuffle=True,random_state=40)


# rescaling, using simple min & max method, which transform data to range [0,1]
standard = MinMaxScaler().fit(X)
train = standard.transform(X_train_np)
test = standard.transform(X_test_np)


"""
part 2: clustering model
"""
# Instantiate the clustering model
model = KMeans()

# elbow method to find best "k" for K-means clustring
# n_clusters = elbow(model,(30,70),train)
# print(n_clusters)

# 48 is a good practical 'k', obtained by running elbow method on train data
model.n_clusters = 48

# fit K-means method
kmeans = model.fit(train)
train_labels = kmeans.labels_

figure = plt.figure(figsize=(9,7))
plt.title("Train Result")
plt.scatter(train[:,0],train[:,1],c=kmeans.labels_, s=180)
plt.show()

# select 10 random record from test data
maxBoundary = len(test)
index = []
test_ls = []
for i in range(10):
    ind = random_int(0,maxBoundary)
    test_ls.append(test[ind])
    index.append(ind)
test_ls = np.asarray(test_ls)

# predict test data.
predictions = kmeans.predict(test)

# print labels for selected records
print(f"selected data indexes: {index}")
print(f"labels: {predictions[index]}")


plt.scatter(test[:, 0], test[:, 1], c=predictions,s=180)
plt.title("Test Predictions")
plt.show()

print(f"Silhouette Coefficient (train): {metrics.silhouette_score(train, train_labels):.3f}")
print(f"Silhouette Coefficient (test): {metrics.silhouette_score(test, predictions):.3f}")

plt.scatter(test[index, 0], test[index, 1], c=predictions[index],s=250)
plt.title("Selected Points")
plt.show()


"""
part 3: regression model for price estimation
"""
# select a random record from test data
maxBoundary = len(test)
test_record_ind = random_int(0,maxBoundary)
# check label
TRI_lbl = predictions[test_record_ind]

# generate the cluster which test record belongs to, from train data.
cluster_index = []
for i,lbl in enumerate(train_labels):
    if lbl == TRI_lbl:
        cluster_index.append(i)
print(len(cluster_index))

# select regression parameters
x1 = X_train_np[cluster_index,1]
y1 = X_train_np[cluster_index,2]

# plot cluster
plt.axline((0, 0), slope=1, color="red", linestyle=(0, (5, 5)))
plt.xlabel('PRIMALVALUE')
plt.ylabel('BOOKVALUE')
plt.scatter(x1,y1)
ax = plt.gca()
ax.grid(True)
plt.show()


from sklearn import linear_model

x1r = x1.reshape((-1,1))

# regression model
regressor = linear_model.LinearRegression(positive=True)
regressor.fit(x1r,y1)
print("Coefficients: \n    ", regressor.coef_)


# estimate price for selected test data
x2 = X_test_np[test_record_ind,1]
y2 = regressor.predict(np.reshape(x2,(1,-1)))

print("the predicted price is: ",y2)
