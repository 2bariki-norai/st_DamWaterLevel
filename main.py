#メイン画面
import streamlit as st
from PIL import Image
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
st.title('農水用ダム水位モニター')
st.caption('これはダムの水位を表示するウェブサイトです（テスト中）。')
st.subheader('概要')
st.text('ダム管理所への電話で確認したデータを、基本的には15日おきに\nチェックし、記録しています。')
st.text('最新のデータを確認された方は、ぜひ水位登録をお願いいたします。')

st.subheader(f'{lastday} 時点の水位は、{lastlevel}%です')

#image = Image.open('./data/4.png')
#st.image(image, width=200)

#機能追加・改善予定--------------------------------------------------------------------
#main.py
    #サイトのタイトルがダサい。なにか良い名前は？←一応OK！
    #概要以下のテキストがスマホで見ると見切れる。折り返す
    #requirements.txtにPILがあるとエラーが出る。PIL以外の画像処理を試す。
    #ネットで見たときに、日付の取得がうまく行ってないみたい。←もしかしたらstr(date.today())はグリニッジ標準時？？
    
    #このサイトの理念を簡潔に書く
#PastData.py
    #データベースの見栄えがすごく悪い。なんとかしたい。←OK!
    #過去に同じ日付がある場合、その日は書き込めないようにしたい。
    #降水量の棒グラフと、水位の折れ線グラフも追加したい。

#DataRegistration.py
    #水位登録のインプットボックスで、数字以外打てないようにしたい。←OK！
    #ラストデイ==strtodayがうまく動いてない。日付がかぶっても上書きされない←なんとかOK！
    #日付登録で、手打ちする場合はカレンダーから選ぶようにしたい。←OK！

#ManagementScreen.py
    #ページを開くときに、パスワードを求めるようにしたい。
    #このページ内で、データベースの修正ができるようにしたい。
    #大きいインプットボックスを用意して、ここで打ち込んだ内容がmain.py画面にお知らせとして表示できるようにしたい。

    #passwd = st.text_input('パスワード', type='password', max_chars=20)
    
