import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load cleaned data
df_filtered = pd.read_csv('nfl_wide_receivers_cleaned.csv')

# Define the features (Targets, Receptions) and target variable (Receiving Yards)
X = df_filtered[['Tgt', 'Rec']]
y = df_filtered['Yds']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the linear regression model and fit it to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Predict receiving yards on the test set
y_pred = model.predict(X_test)

# Example prediction for a player with 120 targets and 85 receptions
example_prediction = model.predict([[120, 85]])
print(f'Predicted receiving yards for a player with 120 targets and 85 receptions: {example_prediction[0]}')

# Plot the actual vs predicted values
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)
plt.title('Actual vs Predicted Receiving Yards')
plt.xlabel('Actual Receiving Yards')
plt.ylabel('Predicted Receiving Yards')
plt.show()
