#!/usr/bin/env python
# coding: utf-8

# # Pedictive Analytics Lab 1 Data Normalization
# 

# Data Loading and
# Exploration
# Visualization

# In[7]:


#import the libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[8]:


os.getcwd()


# In[17]:


wine=pd.read_csv('C:\\Users\\Tressy\\Desktop\\Semester 3\\Pred Analysis\\Datasets\\wine.csv',encoding="utf8")


# In[21]:


wine.head()


# In[27]:


wine.info()


# In[25]:


#List the column names 
list(wine)


# In[26]:


type(wine)


# In[20]:


wine.describe()


# Outlier Detection

# In[47]:


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
       

