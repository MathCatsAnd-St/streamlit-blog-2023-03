import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('2R1')

name = st.text_input('Name:')
if name != '':
    st.write(f'Hi, {name}! Nice to meet you.')





with st.expander('Show me'):
    st.code('''
import streamlit as st

name = st.text_input('Name:')
if name != '':
    st.write(f'Hi, {name}! Nice to meet you.')
''')