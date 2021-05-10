import pandas as pd
import numpy as np

students_data_df = pd.read_csv('students.csv')

print("Size of the data frame: ", students_data_df.shape)
print("Columns names: ", list(students_data_df.columns))

print(students_data_df.describe())

