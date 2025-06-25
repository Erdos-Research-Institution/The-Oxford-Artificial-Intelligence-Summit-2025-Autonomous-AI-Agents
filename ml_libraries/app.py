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

st.header("Pandas DataFrame Example")
num_records = st.slider("Number of records", min_value=1, max_value=10, value=3)
names = [f"Person {i+1}" for i in range(num_records)]
ages = [st.number_input(f"Age for {names[i]}", min_value=0, max_value=120, value=25 + i*5, key=f"age_{i}") for i in range(num_records)]
data = {'Name': names, 'Age': ages}
df = pd.DataFrame(data)
st.write(df)

st.header("Numpy Array Example")
arr = np.array([[1, 2, 3], [4, 5, 6]])
st.write(arr)

st.header("Matplotlib Plot Example")
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Sine Wave")
st.pyplot(fig)

st.header("Scikit-learn: Linear Regression")
X = np.random.rand(100, 1) * 10
y = 2.5 * X.flatten() + np.random.randn(100) * 2
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
st.write(f"Mean Squared Error: {mse:.2f}")
st.write(f"R^2 Score: {r2:.2f}")
fig2, ax2 = plt.subplots()
ax2.scatter(X_test, y_test, color='blue', label='Actual')
ax2.plot(X_test, y_pred, color='red', label='Predicted')
ax2.set_title("Linear Regression Fit")
ax2.legend()
st.pyplot(fig2)
