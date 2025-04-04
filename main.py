import streamlit as st
# Title and subtitle code
st.markdown('<h1 style="font-size: 24px; text-align: center;">Escape Zaroff\'s Castle</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="font-size: 18px; text-align: center;">Answer quetions to unlock the code and uncipher the code.</h3>', unsafe_allow_html=True)

#background passage
passage = """
After your strange dinner with General Zaroff, Ivan directs you to your room. You try to sleep but you can't.
Then you hear a gunshot and you get up and look out the window and down below you see the eyes of Zaroff's dogs.
You go to the door and it’s locked with a seven digit code lock.
You look around the room and you see strange writing on the walls.
You look closer and it's a secret message."""
st.markdown(f'<p style="font-size: 12px; text-align: center;">{passage}</p>', unsafe_allow_html=True)

# Question 1
st.text("1. What is  short and sharp as a word?")
options_1 = ['Extremity', 'Palpable','Staccato', 'Scruples']
answer_1 = st.radio("", options_1)
#Question 2
st.text("2. What is a loosely curled fur made from lamb skin?")
option_2 = ['Capital','Droll','Analytical','Astrakhan']
answer_2 = st.radio("", option_2)
#Question 3
st.text("3. What is the author's purpose?")
option_3 = ['Entertain','Inform','Presuade','Describe']
answer_3 = st.radio("", option_3)
#Question 4
st.text("4. What did Zaroff shoot while Rainsford was in bed?")
option_4 = ['A human','A deer','A cape buffalo','A dog']
answer_4 = st.radio("", option_4)
#question 5
st.text("5. Where was Rainsford heading?")
option_5 = ('Africa','the Rockies','Africa','Caribbean')
answer_5 = st.radio("",option_5)
# Question 6
st.text("6. What did Rainsford lose when he fell of the boat?")
option_6 = ('Cigar','His watch','A coin','his shoe')
answer_6 = st.radio("",option_6)
#Question 7
st.text("7. What cracked Zaroff\'s rib cage?")
option_7 = ('his dog','an elk','a moose','a cape buffalo')
answer_7 = st.radio("",option_7)
#Question 8
st.text("")
option_8 = ('','','','')
answer_8 = st.radio("",option_8)

# Add a submit_button
submit_button = st.button("Submit")
if submit_button:
    if answer_1 == "Staccato" and answer_5 == "Caribbean":
        st.text("Here is a hint, Caesar Cipher")
    else:
        st.text("Incorrect. try again.")
    if answer_2 == "Astrakhan" and answer_6 == "Cigar":
            st.text("decipher this code, abzivlml")
    else:
        st.text("Incorrect. try again.")
    if answer_3 == "Entertain" and answer_7 == "cape buffalo":
        st.text("Decipher this code, cpnlulyl")
    else:
        st.text("Incorrect. try again.")
    if answer_4 == "A dog" and "":
            st.text("Decipher this code, Qhl fvqh d acxj evwh vvh pabmlkz KSZVXXF ooac vlx bquulkz 3,7,6,2,5,1,4")
    else:
            st.text("")
