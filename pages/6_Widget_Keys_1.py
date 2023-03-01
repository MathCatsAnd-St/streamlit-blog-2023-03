import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('6K1')

st.session_state.my_key = 1

st.slider('Test', 0, 10, key='my_key')





with st.expander('Show me'):
    st.code('''
import streamlit as st

st.session_state.my_key = 1

st.slider('Test', 0, 10, value=0, key='my_key')
''')