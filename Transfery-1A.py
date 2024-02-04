#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np


# In[7]:


# open file
df = pd.read_csv("C:/Users/Admin/OneDrive/Desktop/transfery.csv")

df.head()


# In[41]:


#check data types
df.dtypes


# In[8]:


# clean data (drop NaN values)
df = df.dropna(subset=['clinical_gravidity'])


# In[32]:


# delete data where 'vek_mother' is 'x'
indexAge = df[(df['vek_mother'] == 'x')].index
df.drop(indexAge, inplace=True)


# In[ ]:


# change data types
df['vek_mother'] = pd.to_numeric(df['vek_mother'])
df['clinical_gravidity'] = pd.to_numeric(df['clinical_gravidity'])


# In[34]:


df.count()


# In[43]:


conditions = [
    (df['vek_mother'] <= 29),
    (df['vek_mother'] >= 30) & (df['vek_mother'] <= 34),
    (df['vek_mother'] >= 35) & (df['vek_mother'] <= 39),
    (df['vek_mother'] >= 40)
    ]

values = ['do 29', '30-34', '35-39', '40 a výše']

df['age_category'] = np.select(conditions, values)

df.head(100)


# In[123]:


age_category_do29 = df[df['age_category'] == 'do 29'].count()
age_category_do29_1 = df[(df['age_category'] == 'do 29') & (df['clinical_gravidity'] == 1)].count()
#age_category_do29.head()  

results_for_29 = ((age_category_do29_1['vek_mother'] * 100) / (age_category_do29['vek_mother'])).round(2)
print(results_for_29)


# In[126]:


age_category_30_34 = df[df['age_category'] == '30-34'].count()
age_category_30_34_1 = df[(df['age_category'] == '30-34') & (df['clinical_gravidity'] == 1)].count()
#age_category_30_34_1.head()

results_for_30_34 = ((age_category_30_34_1['vek_mother'] * 100) / (age_category_30_34['vek_mother'])).round(2)
print(results_for_30_34)


# In[129]:


age_category_35_39 = df[df['age_category'] == '35-39'].count()
age_category_35_39_1 = df[(df['age_category'] == '35-39') & (df['clinical_gravidity'] == 1)].count()
#age_category_35_39_1.head()

results_for_35_39 = ((age_category_35_39_1['vek_mother'] * 100) / (age_category_35_39['vek_mother'])).round(2)
print(results_for_35_39)


# In[131]:


age_category_40 = df[df['age_category'] == '40 a výše'].count()
age_category_40_1 = df[(df['age_category'] == '40 a výše') & (df['clinical_gravidity'] == 1)].count()
#age_category_40_1.head()

results_for_40 = ((age_category_40_1['vek_mother'] * 100) / (age_category_40['vek_mother'])).round(2)
print(results_for_40)


# In[104]:


age_all = df.count()
age_all_1 = len(df[df['clinical_gravidity']==1])
#age_all_1.head()

results_for_all = ((age_all_1 * 100) / (age_all['vek_mother'])).round(2)
print(results_for_all)


# In[114]:


df2 = pd.DataFrame(columns=['All age categories', 'Until the age of 29', '30-34', '35-39', '40 and more' ])
df2['All age categories'] = [results_for_all]
df2['Until the age of 29'] = [results_for_29]
df2['30-34'] = [results_for_30_34]
df2['35-39'] = [results_for_35_39]
df2['40 and more'] = [results_for_40]
df2


# In[115]:


df2.to_csv('1Results.csv', sep=',', index=False, encoding='utf-8')


# In[ ]:




