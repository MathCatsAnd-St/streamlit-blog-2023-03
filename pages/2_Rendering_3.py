import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('2R3')

# Create a key in session state to track the stage
if 'stage' not in st.session_state:
    st.session_state.stage = 0

# Stage function to update the stage saved in session state
def set_stage(stage):
    st.session_state.stage = stage

st.write('Welcome! Click to begin.')
# Each button runs the Stage function, passing the stage number as an argument
st.button('Begin', on_click=set_stage, args=[1])

# Content for each stage within the body of an if statement
if st.session_state.stage > 0:
    st.write('This is stage 1. Do some things.') 
    st.button('Next', on_click=set_stage, args=[2])
if st.session_state.stage > 1:
    st.write('This is stage 2. Do some more things.')
    st.button('Finish', on_click=set_stage, args=[3])
if st.session_state.stage > 2:
    st.write('This is the end. Thank you!')
    st.button('Reset', on_click=set_stage, args=[0])





with st.expander('Show me'):
    st.code('''
import streamlit as st

# Create a key in session state to track the stage
if 'stage' not in st.session_state:
    st.session_state.stage = 0

# Stage function to update the stage saved in session state
def set_stage(stage):
    st.session_state.stage = stage

st.write('Welcome! Click to begin.')
# Each button runs the Stage function, passing the stage number as an argument
st.button('Begin', on_click=set_stage, args=[1])

# Content for each stage within the body of an if statement
if st.session_state.stage > 0:
    st.write('This is stage 1. Do some things.') 
    st.button('Next', on_click=set_stage, args=[2])
if st.session_state.stage > 1:
    st.write('This is stage 2. Do some more things.')
    st.button('Finish', on_click=set_stage, args=[3])
if st.session_state.stage > 2:
    st.write('This is the end. Thank you!')
    st.button('Reset', on_click=set_stage, args=[0])
''')