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
    st.text("Classification Report (per-class only):")
    # Remove macro avg and weighted avg from the report
    report = classification_report(y_test, y_pred, output_dict=True)
    report_str = ""
    for label in iris.target_names:
        if label in report:
            metrics = report[label]
            report_str += f"{label}: precision={metrics['precision']:.2f}, recall={metrics['recall']:.2f}, f1-score={metrics['f1-score']:.2f}\n"
    st.text(report_str)
    st.text("Confusion Matrix:")
    st.write(confusion_matrix(y_test, y_pred))
    # Plot
    fig, ax = plt.subplots()
    scatter1 = ax.scatter(X_test[:, 0], X_test[:, 1],  color='blue', marker='o', label='Predicted')
    scatter2 = ax.scatter(X_test[:, 0], X_test[:, 1],  color='red', marker='x', label='True')
    ax.set_xlabel(iris.feature_names[0])
    ax.set_ylabel(iris.feature_names[1])
    ax.legend([scatter1, scatter2], ["Predicted ", "True"])
    st.pyplot(fig)
    st.caption("In the scatter plot, color represents the class label: 'Predicted' uses predicted class, 'True' uses true class.")
