import streamlit as st

st.title('SED生産計画展開アプリ!')
st.markdown(
    '''
    週次計画をDaily計画に落とし込みます!
    '''
)
with st.sidebar:
    st.subheader('News!🆕')
    st.text('画像認識AIが追加されました！')