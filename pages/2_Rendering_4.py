import streamlit as st
import pandas as pd

# To keep session state clean between examples
import page_freshener
page_freshener.reset('2R4')

# Initialize some object in session state where you will you be storing edits
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame({'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]})

# Optional: Assign the stored value to a convenient variable for brevity in code
df = st.session_state.df

st.dataframe(df)

cols = st.columns(3)
cols[0].number_input('A',0,100,step=1, key='A')
cols[1].number_input('B',0,100,step=1, key='B')
cols[2].number_input('C',0,100,step=1, key='C')

def add_row():
    row = [st.session_state.A, st.session_state.B, st.session_state.C]
    next_row = len(st.session_state.df)
    # Make sure modifcation is performed on the object in session state
    st.session_state.df.loc[next_row] = row

st.button('Add Row', on_click=add_row)





with st.expander('Show me'):
    st.code('''
import streamlit as st
import pandas as pd

# Initialize some object in session state where you will you be storing edits
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame({'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]})

# Optional: Assign the stored value to a convenient variable for brevity in code
df = st.session_state.df

st.dataframe(df)

cols = st.columns(3)
cols[0].number_input('A',0,100,step=1, key='A')
cols[1].number_input('B',0,100,step=1, key='B')
cols[2].number_input('C',0,100,step=1, key='C')

def add_row():
    row = [st.session_state.A, st.session_state.B, st.session_state.C]
    next_row = len(st.session_state.df)
    # Make sure modifcation is performed on the object in session state
    st.session_state.df.loc[next_row] = row

st.button('Add Row', on_click=add_row)
''')