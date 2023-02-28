import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('6K3')

switch = st.radio('Choice:', [1,2])

match switch:
    case 1:
        st.checkbox('1', key='1')
    case 2:
        st.checkbox('2', key='2')





with st.expander('Show me'):
    st.code('''
import streamlit as st

switch = st.radio('Choice:', [1,2])

match switch:
    case 1:
        st.checkbox('1', key='1')
    case 2:
        st.checkbox('2', key='2')
''')