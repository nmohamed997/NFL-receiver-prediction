import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df_filtered = pd.read_csv('nfl_wide_receivers_cleaned.csv')

# Calculate descriptive statistics
desc_stats = df_filtered[['Tgt', 'Rec', 'Yds', 'TD']].describe()
print(desc_stats)

# Correlation heatmap between variables
plt.figure(figsize=(8, 6))
sns.heatmap(df_filtered[['Tgt', 'Rec', 'Yds', 'TD']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation between Targets, Receptions, Receiving Yards, and Touchdowns')
plt.show()

# Scatter plot for Targets vs Receiving Yards
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Tgt', y='Yds', data=df_filtered)
plt.title('Targets vs Receiving Yards')
plt.xlabel('Targets')
plt.ylabel('Receiving Yards')
plt.show()
