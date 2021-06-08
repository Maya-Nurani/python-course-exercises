import pandas as pd

# Student 1 - Laly Datsyuk
# Student 2 - Maya Nurani

# Part A ex. 1 - Reading file content to data frame
try:
    sympthoms_df = pd.read_csv('diabetes_sympthoms.csv')
except:
    print("Failed to read the file")
    sympthoms_df = []  # In case the file is not read

# Part A ex. 2
print("There are", sympthoms_df.shape[0], "rows and", sympthoms_df.shape[1], "columns in this file.")
print("Columns names are: ", list(sympthoms_df.columns))
print(sympthoms_df.describe())


