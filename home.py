import streamlit as st

st.title('はじめてのStreamlit!')
st.markdown(
    '''
    これは私が**初めて**Streamlitで作ったアプリです！
    '''
)
with st.sidebar:
    st.subheader('News!🆕')
    st.text('画像認識AIが追加されました！')