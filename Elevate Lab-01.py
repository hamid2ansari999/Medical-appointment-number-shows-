#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

file_path = 'KaggleV2-May-2016.csv'
df = pd.read_csv(file_path)

print("Initial dataset shape:", df.shape)
df.head()


# In[2]:


print("\nMissing values per column:")
print(df.isnull().sum())

df_cleaned = df.dropna()
print("After dropping missing values:", df_cleaned.shape)


# In[3]:


df_cleaned = df_cleaned.drop_duplicates()
print("After removing duplicates:", df_cleaned.shape)


# In[4]:


df_cleaned['Gender'] = df_cleaned['Gender'].str.strip().str.upper()
df_cleaned['Neighbourhood'] = df_cleaned['Neighbourhood'].str.strip().str.title()


# In[5]:


df_cleaned['ScheduledDay'] = pd.to_datetime(df_cleaned['ScheduledDay'], errors='coerce')
df_cleaned['AppointmentDay'] = pd.to_datetime(df_cleaned['AppointmentDay'], errors='coerce')

df_cleaned['ScheduledDay'] = df_cleaned['ScheduledDay'].dt.strftime('%d-%m-%Y')
df_cleaned['AppointmentDay'] = df_cleaned['AppointmentDay'].dt.strftime('%d-%m-%Y')

df_cleaned[['ScheduledDay', 'AppointmentDay']].head()


# In[6]:


df_cleaned.columns = df_cleaned.columns.str.lower().str.replace(' ', '_')

print("Updated column names:", df_cleaned.columns.tolist())


# In[7]:


df_cleaned['age'] = df_cleaned['age'].astype(int, errors='ignore')

print("\nData types after conversion:")
print(df_cleaned.dtypes)


# In[8]:


# Save cleaned data
df_cleaned.to_csv('cleaned_kaggle_appointments.csv', index=False)
print("\nCleaned data saved to 'cleaned_kaggle_appointments.csv'")


# In[ ]:




