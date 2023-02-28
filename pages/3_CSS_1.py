import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('3C1')

st.button('Click me!')

css='''
<style>
    .stButton > button {
        color: red;
    }
    .stButton > button:hover {
        color: violet;
        border-color: violet;
    }
    .stButton > button:focus {
        color: purple !important;
        border-color: purple !important;
        box-shadow: purple 0 0 0 .2rem;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)





with st.expander('Show me'):
    st.code('''
import streamlit as st

st.button('Click me!')

css=\'''
<style>
    .stButton > button {
        color: red;
    }
    .stButton > button:hover {
        color: violet;
        border-color: violet;
    }
    .stButton > button:focus {
        color: purple !important;
        border-color: purple !important;
        box-shadow: purple 0 0 0 .2rem;
    }
</style>
\'''

st.markdown(css, unsafe_allow_html=True)
''')