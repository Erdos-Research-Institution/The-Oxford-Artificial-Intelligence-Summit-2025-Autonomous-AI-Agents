import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

st.title("Support Vector Machines (SVM) Tutorial")
st.markdown("""
### Subtopics
- Basic ML operations
- Classification
- Evaluation
- Industry Use Case: Classification and Model Evaluation
""")

st.header("Load Dataset")
iris = datasets.load_iris()
X = iris.data
y = iris.target
st.write("Shape of features:", X.shape)
st.write("Shape of labels:", y.shape)

st.header("Train/Test Split")
test_size = st.slider("Test size (fraction)", min_value=0.1, max_value=0.5, value=0.2, step=0.05)
random_state = st.number_input("Random state", min_value=0, max_value=100, value=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
st.write(f"Train size: {X_train.shape[0]}, Test size: {X_test.shape[0]}")

st.header("SVM Classifier")
kernel = st.selectbox("Kernel", ["linear", "rbf", "poly", "sigmoid"])
C = st.slider("C (Regularization)", min_value=0.01, max_value=10.0, value=1.0)
if st.button("Train SVM"):
    clf = SVC(kernel=kernel, C=C)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    st.success(f"Accuracy: {acc:.2f}")
    st.text("Classification Report:")
    st.text(classification_report(y_test, y_pred))
    st.text("Confusion Matrix:")
    st.write(confusion_matrix(y_test, y_pred))
    # Plot
    fig, ax = plt.subplots()
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='viridis', marker='o', label='Predicted')
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='cool', marker='x', label='True')
    ax.set_xlabel(iris.feature_names[0])
    ax.set_ylabel(iris.feature_names[1])
    ax.legend(["Predicted", "True"])
    st.pyplot(fig)
