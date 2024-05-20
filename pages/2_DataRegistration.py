import streamlit as st
import sqlite3
from datetime import date# デートタイムモジュールのdate（日付）オブジェクトをインポート
DATABASE = 'water_level_data.db'#データベースの名前を定数に格納




#データベースを作る------------------------------
con = sqlite3.connect(DATABASE)#connectメソッドの引数にDATABASEを使ってdbへアクセスするオブジェクト(コネクションオブジェクト)をインスタンス化
con.execute("CREATE TABLE IF NOT EXISTS water_level_table (survey_day STRING ,water_level STRING ,user_name STRING)")
#con.execute("テーブルを作る。すでに同じ名前があれば無視。water_level_table (調査日：文字列型,水位：文字列型 登録者名：文字列型)")
#IF NOT EXISTSは作成済みのテーブルを作ろうとするエラーを防ぐ文。2回目以降にアプリを立ち上げたときに必要。
con.close()#作業が終わったらコネクションオブジェクトを閉じて、接続を断つ（トラブル防止）


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


st.caption('水位の登録')

# 登録日が重複しない場合、データを追加する
def add_data(survey_day, water_level, user_name):
    con = sqlite3.connect(DATABASE)#データベースに接続
    c = con.cursor()#カーソルは表の行へのポインタと考えることができる。操作にはこれがいる
    c.execute('INSERT INTO water_level_table (survey_day, water_level, user_name) VALUES (?, ?, ?)', (survey_day, water_level, user_name))
    con.commit()
    st.write('Data added. Please reload page.')
    c.close()
    con.close()
    



# データの追加
strtoday = str(date.today())#今日の日付を取得
survey_day = st.text_input('登録日', strtoday)#今日の日付を初期値として登録
water_level = st.text_input('水位')
user_name = st.text_input('名前(記入しなくてもOK)')

if st.button('水位を登録'):#ボタンを押すと実行される処理
    if lastday == survey_day:#今日の日付がデータベースの最後の日付と一緒なら
        #up_data(survey_day, water_level, user_name)#データを上書きする
        #登録日が重複したら、データを上書きする。
        def up_data():#同じ日付のカラムの水位データを上書きする。
    #sql=f"UPDATE water_level_table SET water_level = \"{water_level}\" WHERE survey_day = \"{lastday}\";"
    #UPDATE テーブル名 SET カラム名1 = 値1, カラム名2 = 値2, ... WHERE 条件式;
            sql=f"UPDATE water_level_table SET water_level = \"{water_level}\" ,user_name = \"{user_name}\" WHERE survey_day = \"{lastday}\";"
            return sql
    
        con = sqlite3.connect(DATABASE)#データベースへのコネクションオブジェクトを変数にインスタンス化
        c = con.cursor()#カーソルは表の行へのポインタと考えることができるらしい。操作にはこれがいるみたい
        c.execute(up_data())#sql_Var関数で作ったSQL文を実行する。
        con.commit()
        c.close()
        con.close()
    else:#そうでないなら
        add_data(survey_day, water_level, user_name)#データを追加する

