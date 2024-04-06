import pandas as pd

# Read the json data into a pandas dataframe
# The "meteors-data.json file is in the same working directory"
df = pd.read_json("meteors-data.json")

# How many entries are in the dataset?
# ---------------------------------------------------------
# Get dataframe length
num_entries = len(df)
print("Number of entries in the dataset:", num_entries)

# What is the name and mass of the most massive meteorite in this dataset?
most_massive_meteor = df.loc[df['mass'] == df['mass'].max()]
most_massive_meteor_name = most_massive_meteor.iloc[0]['name']
most_massive_meteor_mass = most_massive_meteor.iloc[0]['mass']
print("Name of the most massive meteorite:", most_massive_meteor_name)
print("Mass of the most massive meteorite:", most_massive_meteor_mass)

# What is the most frequent year in this dataset?
most_frequent_year = df['year'].mode()[0]
print("Most frequent year in the dataset:", most_frequent_year)

