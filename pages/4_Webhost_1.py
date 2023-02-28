import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('4W1')

if 'css' not in st.session_state:
    with open('files/my_css.css', 'r') as file:
        css = file.read()
    st.session_state.css = css

css = '<style>' + st.session_state.css + '</style>'

st.button('Click me!')

st.markdown(css, unsafe_allow_html=True)





with st.expander('Show me'):
    st.code('''
import streamlit as st

if 'css' not in st.session_state:
    with open('files/my_css.css', 'r') as file:
        css = file.read()
    st.session_state.css = css

css = '<style>' + st.session_state.css + '</style>'

st.button('Click me!')

st.markdown(css, unsafe_allow_html=True)
''')