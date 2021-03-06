import random as random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Student 1 - Laly Datsyuk
# Student 2 - Maya Nurani

# Reading file content to data frame
try:
    students_data_df = pd.read_csv('students.csv')
except:
    print("Failed to read the file")
    students_data_df = []  # In case the file is not read

# Part A ex. 1
print("There are", students_data_df.shape[0], "rows and", students_data_df.shape[1], "columns in this file.")
print("Columns names are: ", list(students_data_df.columns))
print(students_data_df.describe())

# Part A ex. 2
students_data_df["race/ethnicity"].value_counts().plot(kind="bar", color='r')
plt.grid()
plt.title("Group value amount")
plt.show()

# Part A ex. 3
total_students = int(len(students_data_df.axes[0]))
print('the percent of highschool students is: {0}'.format(
    students_data_df.groupby('parental level of education').count()['gender']['high school'] / total_students))

# Part A ex. 4
# The function 'isnull' checks if theres an empty or NaN value in the given dataframe
if not (students_data_df.isnull().values.any()):
    print('There is no empty values in this dataframe')
else:
    null_columns = students_data_df.isnull().sum()
    print("columns with null values are:\n", null_columns[null_columns > 0])

# Part A ex. 5
students_data_df = pd.get_dummies(students_data_df, columns=['gender'])

# Part A ex. 6
print('Males amount: {0}, Females amount: {1}'.format(students_data_df['gender_male'].sum(), students_data_df['gender_female'].sum()))

# Part A ex. 7
students_data_df = students_data_df.rename(columns={"race/ethnicity": "ethnicity"})


# Part A ex. 8
# a function that returns the last chart of a string
def get_last_char(string):
    string = string[-1]
    return string


# Part A ex. 9
students_data_df['ethnicity'] = students_data_df['ethnicity'].apply(lambda x: get_last_char(x))

# Part A ex. 10
students_data_df["test preparation course"] = students_data_df["test preparation course"].replace \
    ({'completed': 1, 'none': 0})

# Part A ex. 11 makes 'lunch' binaric: standart = 0, free/reduced = 1
students_data_df["lunch"] = pd.get_dummies(students_data_df['lunch'], prefix='lunch')

# Part A ex. 12
students_data_df["parental level of education"] = students_data_df["parental level of education"].replace(
    to_replace={"master's degree", "bachelor's degree", "some college"}, value="higher education", regex=True)
students_data_df["parental level of education"] = students_data_df["parental level of education"].replace(
    to_replace={"associate's degree"}, value="degree", regex=True)
students_data_df["parental level of education"] = students_data_df["parental level of education"].replace(
    to_replace={"some high school"}, value="high school", regex=True)

# Part A ex. 13
ethnicity_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
students_data_df["ethnicity"] = students_data_df["ethnicity"].map(ethnicity_dict)


# Part B ex. 1
# a new dataframe that will include the normalized grades (in order to keep the old dataframe for next graphs)
normalized_grades = students_data_df[["math score", "reading score", "writing score"]].copy()

def reduce_average_and_std_from_score(columns):
    for col in columns:
        m = students_data_df[col].mean()
        s = students_data_df[col].std()
        normalized_grades[col] = (students_data_df[col] - m) / s


column_names = ["math score", "reading score", "writing score"]
reduce_average_and_std_from_score(column_names)

# Part B ex. 2
completed_stud = students_data_df[students_data_df['test preparation course'] == 1]
group = completed_stud['ethnicity'].value_counts().head(1)
print("The group with the most students that finish pre-course:", group.index.values.tolist()[0])

# Part B ex. 3
average_group = students_data_df.groupby('ethnicity').mean()['math score']
average_group.plot(kind="bar", color='b')
plt.grid()
plt.ylabel('Average number')
plt.title("Average math score per each group")
plt.show()

# Part B ex. 4
normalized_grades.hist()
plt.show()
# the graph shows us the distribution of the normalized grades at each subject (grade/amount of students that have it)

# Part B ex. 5
df_female_grades = students_data_df.where(students_data_df['gender_female']==1)[["math score", "reading score", "writing score"]]
df_female_grades = df_female_grades.dropna() #removing NaN values (male values)
df_female_grades = df_female_grades.mean()
df_male_grades = students_data_df.where(students_data_df['gender_female']==0)[["math score", "reading score", "writing score"]]
df_male_grades = df_male_grades.dropna() #removing NaN values (female values)
df_male_grades = df_male_grades.mean()
df_female_grades.plot(kind="pie", subplots=True)
plt.title("Female grades average")
plt.ylabel("")
plt.show()
df_male_grades.plot(kind="pie", subplots=True)
plt.title("Male grades average")
plt.ylabel("")
plt.show()

# Part C ex. 1


def distance(lst1, lst2):
    arr1 = np.array(lst1)
    arr2 = np.array(lst2)
    dist = np.linalg.norm(arr1 - arr2)
    return dist

# Part C ex. 2
items = ['A', 'B', 'C', 'D', 'E']
df = pd.DataFrame(columns=['id', 'item'])
df['id'] = random.sample(range(0, 100), 100)
df['item'] = df['item'].apply(lambda x: random.choice(items))

print(df.head())

item_count = df['item'].value_counts()
print(item_count)
print("Do we have all the groups in the data frame? ", set(item_count.index.values) == set(items))

# Part C ex. 3
groups_df = pd.get_dummies(df, columns=["item"])

# Part C ex. 4 - adding new column fo distance
groups_df["distance"] = groups_df.values.tolist()
groups_df["distance"] = groups_df["distance"].apply(lambda row: distance([0, 1, 0, 0, 0], row[1:6]))

print(groups_df.head())

# Part C ex. 5
group_by_distance = groups_df.groupby('distance')
# Those rows values are the same like this list [0, 1, 0, 0, 0]
print(group_by_distance.get_group(0))

# Part C ex. 6
# Explanation: if the row content list is not the same as this list [0, 1, 0, 0, 0], then all the other rows will have the same distance from this list.
# Because it doesn't meter where the number 1 is placed on the list, when it calculating in the distance format it will be the same result
# (The formula based on sum of a few numbers, we can switch the location of each number in when sumerized them - and get always the same result).
if (groups_df["distance"].max() != 0):
    print(groups_df["distance"].max())


