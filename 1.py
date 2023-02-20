#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[10]:


df=pd.read_csv('data/iwalkFitnessDataset.csv')
df.head()


# In[11]:


df.tail()


# In[12]:


df.sample(10)


# In[13]:


df.shape


# In[14]:


df.info()


# In[23]:


df.describe()


# In[28]:


df[['weight','age','program']].sample(10)


# ### จัดการค่าซ้ำกัน

# In[29]:


df.apply(lambda x:sum(x.duplicated()))


# In[33]:


df.customer_id.duplicated()


# In[32]:


df.duplicated(subset=['customer_id','name']).sum()


# In[39]:


df=df.drop_duplicates(subset='customer_id',keep='first')


# In[40]:


df.shape


# ## จัดการกับ missing value
# 

# In[41]:


df.info()


# In[42]:


df.isnull().sum()


# In[46]:


import missingno as ms
ms.matrix(df)


# In[48]:


ms.bar(df)


# In[ ]:




