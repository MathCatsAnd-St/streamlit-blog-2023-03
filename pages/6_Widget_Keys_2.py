import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('6K2')

st.session_state.clear()

st.slider('Test', 0, 10, key='my_key')





with st.expander('Show me'):
    st.code('''
import streamlit as st

st.session_state.clear()

st.slider('Test', 0, 10, key='my_key')
''')