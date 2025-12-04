import streamlit as st
import pandas as pd
import numpy as np
# Ensure you have a file named 'prediction.py' with a 'predict' function
from prediction import predict 

st.title('Classifying Iris Flowers')
st.markdown('Toy model to play to classify iris flowers into \
(setosa, versicolor, virginica) based on their sepal/petal \
and length/width.')

st.header("Plant Features")
col1, col2 = st.columns(2)

with col1:
    st.text("Sepal characteristics")
    # Changed variable 'sepal_1' to 'sepal_l' to match the prediction call
    # Fixed spelling of 'lenght'
    sepal_l = st.slider('Sepal length (cm)', 1.0, 8.0, 0.5)
    sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 0.5)

with col2:
    st.text("Petal characteristics") # Fixed 'Pepal' typo
    # Changed variable 'petal_1' to 'petal_l'
    petal_l = st.slider('Petal length (cm)', 1.0, 7.0, 0.5)
    petal_w = st.slider('Petal width (cm)', 0.1, 2.5, 0.5)

st.text('')
if st.button("Predict type of Iris"):
    # Now using the correct variable names (sepal_l, petal_l)
    result = predict(
        np.array([[sepal_l, sepal_w, petal_l, petal_w]])
    )
    st.text(result[0])