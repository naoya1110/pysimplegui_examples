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
img_dummy = np.ones((200, 200, 3), dtype="uint8")*255         # 白の背景を作成
img_dummy = cv2.imencode('.png', img_dummy)[1].tobytes()            # 画像のデータ形式を変換

# 部品を作成
## CLOSEボタン
close_button_element = sg.Button(button_text="CLOSE", size=(10,3), key="CLOSE")

## ファイルパスを表示
filepath_element = sg.InputText(size=(25, 1), enable_events=True, key="FILEPATH")

## ファイルブラウズボタン
file_browser_element = sg.FileBrowse(key="FILE BROWSE")

## 画像表示
img_element = sg.Image(data=img_dummy,
                       size=(200,200),
                       key="IMAGE")




# アプリのレイアウトを設定，部品を2次元配列で配置
layout = [[filepath_element, file_browser_element],
          [img_element],
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
    
    # ファイルパスが更新されたら画像を読み込んで表示
    if event == "FILEPATH":
        filepath = values["FILEPATH"]
        img = cv2.imread(filepath)
        img = cv2.resize(img, (200, 200))
        img = cv2.imencode('.png', img)[1].tobytes()
        img_element.update(data=img)
        

# アプリを終了
window.close()