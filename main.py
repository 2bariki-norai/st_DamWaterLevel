import streamlit as st

import pandas as pd
from datetime import date# デートタイムモジュールのdate（日付）オブジェクトをインポート
import sqlite3

strToday = str(date.today())#今日の日付を取得
DATABASE = 'water_level_data.db'#データベースの名前を定数に格納

#データベースの最後の行を取得
con = sqlite3.connect(DATABASE)
c = con.cursor()
c.execute('SELECT max(survey_day), * FROM water_level_table')#conのSQL実行メソッドで、テーブルからデータをすべて取得する。
list = c.fetchall()#リスト変数にデータを格納
for row in list:#ループを回してレコードを書き出す
    lastday = str(row[1])#要素１：日付が書き出される
    lastlevel = str(row[2])#要素2：水位が書き出される
    lastuser = str(row[3])#要素３：ユーザーネームが書き出される。
c.close()   
con.close() 

st.caption(f'{strToday}')
#いろいろテキストを表示する-----------------------------------------------------------------
st.title('奥山ダム水位チェックアプリ')
st.caption('これは奥山ダムの水位を表示するテストアプリです。')
st.subheader('概要')#まあでかい。
st.text('ダム管理所への電話で確認したデータを、基本的には15日おきにチェックし、記録しています。')
st.text('最新のデータを確認された方は、ぜひ水位登録をお願いいたします。')

st.subheader(f'{lastday} 時点の水位は、{lastlevel}%です')



