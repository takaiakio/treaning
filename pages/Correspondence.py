import streamlit as st
import mca
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
#import numpy as np
import japanize_matplotlib
#import base64
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


mca_counts = mca.MCA(df, benzecri=False)#benzecri=Falseにしないと固有値が0になってしまう
rws = mca_counts.fs_r(N=2) #商品（行）の成分スコア　Nは保持する成分の数
cols = mca_counts.fs_c(N=2) #イメージ（列）の成分スコア　Nは保持する成分の数


fig = plt.figure(figsize=(12,12)) #サイズの調整
ax = plt.axes() #わからない3
#グラフのレイアウトを設定
plt.axhline(0, color='gray') #横線
plt.axvline(0, color='gray') #縦線
plt.xlabel('成分1', fontname="IPAexGothic",fontsize=15) #X軸のラベル fontname：日本語の文字化け防止にフォントを指定
plt.ylabel('成分2', fontname="IPAexGothic",fontsize=15) #Y軸のラベル

# grid表示
plt.grid(True)

# 軸範囲
plt.xlim(left=-1.5, right=1.5)
plt.ylim(bottom=-1.5, top=1.5)

# グラフタイトル
plt.title('コレポン出力', fontname="IPAexGothic",fontsize=15)


#商品（行）のプロット
plt.scatter(rws[:,0], rws[:,1], c='r',marker='s',s=10) #c:色、marker:マーク
labels = df.index
for label,x,y in zip(labels,rws[:,0],rws[:,1]):
    plt.annotate(label, xy=(x, y), fontname="IPAexGothic",fontsize=15,color = 'b')


#イメージ（列）のプロット
plt.scatter(cols[:,0], cols[:,1], c='c',marker='o',s=20)
labels = df.columns
for label,x,y in zip(labels,cols[:,0],cols[:,1]):
    plt.annotate(label, xy=(x, y), fontname="IPAexGothic",fontsize=20,color = 'c')



# x 軸 (major) の目盛りを設定する。
#ax.set_xticks(np.linspace(-1, 1, 5))

# x 軸 (minor) の目盛りを設定する。
#ax.set_xticks(np.linspace(-1,1, 5), minor=True)

# y 軸 (major) の目盛りを設定する。
#ax.set_yticks(np.linspace(-1, 1, 5))

# y 軸 (minor) の目盛りを設定する。
#ax.set_yticks(np.linspace(-1, 1, 5), minor=True)

st.pyplot(fig)

