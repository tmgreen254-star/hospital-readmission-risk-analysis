import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\tmgre\Downloads\diabetes+130-us+hospitals+for+years+1999-2008\diabetic_data.csv")

print("Dataset shape:", df.shape)
print(df.head())

# Check readmission categories
print(df["readmitted"].value_counts())

# Replace missing values marked as ?
df = df.replace("?", pd.NA)

# Create binary readmission variable
# 0 = not readmitted
# 1 = readmitted
df["readmitted_binary"] = df["readmitted"].apply(lambda x: 0 if x == "NO" else 1)

# Overall readmission rate
readmission_rate = df["readmitted_binary"].mean()

print("Overall readmission rate:", round(readmission_rate * 100, 2), "%")

# Plot 1: readmission outcomes
df["readmitted"].value_counts().plot(kind="bar", figsize=(8,5))

plt.title("Hospital Readmission Outcomes")
plt.xlabel("Readmission Category")
plt.ylabel("Number of Encounters")

plt.tight_layout()
plt.savefig("readmission_outcomes.png")
plt.show()

# Plot 2: readmission rate by age group
age_readmission = df.groupby("age")["readmitted_binary"].mean().sort_index()

age_readmission.plot(kind="bar", figsize=(10,5))

plt.title("Readmission Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Readmission Rate")

plt.tight_layout()
plt.savefig("readmission_by_age.png")
plt.show()

# Plot 3: readmission rate by hospital stay length
time_readmission = df.groupby("time_in_hospital")["readmitted_binary"].mean()

time_readmission.plot(kind="line", marker="o", figsize=(10,5))

plt.title("Readmission Rate by Time in Hospital")
plt.xlabel("Time in Hospital (Days)")
plt.ylabel("Readmission Rate")

plt.tight_layout()
plt.savefig("readmission_by_time_in_hospital.png")
plt.show()

# Plot 4: readmission rate by number of medications
med_readmission = df.groupby("num_medications")["readmitted_binary"].mean()

med_readmission.plot(kind="line", figsize=(10,5))

plt.title("Readmission Rate by Number of Medications")
plt.xlabel("Number of Medications")
plt.ylabel("Readmission Rate")

plt.tight_layout()
plt.savefig("readmission_by_medications.png")
plt.show()

# Summary table
summary = df.groupby("age")["readmitted_binary"].agg(["count", "mean"])

summary["mean"] = summary["mean"].round(3)

print("\nReadmission Summary by Age:")
print(summary)
