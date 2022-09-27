# スライダの値を表示するアプリ

# 公式ドキュメント
# https://www.pysimplegui.org/en/latest/readme%20Japanese/
# https://www.pysimplegui.org/en/latest/
# https://www.pysimplegui.org/en/latest/call%20reference/


# パッケージのインポート
import PySimpleGUI as sg
import cv2
import numpy as np

# ウィンドウのカラーテーマ設定
sg.theme("DefaultNoMoreNagging") 


# ダミー画像を作成
img = np.ones((200, 200, 3), dtype="uint8")*255         # 白の背景を作成
img = cv2.circle(img, (100, 100), 50, (0, 255, 0), 3)   # 緑の円を描く
img = cv2.imencode('.png', img)[1].tobytes()            # 画像のデータ形式を変換

# 部品を作成
## CLOSEボタン
close_button_element = sg.Button(button_text="CLOSE", size=(10,3), key="CLOSE")

## 画像表示
img_element = sg.Image( data=img,
                        size=(200,200),
                        key="IMAGE")




# アプリのレイアウトを設定，部品を2次元配列で配置
layout = [[img_element],
          [close_button_element]]


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

# アプリを終了
window.close()