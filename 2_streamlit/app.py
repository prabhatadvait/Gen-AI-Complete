import streamlit as st
import pandas as pd
import numpy as np


#Title of the application
st.title("Hello Streamlit")

## Display a simple text
st.write('This is simple text')

#Create a simple dataframe

df = pd.DataFrame({
    'fist column':[1,2,3,4],
    'second column':[10,20,30,40]
})

#Display the data frame
st.write("Hey, This is the dataframe.")
st.write(df)

## create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)