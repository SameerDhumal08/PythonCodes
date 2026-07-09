import pandas as pd

data = {
    "Name": ["Sameer", "Rahul", "Amit"],
    "Age": [25, 28, 30],
    "City": ["Mumbai", "Pune", "Nashik"]
}

df = pd.DataFrame(data)

print(df)
