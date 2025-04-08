import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# Use only the BMI feature (feature index 2)
X = diabetes.data[:, np.newaxis, 2]

# Split data into training/testing sets
X_train = X[:-20]
X_test = X[-20:]
y_train = diabetes.target[:-20]
y_test = diabetes.target[-20:]

# Create linear regression model
model = linear_model.LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print metrics
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("Coefficient (slope):", model.coef_)
print("Intercept:", model.intercept_)
print("R² score:", r2_score(y_test, y_pred))

# Plot the results
plt.scatter(X_test, y_test, color="black", label="Actual")
plt.plot(X_test, y_pred, color="blue", linewidth=3, label="Predicted")
plt.xlabel("BMI")
plt.ylabel("Disease Progression")
plt.title("OLS Linear Regression on Diabetes Data")
plt.legend()
plt.tight_layout()
plt.savefig("plot.png")  # Save the plot
plt.show()
