# hospital-readmission-risk-analysis
Analyze hospital readmission data to identify factors associated with higher 30 day readmission risk and build a simple predictive model.
## Project Goals 
- Load and clean patient encounter data
- Explore hospital readmission outcomes
- Calculate overall readmission rates
- Compare readmission rates across age groups
- Analyze how time in hospital relates to readmission
- Create clear visualizations for healthcare analytics
  ## Dataset
This project uses a publicly available hospital readmission dataset containing patient encounter records from U.S. hospitals.
The dataset includes variables such as:
- Age group
- Time in hospital
- Number of lab procedures
- Number of medications
- Diagnosis information
- Readmission outcome
The main outcome variable is `readmitted`, which basically indicates whether a patient was readmitted after a hospital encounter.
## Methods
The analysis includes:
- Data loading with Pandas
- Replacement of missing values marked as `?`
- Creation of a binary readmission variable
- Calculation of overall readmission rate
- Grouped analysis by age group
- Grouped analysis by time in hospital
- Data visualization using Matplotlib
## Tools Used
- Python
- Pandas
- Matplotlib
## Visualizations
### Hospital Readmission Outcomes
### Readmission Rate by Age Group
### Readmission Rate by Time in Hospital
## Key Observations
This project explores whether readmission patterns vary by patient age and hospital stay length. The visualizations help show how readmission rates differ across patient groups and provide a starting point for thinking about hospital quality, patient risk, and healthcare resource use.
## Any Future Improvements
- Add diagnosis level analysis
- Compare readmission rates by number of medications
- Build a simple logistic regression model
- Evaluate model accuracy and feature importance
- Create a dashboard style summary of patient risk factors
