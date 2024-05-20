import streamlit as st
from PIL import Image
import pandas as pd#データ分析ライブラリのインポート
import sqlite3
DATABASE = 'water_level_data.db'#データベースの名前を定数に格納
st.text("(日付),(水位％),(登録者名)")
#データを降順で並び替えて表示する関数
con = sqlite3.connect(DATABASE)
c = con.cursor()
def show_data():
    c.execute('SELECT * FROM water_level_table ORDER BY survey_day DESC')#DESC降順でソート。昇順はASC
    data = c.fetchall()
    for d in data:
        st.write(d)
    c.close()
    con.close()        


# データの表示
show_data()