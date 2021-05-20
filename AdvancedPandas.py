import pandas as pd
import numpy as np

# not necessary
try:
    students_data_df = pd.read_csv('students.csv')
except:
    print("Failed to read the file")
    students_data_df = []  # In case the file is not read

# Part A - question 1
print("There are", students_data_df.shape[0], "rows and", students_data_df.shape[1], "columns in this file.")
print("Columns names are: ", list(students_data_df.columns))
print(students_data_df.describe())


# Part B - Query 1


def reduce_average_and_std_from_score(columns):
    for col in columns:
        m = students_data_df[col].mean()
        s = students_data_df[col].std()
        print('m=', m, "s=", s)
        # students_data_df[col] = students_data_df[col].apply(lambda grade: (grade - m) / s)   #Another way of calculation
        students_data_df[col] = (students_data_df[col] - m) / s


column_names = ["math score", "reading score", "writing score"]
reduce_average_and_std_from_score(column_names)

# TODO: remove this print before submission
print(students_data_df[column_names].head())

# Part B - Query 2



# Part B - Query 3


# Part C Q1

def distance(lst1, lst2):
    arr1 = np.array(lst1)
    arr2 = np.array(lst2)
    dist = np.linalg.norm(arr1 - arr2)
    return dist

# TODO: check if need to remove lists and print at the end
lst1 = [2, 4, 6]
lst2 = [1, 2, 3]
print(distance(lst1, lst2))
