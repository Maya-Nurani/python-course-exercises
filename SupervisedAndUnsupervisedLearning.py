import pandas as pd

# Student 1 - Laly Datsyuk
# Student 2 - Maya Nurani

# Part A ex. 1 - Reading file content to data frame
try:
    sympthoms_df = pd.read_csv('diabetes_sympthoms.csv')
except FileNotFoundError:
    print("Failed to read the file")
    sympthoms_df = []  # In case the file is not read

# Part A ex. 2
# from the df description we can see that there are 768 patients.
# one thing we can see about them is that the minimum level of their glucose is 0 and max level s 199.
# minimum diabetes level is 0.07, while maximum level is 2.42, and average level is 0.47 (much below max level).
# 34% of the patients are recognized with diabetes.
print("There are", sympthoms_df.shape[0], "rows and", sympthoms_df.shape[1], "columns in this file.")
print("Columns names are: ", list(sympthoms_df.columns))
print(sympthoms_df.describe())

# Part A ex. 3
print("The highest blood pressure within men is",
      sympthoms_df.where(sympthoms_df["Pregnancies"] == 0)["BloodPressure"].max())

# Part A ex. 4
avgWomen = sympthoms_df.where(sympthoms_df["Pregnancies"] > 0)["SkinThickness"].mean()
avgMen = sympthoms_df.where(sympthoms_df["Pregnancies"] == 0)["SkinThickness"].mean()
if avgWomen > avgMen:
    print("Women's average skin thickness is the highest")
else:
    print("Men's average skin thickness is the highest")