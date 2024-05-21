#水位登録画面
import streamlit as st
import sqlite3
from datetime import date# デートタイムモジュールのdate（日付）オブジェクトをインポート
DATABASE = 'water_level_data.db'#データベースの名前を定数に格納
lastday = ""#グローバルなスコープとして変数を作っておく
st.header('水位の登録')


#データベースを作る------------------------------------------------------------------------------------
con = sqlite3.connect(DATABASE)#connectメソッドの引数にDATABASEを使ってdbへアクセスするオブジェクト(コネクションオブジェクト)をインスタンス化
con.execute("CREATE TABLE IF NOT EXISTS water_level_table (survey_day STRING ,water_level STRING ,user_name STRING)")
#con.execute("テーブルを作る。すでに同じ名前があれば無視。water_level_table (調査日：文字列型,水位：文字列型 登録者名：文字列型)")
#IF NOT EXISTSは作成済みのテーブルを作ろうとするエラーを防ぐ文。2回目以降にアプリを立ち上げたときに必要。
con.close()#作業が終わったらコネクションオブジェクトを閉じて、接続を断つ（トラブル防止）


#データベースの最後の行を取得------------------------------------------------------------------------------
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



# データのインプット--------------------------------------------------------------------------------
strtoday = str(date.today())#今日の日付を取得
survey_day = st.date_input('登録日', date.today())#今日の日付を初期値として登録
water_level = st.number_input('水位')#水位を数値として登録
user_name = st.text_input('名前(記入しなくてもOK)')#登録者名を登録


#水位の登録部分。バルーンが飛んだら上書き。雪が降ったら新たに追加。-----------------------------------
if st.button('水位を登録'):#ボタンを押すと実行される処理
    lastday = str(lastday)
    survey_day = str(survey_day)#型が違うとifを通り抜けるので型を合わせる。
   
    if lastday == survey_day:#今日の日付がデータベースの最後の日付と一緒なら上書き
        
        def up_data():#同じ日付のカラムの水位データを上書きする。
            sql=f"UPDATE water_level_table SET water_level = \"{water_level}\" ,user_name = \"{user_name}\" WHERE survey_day = \"{lastday}\";"
            return sql
    
        con = sqlite3.connect(DATABASE)#データベースへのコネクションオブジェクトを変数にインスタンス化
        c = con.cursor()#カーソルは表の行へのポインタと考えることができるらしい。操作にはこれがいるみたい
        c.execute(up_data())#sql_Var関数で作ったSQL文を実行する。
        con.commit()#コミットで上書きを固定
        c.close()
        con.close()
        st.write('Data updated. Please reload page.')#データが追加されました。と表示
        st.balloons()#バルーンを飛ばす
        
    else:#日付が違うなら追加書き
        
        con = sqlite3.connect(DATABASE)#データベースに接続
        c = con.cursor()#カーソルは表の行へのポインタと考えることができる。操作にはこれがいる
        c.execute('INSERT INTO water_level_table (survey_day, water_level, user_name) VALUES (?, ?, ?)', (survey_day, water_level, user_name))
        con.commit()
        c.close()
        con.close()
        st.write('Data added. Please reload page.')#データが追加されました。と表示
        st.snow()#雪がふる

