# Splitting the dataset into train, validation, and test sets

import os
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

# Load the dataset
data = pd.read_csv('data.csv')
# Split the dataset into train, validation, and test sets
train_data, temp_data = train_test_split(data, test_size=0.4, random_state=42)
val_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)
# Save the datasets to CSV files
train_data.to_csv('train_data.csv', index=False)
val_data.to_csv('val_data.csv', index=False)
test_data.to_csv('test_data.csv', index=False)
# Check if the files are created
if os.path.exists('data_work/train_data.csv'):
    print("Train data file created successfully.")
if os.path.exists('data_work/val_data.csv'):
    print("Validation data file created successfully.")
if os.path.exists('data_work/test_data.csv'):
    print("Test data file created successfully.")       

