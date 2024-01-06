#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[18]:


data=pd.read_csv("C:\\Users\\HP\\OneDrive\\test1.csv")
data


# In[21]:


print(data.shape)


# In[43]:


sns.distplot(data["title"]=="Fight Club (1999)",hist=False)


# In[48]:


print(np.mean(data["title"]=="Shawshank Redemption, The (1994)"))


# In[56]:


data=pd.read_csv("C:\\Users\\HP\\OneDrive\\test2.csv")
data


# In[57]:


print(data.shape)


# In[58]:


data.head()


# In[61]:


len(np.unique(data["userId"]))


# In[90]:


q.groupby("movieId").agg([np.mean]).count()


# In[89]:


q=data[50:].groupby(by=["rating","movieId"]).count()
q


# In[ ]:


data.groupby(by=["tag",""]).count()


# In[91]:


data=pd.read_csv("C:\\Users\\HP\\OneDrive\\test3.csv")
data


# In[94]:


data


# In[110]:


dq=data.tail(51)
dq


# In[ ]:




