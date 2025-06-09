import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder

# Set the title of the apps
st.title("Jaya Jaya Prediction App")


df = pd.read_csv('data.csv', sep=';')


def train_model(data):
    X = data.drop('Status', axis=1)
    y = data['Status']
    
    le = LabelEncoder()
    encoded_y = le.fit_transform(y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, encoded_y, test_size=0.2, random_state=42)
    
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=le.classes_)
    
    return rf, le, accuracy, report, cm, X.columns

model, label_encoder, acc, report, cm, features = train_model(df)

user_input = {}

for feature in features :
    val = st.number_input(f"Enter value for {feature}:", value=float(df[feature].mean()), step=0.1)
    user_input[feature] = val
    
user_input_df = pd.DataFrame([user_input])

def make_prediction():
    prediction = model.predict(user_input_df)
    predicted_label = label_encoder.inverse_transform(prediction)[0]
    st.session_state.result = predicted_label

st.button("Predict", on_click=make_prediction)

if 'result' in st.session_state:
    st.success(f"Predicted Status: {st.session_state.result}")
    st.success(f"Model Accuracy: {acc:.2f}")
    del st.session_state['result']

st.subheader("Classification Report")

st.write(report)

st.subheader("Confusion Matrix")
fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
st.pyplot(fig)



