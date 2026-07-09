import pandas as pd

df = pd.read_excel("employees.xlsx")

print(df)

#Display First and Last Rows

print(df.head())
print(df.tail())

#Display Specific Columns

print(df["Name"])

print(df[["Name", "Age"]])

#Select row

print(df.iloc[0])

print(df.iloc[1:4])

print(df.loc[0])

#Get Information

print(df.info())

print(df.describe())

print(df.shape)

print(df.columns)

print(df.dtypes)

# Filter Data

result = df[df["Age"] > 25]

print(result)

#multiple condition 
result = df[(df["Age"] > 25) & (df["City"] == "Pune")]

print(result)

#Add new column

df["Salary"] = [50000, 60000, 70000]

print(df)

