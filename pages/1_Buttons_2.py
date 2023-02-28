import streamlit as st

# To keep session state clean between examples
import page_freshener
page_freshener.reset('1B2')

if st.button('First Button'):
    st.write('The first button was clicked.')
    if st.button('Second Button'):
        # This will never execute!
        st.write('The second button was clicked')





with st.expander('Show me'):
    st.code('''
import streamlit as st

if st.button('First Button'):
    st.write('The first button was clicked.')
    if st.button('Second Button'):
        # This will never execute!
        st.write('The second button was clicked')
''')