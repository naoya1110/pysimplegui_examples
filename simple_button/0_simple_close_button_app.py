# CLOSEボタンだけのシンプルなアプリ

# 公式ドキュメント
# https://www.pysimplegui.org/en/latest/readme%20Japanese/
# https://www.pysimplegui.org/en/latest/
# https://www.pysimplegui.org/en/latest/call%20reference/

# パッケージのインポート
import PySimpleGUI as sg

# ウィンドウのカラーテーマ設定
sg.theme("default") 

# 部品を作成
## CLOSEボタン
close_button_element = sg.Button(
                                "CLOSE",
                                size=(10,3),
                                key="CLOSE"
                                )

# アプリのレイアウトを設定，部品を2次元配列で配置
layout = [[close_button_element]]

# ウィンドウを設定
window = sg.Window(
                    title="Simple Button App",  # ウィンドウのタイトル
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