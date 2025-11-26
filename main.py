import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pickle



with open("Classifier.pkl", "rb") as file:
    model = pickle.load(file)
st.title("Credit Card Fraud Detection")
st.write("Enter the transaction details")

x = st.number_input("Enter a number", min_value=0.0, max_value=10.0, value=5.0)

if st.button("Predict"):
    st.write("Button clicked!")














# if st.button("Predict"):
#     # Prepare input as numpy array
#     input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    
#     prediction = model.predict(input_features)
    
#     # Map numeric class to species name
#     species = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    
#     st.success(f"The predicted Iris species is: {species[prediction[0]]}")








# st.title("This is a Title")
# st.header("This is a Header")
# st.subheader("This is a Subheader")

# name = st.text_input("Enter your name: ")
# st.write("Your name is:", name)


# if st.button("Click Me"):
#     st.write("Button clicked!")


