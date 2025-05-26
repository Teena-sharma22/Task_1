# Task_1

# Medical Appointment No-Show Analysis - Data Cleaning

This repository contains the data cleaning and preprocessing steps for the Medical Appointment No-Show dataset. The goal is to prepare the data for analysis and modeling by transforming raw data into a clean, structured format.

## Dataset

- Original dataset: `Medical Appointment No Shows.csv`
- Cleaned dataset output: `Medical_Appointment_cleaned.csv`

## Summary of Data Cleaning

- Renamed columns to lowercase and standardized naming conventions.
- Corrected typos in column headers.
- Filled missing values in the `age` column with the mean age.
- Removed duplicate records.
- Standardized categorical values for `gender` and `no_show`.
- Converted date columns to datetime format.
- Created a new feature `waiting_days` to capture the time between scheduling and appointment.
- Filtered out invalid ages and negative waiting days.
- Removed columns not needed for analysis (`patientid`, `appointmentid`).
- Simplified handicap to a binary indicator.

## How to Use

1. Clone the repository.
2. Run the cleaning script (`Task_1.py` or a Jupyter notebook with the cleaning code).
3. Use the cleaned CSV file (`Medical_Appointment_cleaned.csv`) for further analysis or modeling.

## Dependencies

- Python
- pandas
- numpy

