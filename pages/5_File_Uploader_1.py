import streamlit as st
import pandas as pd

# To keep session state clean between examples
import page_freshener
page_freshener.reset('5F1')

file = st.file_uploader("Choose a file:", key="loader", on_change=load_data, type='csv')

if file != None:
    df = pd.read_csv(file)





with st.expander('Show me'):
    st.code('''
import streamlit as st
import pandas as pd

file = st.file_uploader("Choose a file:", key="loader", on_change=load_data, type='csv')

if file != None:
    df = pd.read_csv(file)
''')