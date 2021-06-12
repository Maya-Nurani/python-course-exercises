import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

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

# Part B ex. 1
if (sympthoms_df.isnull().values.any()):
    mean_columns = list(sympthoms_df.describe().columns)
    for col in mean_columns:  # Adding mean value only for numeric columns
        sympthoms_df.loc[sympthoms_df[col].isna(), col] = sympthoms_df[col].mean()
else:
    print('There is no empty values in this dataframe')

# Part B ex. 2 one hot vector
sympthoms_df = pd.get_dummies(sympthoms_df)
print(sympthoms_df.columns)  # TODO: remove

# Part B ex. 3
old_sympthoms_df = sympthoms_df.copy()

scaler = MinMaxScaler()
normalize_data = pd.DataFrame(scaler.fit_transform(old_sympthoms_df), columns= sympthoms_df.columns)

# Part B ex. 4

measures = {
    "K": range(2,16),
    "SSE" :[]
}

def run_kmeans(df):
    for k in measures["K"]:
        kmeans = KMeans(n_clusters=k, init="K-means++")
        kmeans.fit(df)
        measures["SSE"].append(kmeans.inertia_)

run_kmeans(old_sympthoms_df)
run_kmeans(normalize_data)



