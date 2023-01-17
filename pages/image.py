import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(font_scale=2)

st.title('AI for Images!📷')
st.markdown('**画像**向けのAIデモページだよ！')
input_file = st.file_uploader(label='Upload Image File!',type=['png','jpg'])

clm1, clm2 = st.columns([1, 1.5])
with clm1:
    if input_file is not None:
        img = Image.open(input_file)
        st.image(img)
with clm2:
    if input_file is not None:
        score_test = [0.9, 0.1]
        label_test = ['Cat', 'Dog']

        fig = plt.figure(figsize=(15,10))
        sns.barplot(
            data=pd.DataFrame({'score':score_test, 'label':label_test}),
            x='score',
            y='label',
            palette=sns.color_palette('dark:#5A9_r')
        )
        st.pyplot(fig)