import random as random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# not necessary
try:
    students_data_df = pd.read_csv('students.csv')
except:
    print("Failed to read the file")
    students_data_df = []  # In case the file is not read

# Part A ex. 1
print(students_data_df.describe())

# Part A ex. 2
students_data_df["race/ethnicity"].value_counts().plot(kind="bar", color='r')
plt.grid()
plt.title("Group value amount")
plt.show()

# Part A ex. 3
total_students = int(len(students_data_df.axes[0]))
print (total_students)
print('the percent of highschol studends is: {0}'.format(students_data_df.groupby('parental level of education').count()['gender']['high school']/total_students))

# Part A ex. 4
# The function 'isnull' checks if theres an empty or NaN value in the given dataframe
if not (students_data_df.isnull().values.any()):
    print('There is no empty values in this dataframe')

else:
    print(students_data_df.isnull().sum() > 0)

#Part A ex. 5
#TODO: check if we should rewrite the main dataframe instead of creating a new one
bin_gender_df = pd.get_dummies(students_data_df['gender'], prefix='gender')

#Part A ex. 6
print('Males amount: {0}, Females amount: {1}'.format(bin_gender_df['gender_male'].sum(), bin_gender_df['gender_female'].sum()))

#Part A ex. 7
students_data_df = students_data_df.rename(columns={"race/ethnicity": "ethnicity"})
print(students_data_df)

#Part A ex. 8
#a function that returns the last chat of a string
def get_last_char(string):
    string = string[-1]
    return string

#todo: still doesn't work
students_data_df['ethnicity'].apply(lambda x: get_last_char(x))
print(students_data_df)

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

# max_val_df = students_data_df[students_data_df['test preparation course'] == 'completed'].groupby('race/ethnicity').value_counts()
# print(max_val_df)
# max_group = max_val_df['race/ethnicity'].where[max_val_df['gender'] == max_val_df['gender'].max()]
# print("The group with the most students that finish the pre-course", max_val_df['race/ethnicity'].where(max_val_df == max_val_df['gender'].max()))


completed_stud = students_data_df[students_data_df['test preparation course'] == 'completed']
print(completed_stud.head())
max_val = completed_stud.groupby('ethnicity').count()
print("completed_stud type ", type(completed_stud))
print(max_val.nlargest(1, 'gender'))


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

# Part C question 2  > not completed
items = ['A','B','C','D','E']
df = pd.DataFrame( columns = ['id', 'item'], index=range(10))
df['id'] = range(10)
df = df['item'].apply(lambda x: random.choice(items))
print(df)
