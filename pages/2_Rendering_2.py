import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('2R2')

# Create a key in session state to record the user's choice, defaulting to None
if 'favorite_color' not in st.session_state:
    st.session_state.favorite_color = None

# Confirmation function to record the user's choice into the favorite_color key
def confirm_color():
    st.session_state.favorite_color = st.session_state.color_picker

name = st.text_input('Name:')
if name != '':
    st.write(f'Hi, {name}! Nice to meet you.')
    st.write(f'What\'s your favorite color?')
    # Confirmation function will run if the user changes the widget
    color = st.color_picker('Color:', key='color_picker', on_change=confirm_color)
    if st.session_state.favorite_color is None:
        # Or, Confirmation function will run if user confirms the default
        st.button('Confirm Black', on_click=confirm_color)
    else:
        st.write(f'<span style="color:{color}">Oh, nice color choice!</span>', 
            unsafe_allow_html=True)





with st.expander('Show me'):
    st.code('''
import streamlit as st

# Create a key in session state to record the user's choice, defaulting to None
if 'favorite_color' not in st.session_state:
    st.session_state.favorite_color = None

# Confirmation function to record the user's choice into the favorite_color key
def confirm_color():
    st.session_state.favorite_color = st.session_state.color_picker

name = st.text_input('Name:')
if name != '':
    st.write(f'Hi, {name}! Nice to meet you.')
    st.write(f'What\'s your favorite color?')
    # Confirmation function will run if the user changes the widget
    color = st.color_picker('Color:', key='color_picker', on_change=confirm_color)
    if st.session_state.favorite_color is None:
        # Or, Confirmation function will run if user confirms the default
        st.button('Confirm Black', on_click=confirm_color)
    else:
        st.write(f'<span style="color:{color}">Oh, nice color choice!</span>', 
            unsafe_allow_html=True)
''')