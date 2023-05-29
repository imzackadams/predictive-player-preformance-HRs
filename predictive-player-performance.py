#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[18]:


# Import necessary libraries
from pybaseball import batting_stats
import pandas as pd

pd.set_option('display.max_columns', None)

# Fetch batting stats data for the years 2015 to 2022
data = batting_stats(2015, 2022)

# Look at the first few rows of the DataFrame
data



# In[19]:


# Check for missing values
print(data.isnull().sum())



# In[20]:


# Summary statistics
print(data.describe())


# In[21]:


# List of numerical variables
num_vars = ['G', 'AB', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO']

# List of categorical variables
cat_vars = ['Age', 'Team']


# In[22]:


print("\nDistributions of numerical variables:")
for var in num_vars:
    print(data[var].describe())


# In[23]:


print("\nCounts of categorical variables:")
for var in cat_vars:
    print(data[var].value_counts())


# In[ ]:




