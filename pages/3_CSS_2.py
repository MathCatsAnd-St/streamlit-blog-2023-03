import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('3C2')

# Layout your containers at the beginning
section1 = st.container()
section2 = st.container()
section3 = st.container()
section4 = st.container()

# Write to the different containers for your display elements
section1.subheader('Section 1')
section1.button('Button 1')

section2.subheader('Section 2')
section2.button('Button 2')

section3.subheader('Section 3')
section3.button('Button 3')

section4.subheader('Section 4')
section4.button('Button 4')

css='''
<style>
    section.main > div > div > div > div:nth-of-type(3) .stButton > button {
        color: green;
    }
    section.main > div > div > div > div:nth-of-type(3) .stButton > button:hover {
        color: violet;
        border-color: violet;
    }
    section.main > div > div > div > div:nth-of-type(3) .stButton > button:focus {
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

# Layout your containers at the beginning
section1 = st.container()
section2 = st.container()
section3 = st.container()
section4 = st.container()

# Write to the different containers for your display elements
section1.subheader('Section 1')
section1.button('Button 1')

section2.subheader('Section 2')
section2.button('Button 2')

section3.subheader('Section 3')
section3.button('Button 3')

section4.subheader('Section 4')
section4.button('Button 4')

css=\'''
<style>
    section.main > div > div > div > div:nth-of-type(3) .stButton > button {
        color: green;
    }
    section.main > div > div > div > div:nth-of-type(3) .stButton > button:hover {
        color: violet;
        border-color: violet;
    }
    section.main > div > div > div > div:nth-of-type(3) .stButton > button:focus {
        color: purple !important;
        border-color: purple !important;
        box-shadow: purple 0 0 0 .2rem;
    }
</style>
\'''

st.markdown(css, unsafe_allow_html=True)
''')