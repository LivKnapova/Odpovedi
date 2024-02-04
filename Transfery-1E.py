#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# open file
df = pd.read_csv("C:/Users/Admin/OneDrive/Desktop/transfery.csv")

df.head()


# In[3]:


# clean data (drop NaN values)
df = df.dropna(subset=['clinical_gravidity'])
df = df.dropna(subset=['sex'])


# In[4]:


df.head()


# In[5]:


df['clinical_gravidity'] = pd.to_numeric(df['clinical_gravidity'])


# In[6]:


count_of_all_XX = df[df['sex'] == 'XX'].count()
print(count_of_all_XX['sex'])
count_of_all_XY = df[df['sex'] == 'XY'].count()
print(count_of_all_XY['sex'])

count_of_success_XX = df[(df['sex'] == 'XX') & (df['clinical_gravidity'] == 1)].count()
print(count_of_success_XX['sex'])
count_of_success_XY = df[(df['sex'] == 'XY') & (df['clinical_gravidity'] == 1)].count()
print(count_of_success_XY['sex'])

count_of_unsuccess_XX = df[(df['sex'] == 'XX') & (df['clinical_gravidity'] == 0)].count()
print(count_of_unsuccess_XX['sex'])
count_of_unsuccess_XY = df[(df['sex'] == 'XY') & (df['clinical_gravidity'] == 0)].count()
print(count_of_unsuccess_XY['sex'])


# In[7]:


# delete data where 'XY' 
df5 = pd.DataFrame(df)
indexXY = df5[(df5['sex'] == 'XY')].index
df5.drop(indexXY, inplace=True) 


# In[8]:


df6 = pd.DataFrame(df)
indexXX = df6[(df6['sex'] == 'XX')].index
df6.drop(indexXX, inplace=True)


# In[9]:


df5.to_csv('XX.csv', sep=',', index=False, encoding='utf-8')
df6.to_csv('XY.csv', sep=',', index=False, encoding='utf-8')


# In[ ]:




