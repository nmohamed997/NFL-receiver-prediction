import pandas as pd

# Load the data
df = pd.read_csv('nfl_wide_receivers_2023.csv')

# Convert 'Yds' to numeric, forcing errors to NaN
df['Yds'] = pd.to_numeric(df['Yds'], errors='coerce')

# Remove rows with missing values in 'Yds' after conversion
df_cleaned = df.dropna(subset=['Yds', 'Tgt'])

# Remove outliers using the IQR method
Q1 = df_cleaned['Yds'].quantile(0.25)
Q3 = df_cleaned['Yds'].quantile(0.75)
IQR = Q3 - Q1

# Filter out rows where receiving yards are outside the typical range
df_filtered = df_cleaned[~((df_cleaned['Yds'] < (Q1 - 1.5 * IQR)) | (df_cleaned['Yds'] > (Q3 + 1.5 * IQR)))]

# Save the cleaned data to a new CSV file
df_filtered.to_csv('nfl_wide_receivers_cleaned.csv', index=False)

# Inspect the cleaned data
print(df_filtered.head())
