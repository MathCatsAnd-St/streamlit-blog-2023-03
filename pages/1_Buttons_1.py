import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('1B1')

if st.button('Submit'):
    st.write('Submitted!')

if st.button('Confirm'):
    st.write('Confirmed!')





with st.expander('Show me'):
    st.code('''
import streamlit as st

if st.button('Submit'):
    st.write('Submitted!')

if st.button('Confirm'):
    st.write('Confirmed!')
''')