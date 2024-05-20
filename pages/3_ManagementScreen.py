import streamlit as st
import datetime
#データ入力関連ウィジェットを作る---------------------------------------------------------------------------------
with st.form(key='profile_form'):#with区の中に配置しないと、インプットボックスからカーソルを話した瞬間にリロードが働きうざい
        name = st.text_input("名前")#インプットされた値を変数に格納
        addres = st.text_input("住所")#デフォルトでは、ボックスからカーソルが離れた瞬間にリロードされる
        
    #セレクトボックスorラジオボタン
        age_category = st.selectbox(#ラジオボタンにする場合は、st.radioとするだけ。あとは一緒
        '年齢層',
        ('ジュニア)', 'シニア')
    )
        
    #複数選択(マルチセレクト)
        hobby = st.multiselect(
        '趣味',
        ('スポーツ', '読書', 'プログラミング', 'アニメ・映画', '釣り', '料理')
    )
        
        #チェックボックス
        mail_subscribe = st.checkbox('メールマガジンを購読する')
        
        #スライダー
        height = st.slider('身長', min_value=110, max_value=210)
        
        #日付
        start_date = st.date_input(
            '開始日',
            datetime.date(2022, 7, 1)   
        )
        
        #カラーピッカー
        color = st.color_picker('テーマカラー', '#00f900')
        
        #ボタン
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')#これを押すと、指定していないのに何故かst.textの内容が消去される？？
        
        #ボタンは、with区を用いない場合は以下のシンプルなメソッドで書いてもOK
        #submit_btn = st.button('送信')#ボタンの変数への返り値は、ボタンが押されたときにTrueが帰り、そうでないときはFalseが帰る。
        #cancel_btn = st.button('キャンセル')
        
        print(f'submit_btn: {submit_btn}')#帰り値の確認用。押されたらtrue,そうでなかったらfalseを返す確認用
        print(f'cancel_btn: {cancel_btn}')
        if submit_btn:
            st.text(f'ようこそ!{name}さん！{addres}へ配達いたします')#インプットボックスの内容を表示
            st.text(f'年齢層:{age_category}')#セレクトボックスの内容を表示
            st.text(f'趣味：{", ".join(hobby)}')#マルチセレクトの内容を表示