import pandas as pd
from sklearn.linear_model import LinearRegression

# Load cleaned data
df_filtered = pd.read_csv('nfl_wide_receivers_cleaned.csv')

# Define the features (Targets, Receptions) and target variable (Receiving Yards)
X = df_filtered[['Tgt', 'Rec']]
y = df_filtered['Yds']

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Add predictions to the dataframe for all players
df_filtered['Predicted_Yds'] = model.predict(df_filtered[['Tgt', 'Rec']])

# Sort by predicted receiving yards
top_receivers = df_filtered[['Player', 'Predicted_Yds', 'Tgt']].sort_values(by='Predicted_Yds', ascending=False).head(10)

# Display top 10 receivers
print(top_receivers)
