import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('4W2')

image = './app/static/cat_background.jpg'

css = f'''
<style>
    .stApp {{
        background-image: url({image});
    }}
    .stApp > header {{
        background-color: transparent;
    }}
</style>
'''
st.markdown(css, unsafe_allow_html=True)





with st.expander('Show me'):
    st.code('''
import streamlit as st

image = './app/static/cat_background.jpg'

css = f\'''
<style>
    .stApp {{
        background-image: url({image});
    }}
    .stApp > header {{
        background-color: transparent;
    }}
</style>
\'''
st.markdown(css, unsafe_allow_html=True)
''')