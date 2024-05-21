#過去の水位データ画面
import streamlit as st
from PIL import Image
import pandas as pd#データ分析ライブラリのインポート
import sqlite3

DATABASE = 'water_level_data.db'#データベースの名前を定数に格納

st.subheader('過去の水位データ')#ページタイトル
st.caption('2022.10.11〜2023.05まで渇水のため送水停止がありました。')


def show_data():#データを降順で並び替えて表示する関数
    con = sqlite3.connect(DATABASE)#データベースに接続
    c = con.cursor()#カーソルを設定
    c.execute('SELECT * FROM water_level_table ORDER BY survey_day DESC')#DESC降順でソート。昇順はASC
    data = c.fetchall()#リスト型で変数にすべて格納
    df = pd.DataFrame(data, columns=['日付', '水位（％）', '登録者名'])#pandasのメソッドで表敬式でdfにインスタンス化
    st.table(df.style.format({'水位（％）':'{:.1f}'}))#水位カラムを小数点第一位の設定をして、テーブルを表示する
    c.close()
    con.close()        

# データの表示関数を呼ぶ
show_data()


#データ分析関連ウィジェット-------------------------------------------------------------


#st.line_chart(df)#折れ線グラフで表示
#st.bar_chart(df['2021年'])#2021年分だけ棒グラフで表示