#メイン画面
import streamlit as st
#from PIL import Image
import pandas as pd
from datetime import date# デートタイムモジュールのdate（日付）オブジェクトをインポート
import datetime
import sqlite3

#今日の日付を取得
now = datetime.datetime.now()
# 現在の日時を取得
now = datetime.datetime.now()
# 9時間を表す timedelta オブジェクトを作成
nine_hours = datetime.timedelta(hours=9)
# 現在の日時に9時間を加算+グリニッジ標準時対策
now = now + nine_hours
# 日付部分を取得
today_date = now.date()
strToday = str(today_date)#今日の日付を文字列に変換

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

#st.caption(f'{strToday}')

st.caption(today_date)


#いろいろテキストを表示する-----------------------------------------------------------------
st.title('農水用ダム水位モニター')
st.subheader(f'{lastday} 時点の水位は、{lastlevel}%です')

st.subheader('概要')
st.text('これはダムの水位を表示するウェブサイトです（テスト中）。')
st.text('ダム管理所へ電話で確認したデータを\n基本的には15日おきに\nチェックし、記録しています。')

st.caption('<サイト作成の理由>')
st.caption('農家にとってダムの水位は重要ですが、現在は管理事務所に\n電話で確認するしか方法がありません。\nこれでは手間も電話代もかかるため、ウェブサイトで情報を共有し、多くの方に利用してもらいたいと思います。\nこのサイトは個人運営のため、情報がリアルタイムでなかったり誤っている場合があります。ご了承ください。')

#image = Image.open('./data/4.png')
#st.image(image, width=200)

#機能追加・改善予定--------------------------------------------------------------------
#main.py
    
    #requirements.txtにPILがあるとエラーが出る。PIL以外の画像処理を試す。
    #ネットで見たときに、日付の取得がうまく行ってないみたい。←もしかしたらstr(date.today())はグリニッジ標準時？？
#PastData.py
    #降水量の棒グラフと、水位の折れ線グラフも追加したい。
#DataRegistration.py
    
#ManagementScreen.py
    #ページを開くときに、パスワードを求めるようにしたい。
    
