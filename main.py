import streamlit as st
# Title and subtitle code
st.markdown("<h1 style='text-align: center;'>Escape Zaroff's Castle</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Answer quetions to unlock the code and uncipher the code.</h3>", unsafe_allow_html=True)

# Question 1
st.header("1. What is  short and sharp as a word?")
options_1 = ['Staccato', 'Palpable', 'Extermity', 'Scruples']
answer_1 = st.radio("Staccato:", options_1)
#Question 2
st.header("2. What is a loosely curled fur made from lamb skin?")
option_2 = ['Capital','Droll','Analytical','Astrakhan']
answer_2 = st.radio("Astrakhan:", option_2)

# Add a submit_button
submit_button = st.button("Submit")
if submit_button:
    if answer_1 == "Staccato":
        st.subheader("Correct! Here is a hint, Caesar Cipher")
    elif answer_2 == "Astrakhan":
            st.subheader("Correct! decipher this code, abzivlml")
    elif answer_1 == "Staccato" and answer_2 == "Astrakhan":
        st.subheader("Correct! decipher this code, abzivlml")
    else:
        st.subheader("Incorrect. try again!")

