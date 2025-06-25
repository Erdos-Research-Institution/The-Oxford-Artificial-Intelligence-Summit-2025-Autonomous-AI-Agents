"""
Data Science Libraries Tutorial
Subtopics:
- Pandas
- Numpy
- Matplotlib
- Scikit-learn
"""

# Pandas
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("Pandas DataFrame:")
print(df)

# Numpy
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", arr)
print("Array mean:", np.mean(arr))

# Matplotlib
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Simple Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Scikit-learn
from sklearn.linear_model import LinearRegression
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
model = LinearRegression()
model.fit(X, y)
print("Predicted value for 5:", model.predict([[5]]))

# Plotting the regression result
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.scatter([5], model.predict([[5]]), color='green', label='Prediction for 5')
plt.title("Linear Regression Fit")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
