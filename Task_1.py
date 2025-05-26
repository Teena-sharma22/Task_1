##  Data Cleaning and Preprocessing

import numpy as np
import pandas as pd

# Load dataset
data = pd.read_csv('Medical Appointment No Shows.csv')
print(data.head())
print(data.tail())
print(data.info()) 

# Rename column headers to be clean and uniform
data.columns = [col.strip().lower().replace('-','_') for col in data.columns]

data.rename(columns={'hipertension':'hypertension','handcap':'handicap'},inplace=True)
print("correct columns names are :",data.columns)

# Check and handle null values
print("null values in each column is :",data.isnull().sum())
data['age'].fillna(data['age'].mean(),inplace=True)

# Remove duplicates rows
data.drop_duplicates(inplace=True)

# Standardize Text Values
data['gender'] = data['gender'].str.upper().map({'F':0,'M':1})
data['no_show'] = data['no_show'].map({'No':0,'Yes':1})

# Convert data column 
data['scheduledday'] = pd.to_datetime(data['scheduledday'])
data['appointmentday'] = pd.to_datetime(data['appointmentday'])
data['handicap'] = data['handicap'].apply(lambda x: 1 if x > 0 else 0)

# Add New Column 
data['waiting_days'] = (data['appointmentday'] - data['scheduledday']).dt.days
data = data[data['waiting_days'] >= 0]

# Remove weird ages (invalid)
data = data[(data['age'] >= 0) & (data['age'] <= 115)]

# Remove column which is not used for analysis
data.drop(columns=['patientid', 'appointmentid'],axis=1, inplace=True)

# save the cleaned data to a new CSV file
data.to_csv('Medical_Appointment_cleaned.csv', index=False)
