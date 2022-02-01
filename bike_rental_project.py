#!/usr/bin/env python
# coding: utf-8

# In[219]:


# import bike share data
# import libraries

df = pd.read_csv("/Users/craighammerstein/Downloads/202109-divvy-tripdata.csv")

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('load_ext', 'nb_black')


# In[220]:


# quick look at dataset

df.head()


# In[221]:


# Checking for any null values

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print("{} - {}%".format(col, pct_missing))


# In[222]:


# Checking data types for possible errors during calculations

df.dtypes


# In[223]:


#Converting the date objects to datetime64[ns]

df['started_at']=pd.to_datetime(df['started_at'])
df['ended_at']=pd.to_datetime(df['ended_at'])


# In[224]:


# New column total time cycled

df["total_time"] = df["ended_at"] - df["started_at"]


# In[225]:


# check to see that datatype was changed

df.dtypes


# In[226]:


# what are the longest rides?

df["total_time"].sort_values(ascending=False)


# In[227]:


df.head()


# In[228]:


df['total_time']=df['total_time'].astype('int64')

df['total_time']= df.total_time/(6*10**10)


# In[229]:


df.head()


# In[240]:


#plot casual vs. member and types of bikes

g=sns.catplot(x='member_casual', y='total_time', data=df, col='rideable_type')

g.fig.subplots_adjust(top=0.8)
g.fig.suptitle('Membership and bike type vs. Time ridden', fontsize=16)


# In[231]:


# see exactly how members vs. casual compare

df["member_casual"].value_counts()


# In[ ]:




