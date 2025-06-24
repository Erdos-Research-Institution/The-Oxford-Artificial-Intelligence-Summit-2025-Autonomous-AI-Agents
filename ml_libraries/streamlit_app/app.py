import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

st.title("Data Science Libraries Tutorial")
st.markdown("""
### Subtopics
- Pandas
- Numpy
- Matplotlib
- Scikit-learn
- Industry Use Case: Model Evaluation, Train/Test Split
""")

st.header("Pandas")
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
st.write("Pandas DataFrame:")
st.dataframe(df)

st.header("Numpy")
arr = np.array([1, 2, 3, 4, 5])
st.write("Numpy Array:", arr)
st.write("Array mean:", np.mean(arr))

st.header("Matplotlib")
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_title("Simple Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
st.pyplot(fig)

st.header("Scikit-learn")
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([2, 4, 6, 8, 10, 12, 14, 16])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)

st.write("**Train/Test Split Example**")
st.write(f"Train X: {X_train.flatten()}, Train y: {y_train}")
st.write(f"Test X: {X_test.flatten()}, Test y: {y_test}")
st.write(f"Predictions on test set: {pred}")

# Evaluation metrics
mse = mean_squared_error(y_test, pred)
r2 = r2_score(y_test, pred)
st.write(f"Mean Squared Error: {mse:.2f}")
st.write(f"R2 Score: {r2:.2f}")

st.write("**Industry Use Case:**")
st.markdown("""
In industry, splitting data into training and testing sets is essential for evaluating model performance. Metrics like Mean Squared Error (MSE) and R2 Score help determine how well the model predicts unseen data.
""")
