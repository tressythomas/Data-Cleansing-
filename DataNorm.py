#!/usr/bin/env python
# coding: utf-8

# # Pedictive Analytics Lab 1 Data Normalization
# 
# Data Loading and
# Exploration
# Visualization

#import the libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
os.getcwd()
wine=pd.read_csv('https://github.com/tressythomas/Data-Cleansing-/blob/master/wine.csv',encoding="utf8")
wine.head()
wine.info()
#List the column names 
list(wine)
type(wine)
wine.describe()

# Outlier Detection
col=list(wine)
type(col)
for i in col:
       Q3,Q1=np.percentile(wine[i],[75,25])
       IQ=Q3-Q1
       print(wine[i][wine[i]>((1.5*IQ)+Q3)])
       print(wine[i][wine[i]<(Q1-(1.5*IQ))])
       fig, ax = plt.subplots()
       ax.set_title('Box Plot')
       ax.boxplot(wine[i])
       plt.show()
       

