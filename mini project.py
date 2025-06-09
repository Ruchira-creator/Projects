#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import datetime
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import calendar


# In[9]:


data=pd.read_csv(r"C:\Users\ruchi\OneDrive\Desktop\Uber Drives - .csv")
data.head()


# In[59]:


data.tail()


# In[4]:


data.shape


# In[5]:


data.dtypes


# In[6]:


data.info()


# In[7]:


data.isnull().any() 


# In[8]:


data.isnull().sum()


# In[51]:


obj = (data.dtypes == 'object')
object_cols = list(obj[obj].index)
 
unique_values = {}
for col in object_cols:
  unique_values[col] = data[col].unique().size
unique_values


# In[9]:


data['PURPOSE*'].value_counts()


# In[11]:


data=data.dropna()
data.isnull().sum()


# In[12]:


data.shape


# In[20]:


data.info()


# In[22]:


data['CATEGORY*'].value_counts()


# In[56]:


plt.figure(figsize=(15, 5))
sns.countplot(data=data, x='PURPOSE*', hue='CATEGORY*')
plt.xticks(rotation=90)
plt.show()


# In[29]:


sns.countplot(x='CATEGORY*',data=data,palette='Set2')


# In[25]:


data['MILES*'].plot.hist()


# In[41]:


data['PURPOSE*'].value_counts().plot(kind='bar',figsize=(10,5),color='green')


# In[46]:


data['START*'].value_counts().plot(kind='bar',figsize=(25,10),color='blue')


# In[10]:


mean=data["MILES*"].mean(skipna=True)
print('The mean of "miles" is %.2f'%mean)


# In[11]:


median=data["MILES*"].median(skipna=True)
print('The median of "miles" is %.2f'%median)


# In[29]:


histo=data["MILES*"].hist(bins=100,density=True,stacked=True,color='red',alpha=0.9)
data["MILES*"].plot(kind='density',color='teal')
histo.set(xlabel='Miles')
plt.xlim(100,300)
plt.show()


# In[39]:


rp=data.head()
purp_data=rp["MILES*"]
cause_data=rp["CATEGORY*"]
colors=["r","g","b","black","purple"]
explode=(0.1,0,0,0,0)
plt.pie(purp_data,labels=cause_data,explode=explode,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title("SERVER DATA")
plt.show()


# In[49]:


pivottable=data.pivot_table(index='CATEGORY*',columns='PURPOSE*',values='MILES*',aggfunc='mean')
plt.figure(figsize=(10,8))
sns.heatmap(pivottable,annot=True,cmap='autumn',fmt='.2f',cbar=True)
plt.title('Analysis')
plt.show()


# In[41]:


sns.distplot(data[data['MILES*']<40]['MILES*'])


# In[42]:


sns.boxplot(data[data['MILES*']<100]['MILES*'])


# In[ ]:




