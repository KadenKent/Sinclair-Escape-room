import streamlit as st
# Title and subtitle code
st.markdown("<h1 style='text-align: center;'>Escape Zaroff's Castle</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Answer quetions to unlock the code and uncipher the code.</h3>", unsafe_allow_html=True)
# Background color
st.markdown("""
    <style>
        /* Set the background color of the main content area */
        .css-18e3th9 {
            background-color: #87CEFA !important;  # Light Sky Blue color
        }

        /* Optionally, you can also change the background color of the sidebar */
        .css-1d391kg {
            background-color: #87CEFA !important;  # Light Sky Blue color
        }
    </style>
""", unsafe_allow_html=True)
# Question 1
st.header("1. What is  short and sharp as a word?")
options_1 = ['Staccato', 'Palpable', 'Extermity', 'Scruples']
answer_1 = st.radio("Staccato:", options_1)

# Add a submit_button
submit_button = st.button("Submit")
if submit_button:
    if answer_1 == "Staccato":
        st.subheader("Correct! Here is a hint, Caesar Cipher")
    else:
        st.subheader("Incorrect. try again!")
