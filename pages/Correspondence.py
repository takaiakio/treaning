import streamlit as st
import mca
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import japanize_matplotlib
import base64
plt.rcParams['font.family'] = 'IPAexGothic'

st.title('コレスポンデンス分析')

uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

if uploaded_file is not None:
    df = pd.read_csv(
        uploaded_file,
        sep=',',
        engine='python',
        skiprows=0,
        index_col=0,
        header=0,
        na_values='-',
        encoding='shift-jis',
        )

st.markdown('### ↓アクセスログ')
st.dataframe(df)

'''
st.table(df)
csv = df.to_csv(index=False)  

# utf-8
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:application/octet-stream;base64,{b64}" download="result_utf-8.csv">Download Link</a>'
st.markdown(f"CSVファイルのダウンロード(utf-8):  {href}", unsafe_allow_html=True)

# utf-8(BOM)
b64 = base64.b64encode(csv.encode('utf-8-sig')).decode()
href = f'<a href="data:application/octet-stream;base64,{b64}" download="result_utf-8-sig.csv">Download Link</a>'
st.markdown(f"CSVファイルのダウンロード(utf-8 BOM):  {href}", unsafe_allow_html=True)
'''
mca_counts = mca.MCA(df, benzecri=False)#benzecri=Falseにしないと固有値が0になってしまう
rws = mca_counts.fs_r(N=2) #商品（行）の成分スコア　Nは保持する成分の数
cols = mca_counts.fs_c(N=2) #イメージ（列）の成分スコア　Nは保持する成分の数


fig = plt.figure() #わからない2
ax = plt.axes() #わからない3
#グラフのレイアウトを設定
plt.axhline(0, color='gray') #横線
plt.axvline(0, color='gray') #縦線
plt.xlabel('成分1', fontname="IPAexGothic",fontsize=10) #X軸のラベル fontname：日本語の文字化け防止にフォントを指定
plt.ylabel('成分2', fontname="IPAexGothic",fontsize=10) #Y軸のラベル


#商品（行）のプロット
plt.scatter(rws[:,0], rws[:,1], c='r',marker='s') #c:色、marker:マーク
labels = df.index
for label,x,y in zip(labels,rws[:,0],rws[:,1]):
    plt.annotate(label, xy=(x, y), fontname="IPAexGothic",fontsize=10,color = 'b')


#イメージ（列）のプロット
plt.scatter(cols[:,0], cols[:,1], c='c',marker='o',s=5)
labels = df.columns
for label,x,y in zip(labels,cols[:,0],cols[:,1]):
    plt.annotate(label, xy=(x, y), fontname="IPAexGothic",fontsize=10,color = 'c')

st.pyplot(fig)