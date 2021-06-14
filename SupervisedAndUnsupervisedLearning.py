import pandas as pd
import matplotlib.pyplot as plt
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
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Student 1 - Laly Datsyuk
# Student 2 - Maya Nurani

# Part A ex. 1 - Reading file content to data frame
try:
    sympthoms_df = pd.read_csv('diabetes_sympthoms.csv')
except:
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

# Part A ex. 5
women_bp = sympthoms_df.where(sympthoms_df["Pregnancies"] > 0)["BloodPressure"]
men_bp = sympthoms_df.where(sympthoms_df["Pregnancies"] == 0)["BloodPressure"]
women_bp.hist()
men_bp.hist()
plt.title('Blood Pressure distribution by gender')
plt.show()

# Part A ex. 6
print("Age group with highest average of glucose in patients is:", sympthoms_df.groupby('AgeCategory').mean()['Glucose'].idxmax())

# Part A ex. 7
print("Insulin level average at women that had up to 8 pregnancies is",
      sympthoms_df.where(sympthoms_df["Pregnancies"] > 8)["Insulin"].mean())

# Part A ex. 8
# A graph that shows the average diabetes level by age group. we can see that it's not so different from group to group
dl_graph = sympthoms_df.groupby('AgeCategory').mean()['DiabetesLevel']
dl_graph.plot.bar()
plt.title('Average diabetes level by age group')
plt.grid()
plt.show()

# Part A ex. 9

sympthoms_df.plot.scatter(x="Glucose", y="BloodPressure")
plt.title('Blood Pressure by glucose')
plt.grid()
plt.show()

# Part B ex. 1
if (sympthoms_df.isnull().values.any()):
    mean_columns = list(sympthoms_df.describe().columns)
    for col in mean_columns:  # Adding mean value only for numeric columns
        sympthoms_df.loc[sympthoms_df[col].isna(), col] = sympthoms_df[col].mean()
else:
    print('There is no empty values in this dataframe')

# Part B ex. 2 one hot vector
sympthoms_df = pd.get_dummies(sympthoms_df)

# Part B ex. 3
old_sympthoms_df = sympthoms_df.copy()

scaler = MinMaxScaler()
normalize_data = pd.DataFrame(scaler.fit_transform(old_sympthoms_df), columns=sympthoms_df.columns)


# Part B ex. 4

def run_kmeans(df):
    # part B section 4
    measures = {
        "K": range(2, 16),
        "SSE": []
    }

    for k in measures["K"]:
        kmeans = KMeans(n_clusters=k, init="k-means++")
        kmeans.fit(df)
        measures["SSE"].append(kmeans.inertia_)

    measures = pd.DataFrame(measures)
    measures.set_index("K", inplace=True)

    # part B section 5
    measures.plot()
    plt.show()
    # For old_sympthoms_df, the best K is 5
    # For normalize_data, the best K is between 2 to 4 (better to take k=4 to reduce overfitting)
    print("silhouette_score = ", silhouette_score(df, kmeans.labels_))

    # part B section 6
    df.describe().plot()
    plt.show()



print("Part B for the old (origin) data frame")
run_kmeans(old_sympthoms_df)

print("Part B for the new (normalize) data frame")
run_kmeans(normalize_data)



# Part C ex. 1
diabetic = sympthoms_df.where(sympthoms_df["Outcome"] == 1)['Outcome'].count()
print("Percent of diabetic patients:", diabetic / sympthoms_df.shape[0])

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
    print("Confusion matrix:", metrics.confusion_matrix(y_test, y_predict, labels=[1, 0]))


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
importance_df = pd.DataFrame({'Feature':x_train.columns, 'Importance':forest.feature_importances_})
importance_df = importance_df.sort_values(by=['Importance'])
print('Feature importance from the lowest to the highest:', importance_df)
print('The most important feature is:', importance_df['Feature'].tail(1))
print('The less important feature is:', importance_df['Feature'].head(1))
