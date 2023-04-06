
import streamlit as st
import openpyxl
import datetime
import pandas as pd
import msoffcrypto
from pathlib import WindowsPath
import tempfile
import xlrd
import sys

st.title('週次計画展開')



option=('C:\\Users\\ALJP18540403\\Desktop\\改善人間\\瞳依頼\\2022\\1208\\PKG週次計画_221121マクロVer9.04.xlsm',
        'C:\\Users\\ALJP18540403\\Desktop\\改善人間\\瞳依頼\\2022\\1208\\MAGIC週次計画_221118(金).xlsx',
        range(3,11),
        )
sel=st.selectbox('ファイルを選択していください',option)
'あなたが選んだファイルは',sel,'です。'

'''if st.button('表示する'):
    df = pd.read_excel(sel,sheet_name='ＡＳＥ Goma')
    st.table(df)'''

#'2022-12-12 00:00:00'
input_text = st.text_input(label='ここに日付を入力してください yyyy-mm-dd 00:00:00')
button_click = st.button('実行')

if button_click:

    if input_text:
        # パスワード
        PASSWORD = "3239"
        # 暗号化されたファイル
        encrypted_file_name = sel
        # 復号化して保存するファイル
        decrypted_file_name = sel+"パスワード解除後.xlsm"
        
        # 暗号化ファイルを開く
        f = open(encrypted_file_name, "rb")
        encrypted_file = msoffcrypto.OfficeFile(f)
        # 復号化のパスワードを設定する
        encrypted_file.load_key(password=PASSWORD)
        
        # 復号化したファイルを別のファイルに保存する
        decrypted_file = open(decrypted_file_name, "wb")
        encrypted_file.decrypt(decrypted_file)
        workbook_0 = openpyxl.load_workbook(decrypted_file_name, data_only=True)
        sheet_0 = workbook_0["ＡＳＥ Goma"]
    
        workbook_1 = openpyxl.load_workbook('C:\\Users\\ALJP18540403\\Desktop\\改善人間\\瞳依頼\\2022\\1208\\MAGIC週次計画_221118(金).xlsx', data_only=True)
        sheet_1 = workbook_1["顧客要求、生産計画 "]

        for i in range(116,148):
            cell_value = sheet_1.cell(row=i, column=1).value
            if cell_value=="HGARAN008A":
             #gyo='行目です'
             #print(str(i)+gyo)
             break

        for j in range(130,183):
            cell_value = sheet_1.cell(row=9, column=j).value

            if cell_value==pd.to_datetime(input_text):

             retsu='列目です'
             #print(str(j)+retsu)
             break

        #st.markdown(f'{input_text}"の判定結果は"{str(j)+retsu}')
        for k in range(24,56):
            cell_value = sheet_0.cell(row=k, column=1).value
            if cell_value=="HGARAN008A":
            #gyo='行目です'
            #print(str(k)+gyo)
             break

        for l in range(150,188):
            cell_value = sheet_0.cell(row=k-3, column=l).value

            if cell_value==pd.to_datetime(input_text):

            #retsu='列目です'
            #print(str(l)+retsu)
             break

        n=0
        for m in range(j,j+24):
            
            bachelor = sheet_1.cell(row = i, column = m).value
            sheet_0.cell(row = k, column = l+n, value = bachelor)
            n += 1
        workbook_0.save(filename = sel+'入力後.xlsx'
                                    )
        st.markdown(f'{input_text}"の展開は完了しました！"')

    else:
        st.markdown(f'日付を入力してから実行ボタンを押して下さい')
        sys.exit()





