import streamlit as st

input_text = st.text_input(label='ここにテキストを入力してみてください')
button_click = st.button('送信')

if button_click:

    if input_text:
        st.markdown(f'{input_text}"の判定結果は"**ポジティブ**"です！')
    else:
        st.markdown(f'テキストを入力してからボタンを押して下さい')