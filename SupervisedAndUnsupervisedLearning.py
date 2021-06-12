import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import sklearn.metrics as metrics
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

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

# Part C ex. 1
diabetic = sympthoms_df.where(sympthoms_df["Outcome"] == 1)['Outcome'].count()
print("Percent of diabetic patients:",diabetic/sympthoms_df.shape[0])

# Part C ex. 2
def split_train_test(percent):
    sympthoms_df_shuffled = shuffle(sympthoms_df)
    x = sympthoms_df_shuffled.drop(columns=["Outcome"])
    y = sympthoms_df_shuffled["Outcome"]
    x_tr = x.iloc[:int(percent * x.shape[0])]
    y_tr = y.iloc[:int(percent * y.shape[0])]
    x_te = x.iloc[int(percent * x.shape[0]):]
    y_te = y.iloc[int(percent * y.shape[0]):]
    return x_tr, x_te, y_tr, y_te


# Part C ex. 3 - data preparation for training
x_train, x_test, y_train, y_test = split_train_test(0.75)

# Part C ex. 4 - data one hot encoding + training
x_train = pd.get_dummies(x_train)
x_test = pd.get_dummies(x_test)
tree = DecisionTreeClassifier()
tree.fit(x_train, y_train)


# Part C ex. 5 - prediction and accuracy calculation
def accuracy_cm_print():
    print("Accuracy:", metrics.accuracy_score(y_test, y_predict))
    print("Confusion matrix:", metrics.confusion_matrix(y_test, y_predict, labels=[1,0]))


y_predict = tree.predict(x_test)
accuracy_cm_print()
# from the confusion matrix we can understand how many diabetic people were recognized as diabetic (TP)
# how many of them weren't recognized (FN), how many non-diabetic were recognized as diabetic (FP)
# and how many of non-diabetic were recognized as non-diabetic (TN)
# as it seems, our algorithm didn't recognize 1/3 of the diabetic patients and 1/4 to 1/3 of the non-diabetic patients

# Part C ex. 6
forest = RandomForestClassifier(n_estimators=50)
forest.fit(x_train, y_train)

# Part C ex. 7
y_predict = forest.predict(x_test)
accuracy_cm_print()

# Part C ex. 8
#TODO: finish
print("The most important value is")