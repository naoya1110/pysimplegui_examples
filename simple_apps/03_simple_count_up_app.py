# カウントアップするアプリ

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

## PUSH MEボタン
push_me_button_element = sg.Button(button_text="PUSH ME", size=(10,3), key="PUSH ME")

## 値の表示
number_display_element = sg.Text(
                            text="0",
                            size=(10,1),
                            font=5,
                            key="NUMBER"
                            )



# アプリのレイアウトを設定，部品を2次元配列で配置
layout = [[push_me_button_element, number_display_element],
          [close_button_element]]

count = 0

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
    
    # PUSH MEボタンが押されたらcountを+1してnumber_text_elementに表示する
    if event == "PUSH ME":
        count += 1
        number_display_element.update(count)
        
# アプリを終了
window.close()