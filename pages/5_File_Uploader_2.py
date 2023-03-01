import streamlit as st
import io

# To keep session state clean between examples
import page_freshener
page_freshener.reset('5F2')

file = st.file_uploader("Choose a file:", type=['css','py'])

if file != None:
    bytes_object = file.getvalue()
    string_object = bytes_object.decode("utf-8")

    st.code(string_object)





with st.expander('Show me'):
    st.code('''
import streamlit as st
import io

file = st.file_uploader("Choose a file:", type=['css','py'])

if file != None:
    bytes_object = file.getvalue()
    string_object = bytes_object.decode("utf-8")

    st.code(string_object)
''')