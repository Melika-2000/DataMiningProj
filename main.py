import pandas as pd

dataSet1 = pd.read_csv('Data set/INOUT.csv')
dataSet2 = pd.read_csv('Data set/INOUTLINE.csv')
dataSet3 = pd.read_csv('Data set/TRANSFER_ITEM_D.csv')
dataSet4 = pd.read_csv('Data set/TRANSFER_ITEM.csv')
dataSet5 = pd.read_csv('Data set/PRODUCTS.csv')
dataSet6 = pd.read_csv('Data set/PRODUCTINSTANCE.csv', encoding='cp1252')

dataSets = [dataSet1, dataSet2, dataSet3, dataSet4, dataSet5, dataSet6]

