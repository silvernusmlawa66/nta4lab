import streamlit as st
import random

st.little('Guess the number game')

#generate a rondom number between 1 and 100
number = random.randint(1,100)

guess = st.number_input("enter a number(1 and 100):,min_value=1,max_value=100)
                       
if st.button('make a guess!'):
    if guess > number:
        st.write('Too high! try a smaller number.')
    elief guess < number:
        st.write('Too low! try a lager number.')
    else:
        st.write('congraturations! you have guessed the number correctly.')               
                       
          
