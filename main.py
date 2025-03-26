import streamlit as st
# Title and subtitle code
st.markdown("<h1 style='text-align: center;'>Escape Zaroff's Castle</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Answer quetions to unlock the code and uncipher the code.</h3>", unsafe_allow_html=True)

#the background story
passage = """
This is the passage that will be displayed in 11px font size.
You can add more text here, and it will still be rendered with the same font size.
"""
# Question 1
st.text("1. What is  short and sharp as a word?")
options_1 = ['Staccato', 'Palpable', 'Extermity', 'Scruples']
answer_1 = st.radio("Staccato:", options_1)
#Question 2
st.text("2. What is a loosely curled fur made from lamb skin?")
option_2 = ['Capital','Droll','Analytical','Astrakhan']
answer_2 = st.radio("Astrakhan:", option_2)
#Question 3
st.text("3. What is the author's purpose?")
option_3 = ['Entertain','Inform','Presuade','Describe']
answer_3 = st.radio("Entertain:", option_3)
#Question 4
st.text("4. What did Zaroff shoot while Rainsford was in bed?")
option_4 = ['A human','A deer','A cape buffalo','A dog']
answer_4 = st.radio("A dog:", option_4)

# Add a submit_button
submit_button = st.button("Submit")
if submit_button:
    if answer_1 == "Staccato":
        st.text("Correct! Here is a hint, Caesar Cipher")
    else:
        st.text("Incorrect. try again.")
    if answer_2 == "Astrakhan":
            st.text("Correct! decipher this code, abzivlml")
    else:
        st.text("Incorrect. try again.")
    if answer_3 == "Entertain":
        st.text("Correct! Decipher this code, cpnlulyl")
    else:
        st.text("Incorrect. try again.")
    if answer_4 == "A dog":
            st.text("Correct! Decipher this code, Qhl fvqh d acxj evwh vvh pabmlkz KSZVXXF ooac vlx bquulkz 3,7,6,2,5,1,4")
    else:
            st.text("Incorrect. try again.")
