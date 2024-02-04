#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np


# In[6]:


# open file
df = pd.read_csv("C:/Users/Admin/OneDrive/Desktop/transfery.csv")

df.head()


# In[3]:


# clean data (drop NaN values)
df = df.dropna(subset=['clinical_gravidity'])


# In[13]:


# clean data (drop NaN values)
df = df.dropna(subset=['vek_embryo'])


# In[19]:


# change data types
df['f_donor'] = pd.to_numeric(df['f_donor'])
df['clinical_gravidity'] = pd.to_numeric(df['clinical_gravidity'])


# In[11]:


# delete data where 'F_donor' is 1
indexDonor = df[(df['f_donor'] == 1)].index
df.drop(indexDonor, inplace=True)


# In[21]:


# delete data where 'vek_embryo' is 'x'
indexEmbryo = df[(df['vek_embryo'] == 'x')].index
df.drop(indexEmbryo, inplace=True)


# In[22]:


# change data type of column 'vek_embryo'
df['vek_embryo'] = pd.to_numeric(df['vek_embryo'])


# In[23]:


conditions = [
    (df['vek_embryo'] <= 29),
    (df['vek_embryo'] >= 30) & (df['vek_embryo'] <= 34),
    (df['vek_embryo'] >= 35) & (df['vek_embryo'] <= 39),
    (df['vek_embryo'] >= 40)
    ]

values = ['until the age of 29', '30-34', '35-39', '40 and more']

df['age_category_embryo'] = np.select(conditions, values)

df.head(100)


# In[29]:


df.count()


# In[48]:


age_all = df.count()
age_all_1 = len(df[df['clinical_gravidity']==1])

results_for_all = ((age_all_1 * 100) / (age_all['vek_embryo'])).round(2)
print(results_for_all)


# In[51]:


age_category_29 = df[df['age_category_embryo'] == 'until the age of 29'].count()
age_category_29_1 = df[(df['age_category_embryo'] == 'until the age of 29') & (df['clinical_gravidity'] == 1)].count() 

results_for_29 = ((age_category_29_1['vek_embryo'] * 100) / (age_category_29['vek_embryo'])).round(2)
print(results_for_29)


# In[55]:


age_category_30_34 = df[df['age_category_embryo'] == '30-34'].count()
age_category_30_34_1 = df[(df['age_category_embryo'] == '30-34') & (df['clinical_gravidity'] == 1)].count()

results_for_30_34 = ((age_category_30_34_1['vek_embryo'] * 100) / (age_category_30_34['vek_embryo'])).round(2)
print(results_for_30_34)


# In[58]:


age_category_35_39 = df[df['age_category_embryo'] == '35-39'].count()
age_category_35_39_1 = df[(df['age_category_embryo'] == '35-39') & (df['clinical_gravidity'] == 1)].count()

results_for_35_39 = ((age_category_35_39_1['vek_embryo'] * 100) / (age_category_35_39['vek_embryo'])).round(2)
print(results_for_35_39)


# In[61]:


age_category_40 = df[df['age_category_embryo'] == '40 and more'].count()
age_category_40_1 = df[(df['age_category_embryo'] == '40 and more') & (df['clinical_gravidity'] == 1)].count()

results_for_40 = ((age_category_40_1['vek_embryo'] * 100) / (age_category_40['vek_embryo'])).round(2)
print(results_for_40)


# In[43]:


df3 = pd.DataFrame(columns=['All age categories', 'Until the age of 29', '30-34', '35-39', '40 and more' ])
df3['All age categories'] = [results_for_all]
df3['Until the age of 29'] = [results_for_29]
df3['30-34'] = [results_for_30_34]
df3['35-39'] = [results_for_35_39]
df3['40 and more'] = [results_for_40]
df3


# In[45]:


df3.to_csv('2Results.csv', sep=',', index=False, encoding='utf-8')


# In[ ]:




