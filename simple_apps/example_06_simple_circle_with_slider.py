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
img = cv2.circle(img, center=(100, 100), radius=50, color=(0, 255, 0), thickness=3)   # 緑の円を描く
img = cv2.imencode('.png', img)[1].tobytes()            # 画像のデータ形式を変換

# 部品を作成
## CLOSEボタン
close_button_element = sg.Button(button_text="CLOSE", size=(10,3), key="CLOSE")

## 画像表示
img_element = sg.Image( data=img,
                        size=(200,200),
                        key="IMAGE")

## スライダ
slider_element = sg.Slider(
                        range=(0,100),
                        default_value=50,
                        orientation="h", # "h" or "v"
                        size=(22,30),
                        enable_events=True,
                        disable_number_display=False,
                        key="SLIDER")


# アプリのレイアウトを設定，部品を2次元配列で配置
layout = [[img_element],
          [slider_element],
          [close_button_element]]


# ウィンドウを設定
window = sg.Window(
                    title="Simple Image App",  # ウィンドウのタイトル
                    layout=layout,  # レイアウト
                    size=(300, 400) # ウィンドウの大きさ
                    )




# 無限ループ
while True:
    
    # アプリ内で発生したイベントを読み取る
    event, values = window.read(timeout=20)
    
    # アプリの終了判定，CLOSEボタンが押される，または×ボタンでウィンドウが閉じられる
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break

    # スライダが動かされたらスライダの値に応じた円を描くに表示する
    if event == "SLIDER":
        radius = values["SLIDER"]   # スライダの値を取得
        radius = int(radius) # 整数の値に変換
        
        # 画像を作成
        img = np.ones((200, 200, 3), dtype="uint8")*255         # 白の背景を作成
        img = cv2.circle(img, center=(100, 100), radius=radius, color=(0, 255, 0), thickness=3)   # 緑の円を描く
        img = cv2.imencode('.png', img)[1].tobytes()            # 画像のデータ形式を変換
        
        # 画像を更新
        img_element.update(data=img)

# アプリを終了
window.close()