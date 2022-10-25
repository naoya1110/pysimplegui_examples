# カウントアップするアプリ

# 公式ドキュメント
# https://www.pysimplegui.org/en/latest/readme%20Japanese/
# https://www.pysimplegui.org/en/latest/
# https://www.pysimplegui.org/en/latest/call%20reference/

# パッケージのインポート
import PySimpleGUI as sg
import time

# ウィンドウのカラーテーマ設定
sg.theme("DefaultNoMoreNagging") 

# 部品を作成
## CLOSEボタン
close_button_element = sg.Button(button_text="CLOSE", size=(10,3), key="CLOSE")

## START/STOPボタン
start_stop_button_element = sg.Button(button_text="START", size=(10,3), key="START_STOP")

## 値の表示
number_display_element = sg.Text(
                            text="0",
                            size=(10,1),
                            font=5,
                            key="NUMBER"
                            )

# アプリのレイアウトを設定，部品を2次元配列で配置
layout = [[number_display_element],
          [start_stop_button_element, close_button_element]]

count = 0
is_started = False
dt = 0

# ウィンドウを設定
window = sg.Window(
                    title="My App",  # ウィンドウのタイトル
                    layout=layout,  # レイアウト
                    size=(300, 300) # ウィンドウの大きさ
                    )

# 無限ループ
while True:
    
    # アプリ内で発生したイベントを読み取る
    event, values = window.read(timeout=20)
    
    # アプリの終了判定，CLOSEボタンが押される，または×ボタンでウィンドウが閉じられる
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break
    
    # START/STOPボタンが押されたら，is_startedに応じて時計をスタート／ストップする
    if event == "START_STOP":
        # is_startedがFalseならt0を取得してis_startedをTrueに変える
        if is_started==False:
            t0 = time.time()
            is_started = True
            start_stop_button_element.update(text="STOP")
        
        # is_startedがTrueならis_startedをFalseに変える
        elif is_started==True:
            is_started = False
            start_stop_button_element.update(text="START")
            
    # is_startedがTrueの間経過時間を計測して表示する
    elif is_started==True:
        dt = time.time() - t0
        number_display_element.update(dt)

    
        
# アプリを終了
window.close()