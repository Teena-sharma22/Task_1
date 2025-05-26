# task 1
📊 Medical Appointment No-Show Analysis (with Python)
This project focuses on cleaning and preprocessing the Medical Appointment No-Show dataset using Python, preparing it for further analysis and modeling.

📝 Dataset Overview
The dataset contains medical appointment records with details such as:

Patient ID, Appointment ID

Gender, Age

Scheduled Day, Appointment Day

Neighborhood

Health indicators: Hypertension, Diabetes, Alcoholism, Handicap

Scholarship status

SMS received

Whether the patient showed up or not (No-show)

🧽 Data Cleaning & Transformation
We performed the following cleaning and preprocessing steps:

🔍 Standardized and corrected column headers (lowercase, replaced hyphens, fixed typos).

❌ Removed duplicate rows to avoid redundancy.

🚫 Handled missing values by filling missing ages with the average age.

🔢 Converted categorical columns:

Gender mapped to numeric (F → 0, M → 1)

No-show mapped to numeric (No → 0, Yes → 1)

🗓️ Converted date columns (scheduledday and appointmentday) to datetime objects for accurate time handling.

➕ Added a new column waiting_days calculating days between scheduling and appointment, filtering out invalid negative values.

🚫 Removed unrealistic ages outside 0-115 years range.

🗑️ Dropped unused columns (patientid and appointmentid) to focus on analysis-relevant data.

🩺 Simplified the handicap column into a binary indicator (0 = no handicap, 1 = handicap present).

All these transformations are performed in the cleaning script Task_1.py.

⚙️ Dependencies
Python 3.x

pandas

numpy

📁 Project Files

📘 [README.md](README.md) – You are here! Project documentation and guide.

📄 [Medical Appointment No Shows.csv](Medical%20Appointment%20No%20Shows.csv) – The original unprocessed dataset.

🧹 [Task_1.py](Task_1.py) – Python script to clean and preprocess the appointment data.

📄 [Medical_Appointment_cleaned.csv](Medical_Appointment_cleaned.csv ) – Cleaned dataset for analysis and modeling.

📝 Short Summary of Changes.txt – Summary of all cleaning steps performed on the dataset.



