# どのボタンが押されたか表示するアプリ

# 公式ドキュメント
# https://www.pysimplegui.org/en/latest/readme%20Japanese/
# https://www.pysimplegui.org/en/latest/
# https://www.pysimplegui.org/en/latest/call%20reference/

# パッケージのインポート
import PySimpleGUI as sg

# ウィンドウのカラーテーマ設定
sg.theme("DefaultNoMoreNagging") 

# 部品を作成
## CLOSEボタン
close_button_element = sg.Button(button_text="CLOSE", size=(10,3), key="CLOSE")

## ３つのボタンの部品
button_1_element = sg.Button(button_text="1", size=(10,3), key="BUTTON 1")
button_2_element = sg.Button(button_text="2", size=(10,3), key="BUTTON 2")
button_3_element = sg.Button(button_text="3", size=(10,3), key="BUTTON 3")

## メッセージの表示
text_display_element = sg.Text(
                            text="",
                            size=(30,1),
                            font=5,
                            key="TEXT DISP"
                            )



# アプリのレイアウトを設定，部品を2次元配列で配置
layout = [[button_1_element, button_2_element, button_3_element],
          [text_display_element],
          [close_button_element]]

count = 0

# ウィンドウを設定
window = sg.Window(
                    title="Task 01",  # ウィンドウのタイトル
                    layout=layout,  # レイアウト
                    size=(400, 300) # ウィンドウの大きさ
                    )

# 無限ループ
while True:
    
    # アプリ内で発生したイベントを読み取る
    event, values = window.read(timeout=20)
    
    # アプリの終了判定，CLOSEボタンが押される，または×ボタンでウィンドウが閉じられる
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break
    
    # PUSH MEボタンが押されたらcountを+1してnumber_text_elementに表示する
    if event == "BUTTON 1":
        text_display_element.update("1を押しました")
    if event == "BUTTON 2":
        text_display_element.update("2を押しました")
    if event == "BUTTON 3":
        text_display_element.update("3を押しました")
        
# アプリを終了
window.close()