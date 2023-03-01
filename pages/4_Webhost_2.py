import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('4W2')

st.title('Boop! :ghost:')

image = './app/static/cat-background.png'

css = f'''
<style>
    .stApp {{
        background-image: url({image});
        background-size: cover;

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

st.title('Boop! :ghost:')

image = './app/static/cat-background.png'

css = f\'''
<style>
    .stApp {{
        background-image: url({image});
        background-size: cover;

    }}
    .stApp > header {{
        background-color: transparent;
    }}
</style>
\'''
st.markdown(css, unsafe_allow_html=True)
''')