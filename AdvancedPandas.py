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
print('the amount of studends is: {0}'.format(
    students_data_df.groupby('parental level of education').count()['gender']['high school']))


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
completed_stud = students_data_df[students_data_df['test preparation course'] == 'completed']
group = completed_stud['race/ethnicity'].value_counts().head(1)
print("The group with the most students that finish pre-course:", group.index.values.tolist()[0])

# Part B - Query 3
average_group = students_data_df.groupby('race/ethnicity').mean()['math score']
print(average_group)
average_group.plot(kind="bar", color='b')
plt.grid()
plt.ylabel('Average number')
plt.title("Average math score per each group")
plt.show()


# Part B - Query 5
average_gender = students_data_df.groupby('gender').mean()
print(average_gender)


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

# Part C question 2
items = ['A', 'B', 'C', 'D', 'E']
df = pd.DataFrame(columns=['id', 'item'])
df['id'] = random.sample(range(0, 100), 100)
df['item'] = df['item'].apply(lambda x: random.choice(items))

print(df.head())

item_count = df['item'].value_counts()
print(item_count)
print("Do we have all the groups in the data frame? ", set(item_count.index.values) == set(items))

# Part C question 3
groups_df = pd.get_dummies(df, columns=["item"])
print(groups_df.head())  # TODO: check if need to remove the print

# Part C question 4 - adding new column fo distance
groups_df["distance"] = groups_df.values.tolist()
groups_df["distance"] = groups_df["distance"].apply(lambda row: distance([0,1,0,0,0],row[1:6]))

print(groups_df.head())

# Part C question 5
groups_df.groupby("distance")


groups_df.groupby("new column").min()
# Part C question 6


