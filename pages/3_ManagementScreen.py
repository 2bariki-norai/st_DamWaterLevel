#管理画面
import streamlit as st
#from PIL import Image
import pandas as pd
from datetime import date# デートタイムモジュールのdate（日付）オブジェクトをインポート
import sqlite3

strToday = str(date.today())#今日の日付を取得
DATABASE = 'water_level_data.db'#データベースの名前を定数に格納
st.text('管理画面')

st.text('データベースの編集')
st.text('お知らせの作成')