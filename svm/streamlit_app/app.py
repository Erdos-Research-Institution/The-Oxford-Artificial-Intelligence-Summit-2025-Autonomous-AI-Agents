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
st.write("Iris dataset shape:", X.shape)
st.write("Target classes:", np.unique(y))

st.header("Train/Test Split")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
st.write(f"Train size: {X_train.shape[0]}, Test size: {X_test.shape[0]}")

st.header("SVM Classification")
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

st.write("**Predictions on test set:**", y_pred)

st.header("Evaluation Metrics")
acc = accuracy_score(y_test, y_pred)
st.write(f"Accuracy: {acc:.2f}")
st.write("Classification Report:")
st.text(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots()
cax = ax.matshow(cm, cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
fig.colorbar(cax)
st.pyplot(fig)

st.write("**Industry Use Case:**")
st.markdown("""
SVMs are widely used in industry for classification tasks such as spam detection, image recognition, and bioinformatics. Evaluation metrics like accuracy and confusion matrix help assess model performance and reliability before deployment.
""")
