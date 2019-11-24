import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel (r'/home/megakruk/workspace/PycharmProjects/PWr-SMA-Project/online_retail_II.xlsx')
print(df)
x=df.loc[:, ["InvoiceDate"]] 
y=df.loc[:,["Invoice","StockCode","Description","Quantity","Price","Country"]] 
x_train, x_test, y_train, y_test =train_test_split(x,y, test_size=1/5, random_state=0)

print (len(x_train))
print (len(y_train))

print (len(x_test))
print (len(y_test))
