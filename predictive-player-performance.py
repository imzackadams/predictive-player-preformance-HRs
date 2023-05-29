#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# In[2]:


# Import necessary libraries
from pybaseball import batting_stats
import pandas as pd

# Fetch batting stats data for the years 2015 to 2022
data = batting_stats(2015, 2022)

# Look at the first few rows of the DataFrame
print(data.head())


# In[3]:


# Check for missing values
print(data.isnull().sum())



# In[4]:


# Summary statistics
print(data.describe())


# In[ ]:




