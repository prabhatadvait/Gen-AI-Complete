import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter Your Name:")

#slider

age = st.slider("Select Your Age:",0,100,25)

st.write(f"Your age is: {age}.")

# selectbox
options = ['Python','C++','Java','JavaScript']
choice = st.selectbox("Choose your favourite Language: ",options)
st.write(f"Your selected Language: {choice}.")

if name:
    st.write(f"Hello, {name}")

data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 22, 28],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

#file uploader
uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)