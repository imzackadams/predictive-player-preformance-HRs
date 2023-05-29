#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[24]:


# Import necessary libraries
from pybaseball import batting_stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

# Fetch batting stats data for the years 2015 to 2022
data = batting_stats(2015, 2022)

# Look at the first few rows of the DataFrame
data



# In[25]:


# Check for missing values
print(data.isnull().sum())



# In[26]:


# Summary statistics
print(data.describe())


# In[27]:


# List of numerical variables
num_vars = ['G', 'AB', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO']

# List of categorical variables
cat_vars = ['Age', 'Team']


# In[28]:


print("\nDistributions of numerical variables:")
for var in num_vars:
    print(data[var].describe())


# In[29]:


print("\nCounts of categorical variables:")
for var in cat_vars:
    print(data[var].value_counts())


# In[30]:


print("\nCorrelations between numerical variables:")
corr = data[num_vars].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation matrix of numerical variables')
plt.show()


# In[31]:


# lets focus on home runs

print("\nCorrelations with HR:")
corr_with_HR = data[num_vars].corr()['HR'].sort_values(ascending=False)
print(corr_with_HR)


# In[32]:


print("\nHistogram of HR:")
sns.histplot(data['HR'], bins=30)
plt.title('Histogram of HR')
plt.show()


# In[33]:


print("\nBox plots of HR by categorical variables:")
for var in cat_vars:
    plt.figure(figsize=(10, 4))
    sns.boxplot(x=var, y='HR', data=data)
    plt.title('Box plot of HR by ' + var)
    plt.xticks(rotation=90)
    plt.show()


# In[36]:


print("\nCorrelation of new features with HR:")
new_features = ['AVG', 'SLG', 'OBP', 'ISO']
for feature in new_features:
    print(f"Correlation between HR and {feature}: {data['HR'].corr(data[feature])}")


# In[ ]:




