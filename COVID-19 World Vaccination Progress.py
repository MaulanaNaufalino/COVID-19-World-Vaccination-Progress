#!/usr/bin/env python
# coding: utf-8

# In[44]:


# import library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.offline as py


# In[45]:


# read the data

df_vaccinations = pd.read_csv(r"country_vaccinations.csv")


# In[46]:


# show first 10 data

df_vaccinations.head(10)


# In[49]:


# show last 10 data

df_vaccinations.tail(10)


# In[50]:


# view some basic statistical details

df_vaccinations.describe()


# In[51]:


# get a concise summary

df_vaccinations.info()


# In[52]:


# get the number of missing values

df_vaccinations.isnull().sum()


# In[53]:


# get unique values based on the date of each country

pd.to_datetime(df_vaccinations.date)
df_vaccinations.country.value_counts()


# In[54]:


# counts England, Scotland, Wales, and Northern Ireland as The United Kingdom

df_vaccinations = df_vaccinations[df_vaccinations.country.apply(lambda x: x not in ["England", "Scotland", "Wales", "Northern Ireland"])]
df_vaccinations.country.value_counts()


# In[55]:


# get unique values based on the date of each country, 
# after England, Scotland, Wales, and Northern Ireland are counted as The United Kingdom

df_vaccinations.vaccines.value_counts()


# In[56]:


# define a dataframe based on vaccines and country

df_country = df_vaccinations[["vaccines", "country"]]
df_country.head()


# In[57]:


# find out how many countries are using each vaccine based on data

dict_ = {}
for i in df_country.vaccines.unique():
  dict_[i] = [df_country["country"][j] for j in df_country[df_country["vaccines"]==i].index]

vaccines = {}
for key, value in dict_.items():
  vaccines[key] = set(value)
for i, j in vaccines.items():
  print(f"{i}:>>{j}")


# In[62]:


# visualize data to see which vaccines each country has used

vaccine_map = px.choropleth(data, locations = 'iso_code', color = 'vaccines')
vaccine_map.update_layout(height=500, margin={"r":10,"t":10,"l":10,"b":10})
vaccine_map.show()


# In[ ]:




